from rest_framework import serializers
from budget.models import BudgetMonthly
from budget.models import BudgetType


class BudgetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetType
        fields = '__all__'


class BudgetMonthlyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetMonthly
        fields = [
            'id',
            'url',
            'amount',
            'type_id'
        ]


class BudgetMonthlyDetailSerializer(serializers.ModelSerializer):
    type_id = BudgetTypeSerializer(many=False)

    class Meta:
        model = BudgetMonthly
        fields = '__all__'
