from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.forms import ValidationError
from isort import code

from .constants import BUS_STATUSES, DRIVER_STATUSES, ROUTE_STATUSES
from .models import Bus, City, Driver, Passenger, Place, Route, Station, Travel
from rest_framework.authtoken.models import Token

# promedio de pasajeros por trayecto
def average_passangers_for_route(route_code):
    # route = get_route_by_code(code=route_code)
    # select all travels where route.id=id_route filter
    total_used_places = (
        Place.objects.select_related("travel__route")
        .get(code=route_code)
        .filter(available=False)
        .count()
    )
    num_of_travels = Travel.objects.get(route__code=route_code).count()
    print("total", total_used_places)
    print("number of travels = ", num_of_travels)
    return total_used_places / num_of_travels


# Filtrar a todos los buses de un trayecto con más del N % de su capacidad vendida.
def selling_buses_by_route(route_code: str, N: int):
    buses = Bus.objects.get(__route__code=route_code).filter(
        Count(____available=False) >= N
    )
    print("buese =", buses)

    # Filtrar viajes por destino


def travels_by_station(id_station):
    travels = Travel.objects.get(route__stops__id=id_station).filter(
        status="active"
    )  # añadir status al modelo


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| CRUD |||||||||||||||||||||||||||||||||||||||||||||||||||||||||


def create_token(user):
    return Token.objects.create(user=user)


# ------------------------------CITIES---------------------------------


def get_all_cities():
    return City.objects.all()


def get_or_create_city(name: str, code: str):
    if not code or not name:
        raise ValidationError
    city, created = City.objects.get_or_create(name=name, code=code)
    if created:
        city.save()
    return city, created


def update_or_create_city(code: str, name: str, new_code: str):
    if not code or not name:
        raise ValidationError("Invalid data")
    if not new_code:
        new_code = code
    return City.objects.update_or_create(
        code=code, defaults={"name": name, "code": new_code}
    )


def get_city_by_code(code):
    if not code:
        raise ValidationError("Invalid data")
    return City.objects.get(code=code)


def create_city(city):
    if not city:
        raise ValidationError("Invalid data")
    city.save()


def delete_city(city):
    if not city:
        raise ValidationError("Invalid data")
    city.delete()


# ------------------------------CITIES---------------------------------

# ------------------------------STATION---------------------------------


def get_all_stations():
    return Station.objects.all()


def get_or_create_station(name, code, city_id):
    city_instance = City.objects.get(id=city_id)
    if not code or not name or not city_instance:
        raise ValidationError
    station, created = Station.objects.get_or_create(
        name=name, code=code, city=city_instance
    )
    if created:
        station.save()
    return station, created


def update_or_create_station(code, name, new_code, city_id):
    city_instance = City.objects.get(id=city_id)
    if not code or not name or not city_instance:
        raise ValidationError("Invalid data")
    if not new_code:
        new_code = code
    return Station.objects.update_or_create(
        code=code, defaults={"name": name, "code": new_code, "city": city_instance}
    )


def get_station_by_code(code):
    if not code:
        raise ValidationError("Invalid data")
    return Station.objects.get(code=code)


def delete_station(station):
    if not station:
        raise ValidationError("Invalid data")
    station.delete()


def create_station(station):
    if not station:
        raise ValidationError("Invalid data")
    station.save()


def get_stations_by_list_code(station_list):
    if not station_list:
        raise ValidationError("Invalid data")
    return list(Station.objects.filter(id__in=station_list))


# ------------------------------STATION---------------------------------

# ------------------------------ ROUTES ---------------------------------


def get_all_routes():
    return Route.objects.all()


def delete_route(route):
    if not route:
        raise ValidationError("Invalid data")
    route.delete()


def get_route_by_code(code):
    if not code:
        raise ValidationError("invalid value of code")
    return Route.objects.get(code=code)


def get_or_create_route(name, code, station_list, status):
    stations = get_stations_by_list_code(station_list)
    if status not in ROUTE_STATUSES or not code or not name or not stations:
        raise ValidationError("Invalid data")

    route, created = Route.objects.get_or_create(
        code=code, defaults={"name": name, "status": status}
    )
    if created:
        route.stops.add(*stations)
        route.save()
    return route, created


def update_or_create_route(name, code, station_list, status, new_code):
    stations = get_stations_by_list_code(station_list)
    if status not in ROUTE_STATUSES or not code or not name or not stations:
        raise ValidationError("Invalid data")
    if not new_code:
        new_code = code
    route, created = Route.objects.update_or_create(
        code=code, defaults={"name": name, "status": status, "code": new_code}
    )
    if created:
        route.stops.add(*stations)
        route.save()
    return route, created


def create_route(route):
    if not route:
        raise ValidationError("Invalid data")
    route.save()


# ------------------------------ ROUTES ---------------------------------

# ------------------------------ Bus ---------------------------------


def get_all_buses():
    return Bus.objects.all()


def get_or_create_bus(code, status):
    if status not in BUS_STATUSES or not code:
        raise ValidationError
    bus, created = Bus.objects.get_or_create(code=code, status=status)
    if created:
        bus.save()
    return bus, created


def update_or_create_bus(code, status, new_code):
    if status not in BUS_STATUSES or not code:
        raise ValidationError("Invalid data")
    if not new_code:
        new_code = code
    return Bus.objects.update_or_create(
        code=code, defaults={"status": status, "code": new_code}
    )


def get_bus_by_code(code):
    if not code:
        raise ValidationError("Invalid data")
    return Bus.objects.get(code=code)


def delete_bus(bus):
    if not bus:
        raise ValidationError("Invalid data")
    bus.delete()


def create_bus(bus):
    if not bus:
        raise ValidationError("Invalid data")
    bus.save()


# ------------------------------ Bus ---------------------------------

# ------------------------------ Driver ---------------------------------
def get_all_drivers():
    return Driver.objects.all()


def get_or_create_driver(name, status, rut):
    if status not in DRIVER_STATUSES or not name or not rut:
        raise ValidationError("Invalid data")
    return Driver.objects.get_or_create(name=name, status=status, rut=rut)


def update_or_create_driver(name, status, rut, new_rut):
    if status not in DRIVER_STATUSES or not name or not rut:
        raise ValidationError("Invalid data")
    if not new_rut:
        new_rut = rut
    return Driver.objects.update_or_create(
        rut=rut, defaults={"status": status, "rut": new_rut, "name": name}
    )


def get_driver_by_rut(rut):
    if not rut:
        raise ValidationError("Invalid data")
    return Driver.objects.get(rut=rut)


def get_driver_by_id(id):
    if not id:
        raise ValidationError("Invalid data")
    return Driver.objects.get(id=id)


def delete_driver(driver):
    if not driver:
        raise ValidationError("Invalid data")
    driver.delete()


def create_driver(driver):
    if not driver:
        raise ValidationError("Invalid data")
    driver.save()


# ------------------------------ Driver ---------------------------------


# ------------------------------ Travel ---------------------------------
def get_all_travels():
    return Travel.objects.all()


def get_or_create_travel(code, code_route, id_driver, code_bus, start_time, end_time):
    driver = get_driver_by_id(id_driver)
    bus = get_bus_by_code(code_bus)
    route = get_route_by_code(code_route)
    if not code or not driver or not bus or not route or not start_time or not end_time:
        raise ValidationError("Invalid data")
    travel, created = Travel.objects.get_or_create(
        code=code,
        defaults={
            "bus": bus,
            "driver": driver,
            "route": route,
            "start_time": start_time,
            "end_time": end_time,
        },
    )
    if created:
        travel.save()
    return travel, created


def update_or_create_travel(
    code, new_code, code_route, id_driver, code_bus, start_time, end_time
):
    driver = get_driver_by_id(id_driver)
    bus = get_bus_by_code(code_bus)
    route = get_route_by_code(code_route)
    if not code or not driver or not bus or not route or not start_time or not end_time:
        raise ValidationError("Invalid data")
    if not new_code:
        new_code = code
    travel, created = Travel.objects.get_or_create(
        code=code,
        defaults={
            "bus": bus,
            "code": new_code,
            "driver": driver,
            "route": route,
            "start_time": start_time,
            "end_time": end_time,
        },
    )
    if created:
        travel.save()
    return travel, created


def get_travel_by_code(code):
    if not code:
        raise ValidationError("Invalid data")
    return Travel.objects.get(code=code)


def delete_travel(travel):
    if not travel:
        raise ValidationError("Invalid data")
    travel.delete()


def create_travel(travel):
    travel.save()


# ------------------------------ Travel ---------------------------------


# ------------------------------ Place ---------------------------------
def get_all_places():
    return Place.objects.all()


def get_place_by_code(code):
    if not code:
        raise ValidationError("Invalid data")
    return Place.objects.get(code=code)


def delete_place(place):
    if not place:
        raise ValidationError("Invalid data")
    place.delete()


def create_place(place):
    if not place:
        raise ValidationError("Invalid data")
    place.save()


def get_or_create_place(code, available, code_travel):
    travel = get_travel_by_code(code_travel)
    if not code or not travel:
        raise ValidationError("Invalid data")
    place, created = Place.objects.get_or_create(
        code=code, defaults={"travel": travel, "available": available}
    )
    if created:
        place.save()
    return place, created


def update_or_create_place(code, available, code_travel, new_code):
    travel = get_travel_by_code(code_travel)
    if not code or not travel:
        raise ValidationError("Invalid data")
    if not new_code:
        new_code = code

    place, created = Place.objects.get_or_create(
        code=code,
        defaults={"travel": travel, "available": available, "new_code": new_code},
    )
    if created:
        place.save()
    return place, created


# ------------------------------ Place ---------------------------------


# ------------------------------ Passenger ---------------------------------
def get_all_passenger():
    return Passenger.objects.all()


def get_passenger_by_id(id):
    if not id:
        raise ValidationError("Invalid data")
    return Passenger.objects.get(id=id)


def get_or_create_passenger(place_code, name, rut):
    place = get_place_by_code(place_code)
    if not rut or not name or not place:
        raise ValidationError("Invalid data")
    passenger, created = Passenger.objects.get_or_create(
        rut=rut, defaults={"name": name, "place": place}
    )
    if created:
        passenger.save()
    return passenger, created


def update_or_create_passenger(place_code, name, rut, new_rut):
    place = get_place_by_code(place_code)
    if not rut or not name or not place:
        raise ValidationError("Invalid data")
    if not new_rut:
        new_rut = rut
    passenger, created = Passenger.objects.get_or_create(
        rut=rut, defaults={"name": name, "place": place, "rut": new_rut}
    )
    if created:
        passenger.save()
    return passenger, created


def delete_passanger(passenger):
    if not passenger:
        raise ValidationError("Invalid data")
    passenger.delete()


# ------------------------------ Passenger ---------------------------------
