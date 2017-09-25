from django.db import models


# Create your models here.
class Travel(object):
    def __init__(self, name, destination, stops):
        self.name = name
        self.destination = destination
        self.stops = stops


travels = [
    Travel('sweden', 'sweden', ['israel', 'ukrain', ' sweden'])
]
