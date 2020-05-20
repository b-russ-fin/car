import requests
from bs4 import BeautifulSoup
from car_scrape_app import car

class Car:
    def __init__(self, url, make, model, year, price, *args, **kwargs):
        self.url = url
        self.model = model
        self.make = make
        self.price = price
        self.year = year
        self.passenger_doors = ''
        self.passenger_capacity = ''
        self.transmission = ''
        self.drive_type = ''
        self.zero_60_mph = ''
        self.epa_mileage_combined = ''
        self.horsepower = ''
        self.torque = ''
        self.cylinders = ''
        self.base_engine_size = ''
        self.engine_type = ''
        self.front_suspension_type = ''
        self.rear_suspension_type = ''
        self.front_brakes = ''
        self.rear_brakes = ''
        self.brake_type = ''
        self.abs_brakes_type = ''
        self.curb_weight = ''
        self.fuel_tank_capacity = ''
        self.dead_weight_hitch___max_tongue_weight = ''
        self.dead_weight_hitch___max_trailer_weight = ''
        self.max_trailering_capacity = ''
        self.weight_distributing_hitch___max_tongue_weight = ''
        self.weight_distributing_hitch___max_trailer_weight = ''
        self.length = ''
        self.width = ''
        self.height = ''
        self.wheelbase = ''
        self.ground_clearance = ''
        self.turning_circle = ''
        self.front_head_room = ''
        self.front_leg_room = ''
        self.front_shoulder_room = ''
        self.front_hip_room = ''
        self.rear_head_room = ''
        self.rear_leg_room = ''
        self.rear_shoulder_room = ''
        self.rear_hip_room = ''
        self.third_row_head_room = ''
        self.third_row_leg_room = ''
        self.third_row_shoulder_room = ''
        self.third_row_hip_room = ''
        self.__dict__.update(kwargs)

    def features(self):
        return self.model, self.make, self.price, self.year, (key, value in kwargs.items())




def car_scrape(car_url):
    r = requests.get(car_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    results = soup.find(id='layout')

    make = car_url[(car_url.find('/2017/') + 6):(car_url.find('/', (car_url.find('/2017/') + 6)))]
    model = car_url[(car_url.find(make) + len(make) + 1):(car_url.find('/', (car_url.find(make) + len(make) + 1)))]
    year = 2017
    car_stats = {}
    car_price = results.find('span', title='Based on average nation-wide prices')
    if car_price is not None:
        car_price = car_price.text.replace('$','').replace(',','')
    # car_stats.update({'price': car_price.text})
    car_elems = results.find_all('div', class_='pure-u-1 pure-u-md-1-2')

    for car_elem in car_elems:
        if car_elem.h4 is not None:
            car_stats.update({car_elem.h4.text.lower().replace('(','').replace(')','').replace('3rd', 'third').replace('0-60', 'zero-60').replace('-','_').replace(' ', '_'): car_elem.br.previousSibling.strip()})

    print(car_stats)
    a_car = Car(car_url, make, model, year, car_price, **car_stats)
    print(a_car.__dict__)
    return a_car
    # print(a_car.features())
