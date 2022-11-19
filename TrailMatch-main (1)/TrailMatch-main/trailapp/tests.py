from django.test import TestCase
from trailapp.models import Trail

# Create your tests here.
def create_trail(name,diff,distance):
    return Trail.objects.create(trail_name=name,difficulty=diff,trail_length=distance)
