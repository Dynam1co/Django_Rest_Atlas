from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.core.exceptions import PermissionDenied
from django.views import debug
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from budget.api import BudgetMonthlyList, BudgetMonthlyDetail
from budget.api import BudgetTypeList


def permission_denied_view(request):
    raise PermissionDenied


schema_view = get_schema_view(
   openapi.Info(
      title="Atlas API",
      default_version='v1',
      description="Method list for Atlas API",
      terms_of_service="https://twitter.com/AsensiFj",
      contact=openapi.Contact(email="fjasensi@outlook.com"),
      license=openapi.License(name="GPL-3.0"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', debug.default_urlconf),
    url(r'^api/1.0(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^api/1.0/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/1.0/budget_entry/$', BudgetMonthlyList.as_view(), name='budget_entry'),
    url(r'^api/1.0/budget_entry/(?P<pk>[0-9]+)$', BudgetMonthlyDetail.as_view(), name='budgetmonthly-detail'),
    url(r'^api/1.0/entry_type/$', BudgetTypeList.as_view(), name='entry_type'),
]
