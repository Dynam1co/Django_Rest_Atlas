from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from budget.models import BudgetMonthly, BudgetType, BudgetEntryCategory
from budget.serializers import BudgetMonthlyListSerializer
from budget.serializers import BudgetTypeSerializer
from budget.serializers import BudgetMonthlyDetailSerializer
from budget.serializers import BudgetEntryCategoryListSerializer


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


class BudgetEntryCategoryList(ListAPIView):
    queryset = BudgetEntryCategory.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BudgetEntryCategoryListSerializer
