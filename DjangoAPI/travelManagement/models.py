from django.db import models

from .constants import BUS_CHOICES, DRIVER_CHOICES, ROUTE_CHOICES

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} - {self.code}"


class Station(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Route(models.Model):
    code = models.CharField(max_length=50, unique=True)
    stops = models.ManyToManyField(Station)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=ROUTE_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.code} - {self.stops.all()} - {self.status}"

    def get_stops_name(self):
        stops = list(self.stops.all().values_list("name", flat=True))
        return " - ".join(name for name in stops)


class Bus(models.Model):
    code = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=50, choices=BUS_CHOICES)

    def __str__(self):
        return f"{self.code} - {self.status}"


class Driver(models.Model):
    name = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, blank=False, unique=True)
    status = models.CharField(max_length=50, choices=DRIVER_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.rut} - {self.status}"


class Travel(models.Model):
    code = models.CharField(max_length=50, unique=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.route} - {self.bus} - {self.driver} - {self.start_time}"


class Place(models.Model):
    travel_id = models.ForeignKey(Travel, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, blank=False, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.travel_id} - {self.code} - {self.available}"


class Passenger(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, blank=False, unique=True)

    def __str__(self):
        return f"{self.place_id} - {self.name} - {self.rut}"
