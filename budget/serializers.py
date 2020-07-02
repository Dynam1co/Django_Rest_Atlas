from rest_framework import serializers
from budget.models import BudgetMonthly
from budget.models import BudgetType
from budget.models import BudgetEntryCategory


class BudgetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetType
        fields = '__all__'


class BudgetEntryCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetEntryCategory
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
    category_id = BudgetEntryCategoryListSerializer(many=False)

    class Meta:
        model = BudgetMonthly
        fields = '__all__'
