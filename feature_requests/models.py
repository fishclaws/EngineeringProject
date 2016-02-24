from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class ConcurrentModificationError( Exception ): pass

class Client(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class ProductArea(models.Model):
    product_category = models.CharField(max_length = 100)
    def __str__(self):
        return self.product_category

class FeatureRequest(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 2000)
    client = models.ForeignKey(Client)
    client_priority = models.IntegerField()
    target_date = models.DateField()
    ticket_url = models.CharField(max_length = 100)
    product_area = models.ForeignKey(ProductArea)

    def correctClientPriorities(self):
        if FeatureRequest.objects.filter(client_priority = self.client_priority, client_id = self.client).exists():
            requestList = FeatureRequest.objects.filter(client_priority__gte = self.client_priority, client_id = self.client)
            for request in requestList:
                request.client_priority += 1
                request.save()
        print("finished!")
