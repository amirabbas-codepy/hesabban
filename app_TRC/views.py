from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.http import JsonResponse
from app_TRC.api.serializers import TrancionSerializer, UserSerializer
from app_TRC.models import Trancion
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Sum
# Create your views here.

User = get_user_model()

# def say_hello(request):
#     """
#     view
#     """
#     return HttpResponse('hello')

# def say_goodby(request):
#     """
#     view and html
#     """
#     return render(request, 'index.html')

# def say_dad(request):
#     """
#     view and model
#     """
#     firs_pain = Trancion.objects.first()
#     # firs_pain.pain += 'amir'
#     return HttpResponse(firs_pain.id)

# def say_last(request):
#     """
#     viwes and models and templates
#     """
#     firs_pain = Trancion.objects.first()
#     return render(request, 'firstpain.html', {'first_pain':firs_pain})

# def api_1(request):

#     return JsonResponse({'status':'success'})


@api_view(['GET'])
def trancion_list(request):
    # Trancions_list = Trancion.objects.values('amount', 'code', 'date', 'user_TRC', 'descripition', 'status_TRC')
    # return JsonResponse({'data':[item for item in Trancions_list]})
    serializer = TrancionSerializer(Trancion.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['POST'])
def sign_in(request):
    serializer = UserSerializer(data=request.data) 

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password: 
        return Response({'error':'username and password required'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        return Response({'messages':'success'}, status=status.HTTP_200_OK)
    
    return Response({'error':'Invalid user'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def get_trancions(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password: 
        return Response({'error':'username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        serializer = TrancionSerializer(Trancion.objects.filter(user_TRC=user), many=True) 

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def save_trancions(request):
    username = request.data.get('username')
    password = request.data.get('password')
    amount = request.data.get('amount')
    code = request.data.get('code')
    date = request.data.get('date')
    status_ = request.data.get('status')
    descripition = request.data.get('descripition')
    # print(date)
    # print(status_)

    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        data = {"amount":amount, 
                "descripition":descripition, 
                "date":date,
                "code":code, 
                "status_TRC":status_
                } 
        
        serializer = TrancionSerializer(data=data)

        if serializer.is_valid():
            serializer.save(user_TRC=user)
            return Response(status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error':'Invalid User!!!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def report_Trancions(request):
    username = request.data.get('username')
    password = request.data.get('password')
    # print(password, username)
    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        trancions = Trancion.objects.filter(user_TRC=user)
        # print(trancions)
        result1 = trancions.filter(status_TRC='cost').aggregate(total=Sum('amount'))
        result2 = trancions.filter(status_TRC='incom').aggregate(total=Sum('amount'))
        result3 = TrancionSerializer(trancions.filter(status_TRC='incom'), many=True)
        result4 = TrancionSerializer(trancions.filter(status_TRC='cost'), many=True)
        
        total_cost = result1['total']
        total_incom = result2['total']
        if total_cost and total_incom:
            profit = total_incom - total_cost
        else:
            profit = 0

        data = {'total_cost':total_cost, 
                'total_incom':total_incom, 
                'profit':profit, 
                'all_incom':result3.data,
                'all_cost':result4.data}

        return Response(data, status=status.HTTP_200_OK) 

    return Response({'error':'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delet_trnacions(request):
    username = request.data.get('username')
    password = request.data.get('password')
    id_trc = request.data.get('id')

    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        trancions = Trancion.objects.filter(user_TRC=user)
        try:
            trancions.get(id=id_trc).delete()
            
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response({'success':'del successfully!!'}, status=status.HTTP_200_OK)
    
    return Response({'error':'Invalid user!!!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def filter_trancions(request):
    username = request.data.get('username')
    password = request.data.get('password')
    date_filter = request.data.get('date')
    # print(type(date_filter), date_filter)

    user = authenticate(request=request, username=username, password=password)    

    if user is not None:
        trancions_user = Trancion.objects.filter(user_TRC=user)
        serializer = TrancionSerializer(trancions_user.filter(date=date_filter), many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({'error':'Invalid user!!'}, status=status.HTTP_400_BAD_REQUEST)