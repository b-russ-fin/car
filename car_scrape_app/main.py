from car_scrape_app import car, scraper, models, crud
from car_scrape_app.database import SessionLocal, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def create_car(a_car, db: Session = SessionLocal()):
    return crud.create_car(a_car, db=db)

for URL in car.url_list:
    create_car(scraper.car_scrape(URL))
