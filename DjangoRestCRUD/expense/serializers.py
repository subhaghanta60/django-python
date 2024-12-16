from rest_framework import serializers

from .models import Transaction

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Transaction

        fields = [
            "id",
            "title",
            "amount",
           "transaction_type"
        ]
        #fields = '_all_'
        #exclude= ['transaction_type']


