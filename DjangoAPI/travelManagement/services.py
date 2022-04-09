from xml.dom import ValidationErr

from django.forms import ValidationError
from .models import Bus, City, Route, Station, Driver, Travel
from .constants import DRIVER_STATUSES, DRIVER_STATUSES, BUS_STATUSES, ROUTE_STATUSES
from django.core.exceptions import ObjectDoesNotExist

# ------------------------------CITIES---------------------------------


def get_all_cities():
    return City.objects.all()


def get_or_create_city(name, code):
    return City.objects.get_or_create(name=name, code=code)


def update_or_create_city(code, name, new_code):
    return City.objects.update_or_create(
        code=code, defaults={"name": name, "code": new_code}
    )


def get_city_by_code(code):
    return City.objects.get(code=code)


def create_city(city):
    city.save()


def delete_city(city):
    city.delete()


# ------------------------------CITIES---------------------------------

# ------------------------------STATION---------------------------------


def get_all_stations():
    return Station.objects.all()


def get_or_create_station(name, code, city_id):
    city_instance = City.objects.get(id=city_id)
    return Station.objects.get_or_create(name=name, code=code, city=city_instance)


def update_or_create_station(code, name, new_code, city_id):
    city_instance = City.objects.get(id=city_id)
    return Station.objects.update_or_create(
        code=code, defaults={"name": name, "code": new_code, "city": city_instance}
    )


def get_station_by_code(code):
    return Station.objects.get(code=code)


def delete_station(station):
    station.delete()


def get_stations_by_list_code(station_list):
    return list(Station.objects.filter(id__in=station_list))


# ------------------------------STATION---------------------------------

# ------------------------------ ROUTES ---------------------------------


def get_all_routes():
    return Route.objects.all()


def delete_route(route):
    route.delete()


def get_route_by_code(code):
    return Route.objects.get(code=code)


def get_or_create_route(name, code, station_list, status):
    # if(status not in ROUTE_STATUSES):
    # raise ValidationError
    stations = get_stations_by_list_code(station_list)
    # if not stations:

    route, created = Route.objects.get_or_create(
        code=code, defaults={"name": name, "status": status}
    )
    if created:
        route.stops.add(*stations)
        route.save()
    return route, created


def update_or_create_route(name, code, station_list, status, new_code):
    stations = get_stations_by_list_code(station_list)
    route, created = Route.objects.update_or_create(
        code=code, defaults={"name": name, "status": status, "code": new_code}
    )
    if created:
        route.stops.add(*stations)
        route.save()
    return route, created


# ------------------------------ ROUTES ---------------------------------

# ------------------------------ Bus ---------------------------------


def get_all_buses():
    return Bus.objects.all()


def get_or_create_bus(code, status):
    return Bus.objects.get_or_create(code=code, status=status)


def update_or_create_bus(code, status, new_code):
    return Bus.objects.update_or_create(
        code=code, defaults={"status": status, "code": new_code}
    )


def get_bus_by_code(code):
    return Bus.objects.get(code=code)


def delete_bus(bus):
    bus.delete()


# ------------------------------ Bus ---------------------------------

# ------------------------------ Driver ---------------------------------
def get_all_drivers():
    return Driver.objects.all()


def get_or_create_driver(name, status, rut):
    return Driver.objects.get_or_create(name=name, status=status, rut=rut)


def update_or_create_driver(name, status, rut, new_rut):
    return Driver.objects.update_or_create(
        rut=rut, defaults={"status": status, "rut": new_rut, "name": name}
    )


def get_driver_by_rut(rut):
    return Driver.objects.get(rut=rut)


def get_driver_by_id(id):
    return Driver.objects.get(id=id)


def delete_driver(driver):
    driver.delete()


# ------------------------------ Driver ---------------------------------


# ------------------------------ Travel ---------------------------------
def get_all_travels():
    return Travel.objects.all()


def get_or_create_travel(code, code_route, id_driver, code_bus, start_time, end_time):
    # if(status not in ROUTE_STATUSES):
    # raise ValidationError
    # stations = get_stations_by_list_code(station_list)
    # if not stations:
    print("start time")

    driver = get_driver_by_id(id_driver)
    bus = get_bus_by_code(code_bus)
    route = get_route_by_code(code_route)
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
        route.save()
    return travel, created


def update_or_create_travel(
    code, new_code, code_route, id_driver, code_bus, start_time, end_time
):
    # if(status not in ROUTE_STATUSES):
    # raise ValidationError
    # stations = get_stations_by_list_code(station_list)
    # if not stations or not code or n:
    print("start time")

    driver = get_driver_by_id(id_driver)
    bus = get_bus_by_code(code_bus)
    route = get_route_by_code(code_route)
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
        route.save()
    return travel, created


def get_travel_by_code(code):
    return Travel.objects.get(code=code)


def delete_travel(travel):
    travel.delete()


# ------------------------------ Travel ---------------------------------
