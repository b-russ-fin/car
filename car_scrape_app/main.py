from car_scrape_app import car, scraper

for URL in car.url_list:
    scraper.car_scrape(URL)
