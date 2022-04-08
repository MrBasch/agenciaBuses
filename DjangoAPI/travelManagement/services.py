from .models import Bus, City, Route, Station, Driver
from .constants import DRIVER_CHOICES, ROUTE_CHOICES, BUS_CHOICES
from django.core.exceptions import ObjectDoesNotExist

# ------------------------------CITIES---------------------------------


def get_all_cities():
    return City.objects.all()


def get_or_create_city(name, code):
    return City.objects.get_or_create(name=name, code=code)


def upload_or_create_city(code, name, new_code):
    return City.objects.update_or_create(
        code=code, defaults={"name": name, "code": new_code}
    )


def get_city_with_code(code):
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


def upload_or_create_station(code, name, new_code, city_id):
    city_instance = City.objects.get(id=city_id)
    return Station.objects.update_or_create(
        code=code, defaults={"name": name, "code": new_code, "city": city_instance}
    )


def get_station_with_code(code):
    return Station.objects.get(code=code)


def delete_station(station):
    station.delete()


def get_stations_with_list_code(station_list):
    print("station list = ", station_list)
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
    stations = get_stations_with_list_code(station_list)
    try:
        existe = get_route_by_code(code=code)
    except ObjectDoesNotExist:
        ruta, created = Route.objects.get_or_create(code=code, name=name, status=status)
        ruta.stops.set(stations)
        print("ruta", ruta)
    print("failed to add, the station already exist")

    #
    # print("created", created)
    # ruta.save()
    # ruta.stops.set(stations)
    # return ruta
    # return Station.objects.get_or_create(name=name, code=code, city=city_instance)


# def crear_ruta(name, code, station_list, status):
#     stops=[1,2,3]
#     paradas= Station.objects.filter(id__in=station_list)
#     Route.objects.create(name=name, code=code, status=status, stops=paradas)
# ------------------------------ ROUTES ---------------------------------

# ------------------------------ Bus ---------------------------------


def get_all_buses():
    return Bus.objects.all()


def get_or_create_bus(code, status):
    return Bus.objects.get_or_create(code=code, status=status)


def upload_or_create_bus(code, status, new_code):
    return Bus.objects.update_or_create(
        code=code, defaults={"status": status, "code": new_code}
    )


def get_bus_with_code(code):
    return Bus.objects.get(code=code)


def delete_bus(bus):
    bus.delete()


# ------------------------------ Bus ---------------------------------

# ------------------------------ Driver ---------------------------------
def get_all_drivers():
    return Driver.objects.all()


def get_or_create_driver(name, status, rut):
    return Driver.objects.get_or_create(name=name, status=status, rut=rut)


def upload_or_create_driver(name, status, rut, new_rut):
    return Driver.objects.update_or_create(
        rut=rut, defaults={"status": status, "rut": new_rut, "name": name}
    )


def get_driver_with_rut(rut):
    return Driver.objects.get(rut=rut)


def delete_driver(driver):
    driver.delete()


# ------------------------------ Driver ---------------------------------
