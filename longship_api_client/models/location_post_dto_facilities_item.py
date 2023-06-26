from enum import Enum


class LocationPostDtoFacilitiesItem(str, Enum):
    AIRPORT = "AIRPORT"
    BIKE_SHARING = "BIKE_SHARING"
    BUS_STOP = "BUS_STOP"
    CAFE = "CAFE"
    CARPOOL_PARKING = "CARPOOL_PARKING"
    FUEL_STATION = "FUEL_STATION"
    HOTEL = "HOTEL"
    MALL = "MALL"
    METRO_STATION = "METRO_STATION"
    MUSEUM = "MUSEUM"
    NATURE = "NATURE"
    PARKING_LOT = "PARKING_LOT"
    RECREATION_AREA = "RECREATION_AREA"
    RESTAURANT = "RESTAURANT"
    SPORT = "SPORT"
    SUPERMARKET = "SUPERMARKET"
    TAXI_STAND = "TAXI_STAND"
    TRAIN_STATION = "TRAIN_STATION"
    TRAM_STOP = "TRAM_STOP"
    WIFI = "WIFI"

    def __str__(self) -> str:
        return str(self.value)
