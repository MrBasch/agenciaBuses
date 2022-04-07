from .models import City, Route, Station

# ------------------------------CITIES---------------------------------


def get_all_cities():
    return City.objects.all()


def get_or_create_city(name, code):
    return City.objects.get_or_create(name=name, code=code)


def upload_or_create_city(code, name, new_code):
    return City.objects.update_or_create(code=code, defaults={"name": name, "code": new_code})


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
    return Station.objects.update_or_create(code=code, defaults={"name": name, "code": new_code, "city": city_instance})


def get_station_with_code(code):
    return Station.objects.get(code=code)


def delete_station(station):
    station.delete()
# ------------------------------STATION---------------------------------

# ------------------------------ ROUTES ---------------------------------


def get_all_routes():
    return Route.objects.all()
# ------------------------------ ROUTES ---------------------------------
