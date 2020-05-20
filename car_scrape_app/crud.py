from sqlalchemy.orm import Session

from car_scrape_app import models


def create_car(a_car, db: Session):
    db_car = models.Car(
        url=a_car.url,
        model=a_car.model,
        make=a_car.make,
        price=a_car.price,
        year=a_car.year,
        passenger_doors=a_car.passenger_doors,
        passenger_capacity=a_car.passenger_capacity,
        transmission=a_car.transmission,
        drive_type=a_car.drive_type,
        zero_60_mph=a_car.zero_60_mph,
        epa_mileage_combined=a_car.epa_mileage_combined,
        horsepower=a_car.horsepower,
        torque=a_car.torque,
        cylinders=a_car.cylinders,
        base_engine_size=a_car.base_engine_size,
        engine_type=a_car.engine_type,
        front_suspension_type=a_car.front_suspension_type,
        rear_suspension_type=a_car.rear_suspension_type,
        front_brakes=a_car.front_brakes,
        rear_brakes=a_car.rear_brakes,
        brake_type=a_car.brake_type,
        abs_brakes_type=a_car.abs_brakes_type,
        curb_weight=a_car.curb_weight,
        fuel_tank_capacity=a_car.fuel_tank_capacity,
        dead_weight_hitch___max_tongue_weight=a_car.dead_weight_hitch___max_tongue_weight,
        dead_weight_hitch___max_trailer_weight=a_car.dead_weight_hitch___max_trailer_weight,
        max_trailering_capacity=a_car.max_trailering_capacity,
        weight_distributing_hitch___max_tongue_weight=a_car.weight_distributing_hitch___max_tongue_weight,
        weight_distributing_hitch___max_trailer_weight=a_car.weight_distributing_hitch___max_trailer_weight,
        length=a_car.length,
        width=a_car.width,
        height=a_car.height,
        wheelbase=a_car.wheelbase,
        ground_clearance=a_car.ground_clearance,
        turning_circle=a_car.turning_circle,
        front_head_room=a_car.front_head_room,
        front_leg_room=a_car.front_leg_room,
        front_shoulder_room=a_car.front_shoulder_room,
        front_hip_room=a_car.front_hip_room,
        rear_head_room=a_car.rear_head_room,
        rear_leg_room=a_car.rear_leg_room,
        rear_shoulder_room=a_car.rear_shoulder_room,
        rear_hip_room=a_car.rear_hip_room,
        third_row_head_room=a_car.third_row_head_room,
        third_row_leg_room=a_car.third_row_leg_room,
        third_row_shoulder_room=a_car.third_row_shoulder_room,
        third_row_hip_room=a_car.third_row_hip_room
        )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car
