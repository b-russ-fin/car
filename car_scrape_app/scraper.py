import requests
from bs4 import BeautifulSoup
from car_scrape_app import car

class Car:
    def __init__(self, make, model, year, price, *args, **kwargs):
        self.model = model
        self.make = make
        self.price = price
        self.year = year
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
    car_price = results.find('span', title='Based on average nation-wide prices').text
    # car_stats.update({'price': car_price.text})
    car_elems = results.find_all('div', class_='pure-u-1 pure-u-md-1-2')

    for car_elem in car_elems:
        if car_elem.h4 is not None:
            car_stats.update({car_elem.h4.text: car_elem.br.previousSibling.strip()})

    print(car_stats)
    a_car = Car(make, model, year, car_price, **car_stats)
    print(a_car.__dict__)
    # print(a_car.features())
