from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .exceptions import ConcurrentModificationError

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
    description = models.TextField()
    client = models.ForeignKey(Client)
    client_priority = models.IntegerField(default = 1)
    target_date = models.DateField()
    ticket_url = models.CharField(max_length = 100)
    product_area = models.ForeignKey(ProductArea)
    version = models.IntegerField(default = 0)

    #FeatureRequest overrides Model.save() to ensure that client_priority is unique among
    #the same client. It increments all client priorities greater than the
    #one being saved if there exists a priority equal to the current one
    def correctClientPriorities(self):
        if FeatureRequest.objects.filter(client_priority = self.client_priority, client_id = self.client).exclude(pk = self.id).exists():
            requestList = FeatureRequest.objects.filter(client_priority__gte = self.client_priority, client_id = self.client).exclude(pk = self.id)
            for request in requestList:
                request.client_priority += 1
                request.save()


    #Version check for optimistic locking
    def getCurrentVersion(self):
        if FeatureRequest.objects.filter(pk = self.id).exists():
            version = FeatureRequest.objects.get(pk = self.id).version
            return version
        return 0

    #throw exception when version # has changed between checking out and checking in
    def save(self, *args, **kwargs):
        self.correctClientPriorities()
        if self.version != self.getCurrentVersion():
            raise ConcurrentModificationError('This feature request has been edited by another user. Please go back and open again.')
        self.version += 1
        super(FeatureRequest, self).save(*args, **kwargs)
