from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    model_no = models.CharField(max_length=255)
    copy = models.PositiveIntegerField()
    date = models.DateField()
    per_copy_rate = models.DecimalField(max_digits=10, decimal_places=2)
    mob = models.CharField(max_length=10)  # No validation
    franchise_name = models.CharField(max_length=255, blank=True, null=True)
    advance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f'{self.customer_name} - {self.model_no}'


class CompletedOrders(models.Model):
    customer_name = models.CharField(max_length=255)
    model_no = models.CharField(max_length=255)
    copy = models.PositiveIntegerField()
    date = models.DateField()
    franchise_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.customer_name} - {self.model_no}'