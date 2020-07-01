from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from budget.models import BudgetMonthly, BudgetType
from budget.serializers import BudgetMonthlyListSerializer
from budget.serializers import BudgetTypeSerializer
from budget.serializers import BudgetMonthlyDetailSerializer


class BudgetMonthlyList(ListCreateAPIView):
    queryset = BudgetMonthly.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BudgetMonthlyListSerializer


class BudgetMonthlyDetail(RetrieveAPIView):
    queryset = BudgetMonthly.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BudgetMonthlyDetailSerializer


class BudgetTypeList(ListAPIView):
    queryset = BudgetType.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BudgetTypeSerializer
