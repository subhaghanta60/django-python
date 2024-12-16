from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionSerializers
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from django.db.models import Sum

# Create your views here.


@api_view(['GET','POST'])
def get_transactions(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializers(queryset, many=True)

    return Response({
       "data": serializer.data
   })
    


class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transaction.objects.all().order_by('-pk')
        serializer = TransactionSerializers(queryset, many=True)

        return Response({
         "data": serializer.data,
         "total" : round(queryset.aggregate(total = Sum('amount'))['total'] or 0,2)
        })

    def post(self, request):
        req_data = request.data
        serializer = TransactionSerializers(data = req_data)
        if not serializer.is_valid():
            return Response({
                "message": "Data Is not saved",
                "errors" : serializer.errors,
            })
        serializer.save()
        return Response({
            "message": "Data is Saved",
           "data": serializer.data
        })

    def put(self, request):
        data=request.data

        if not data.get('id'):
             return Response({
                "message": "Data not Updated",
                "errors": "ID is required"
                
            })
        
        transactions =Transaction.objects.get(id=data.get('id'))
        serializer = TransactionSerializers(transactions,data=data)


        if not serializer.is_valid():
            return Response({
                "message": "Data Is not saved",
                "errors" : serializer.errors,
            })
        serializer.save()
        
        return Response({
            "message": "Data is Saved",
           "data": serializer.data
        })
    def patch(self, request):
        data=request.data

        if not data.get('id'):
             return Response({
                "message": "Data not Updated",
                "errors": "ID is required"
                
            })
        
        transactions =Transaction.objects.get(id=data.get('id'))
        serializer = TransactionSerializers(transactions,data=data,partial=True)


        if not serializer.is_valid():
            return Response({
                "message": "Data Is not saved",
                "errors" : serializer.errors,
            })
        serializer.save()

        return Response({
            "message": "Data is Saved",
           "data": serializer.data
        })

    def delete(self,request):
        data=request.data

        if not data.get('id'):
             return Response({
                "message": "Data not Updated",
                "errors": "ID is required"
                
            })
        
        transactions =Transaction.objects.get(id=data.get('id')).delete()
       

        return Response({
            "message": "Data Deleted",
           "data": {}
        })
