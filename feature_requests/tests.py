from django.test import TestCase
from .models import FeatureRequest
from .models import Client
from .models import ProductArea
from .exceptions import ConcurrentModificationError

# Create your tests here.
class ConcurrencyTestCase(TestCase):
    def setUp(self):
        client = Client.objects.create(name="client")
        pa = ProductArea.objects.create(product_category="A")
        FeatureRequest.objects.create(title="title", description="test", client=client, client_priority=1, target_date='1990-01-01', ticket_url='www.yes.com', product_area=pa, version=0)

    def test_optimistic_concurrency_A(self):
        checkout1 = FeatureRequest.objects.get(title="title")
        checkout2 = FeatureRequest.objects.get(title="title")
        checkout1.save()
        try:
            checkout2.save()
            self.fail("checkout2 should not be saved")
        except ConcurrentModificationError:
            pass

    def test_optimistic_concurrency_B(self):
        checkout1 = FeatureRequest.objects.get(title="title")
        checkout2 = FeatureRequest.objects.get(title="title")
        checkout2.save()
        try:
            checkout1.save()
            self.fail("checkout1 should not be saved")
        except ConcurrentModificationError:
            pass
