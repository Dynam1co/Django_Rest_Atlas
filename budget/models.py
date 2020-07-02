from django.db import models
import datetime


class BudgetType(models.Model):
    description = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.description


class BudgetEntryCategory(models.Model):
    description = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.description


class BudgetMonthly(models.Model):
    now = datetime.datetime.now()

    year_number = models.IntegerField(blank=False, null=False, default=now.year)
    month_number = models.IntegerField(blank=False, null=False, default=now.month)
    day_number = models.IntegerField(blank=False, null=False, default=now.day)
    type_id = models.ForeignKey(
        BudgetType,
        models.DO_NOTHING,
        blank=False,
        null=False
        )
    category_id = models.ForeignKey(
        BudgetEntryCategory,
        models.DO_NOTHING,
        blank=False,
        null=False
        )
    amount = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.id)
