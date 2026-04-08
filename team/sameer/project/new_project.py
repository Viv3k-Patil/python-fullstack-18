class Bike:
    def __init__(self,bike_name,bike_engine,bike_price,bike_speed,bike_milege):
        self.bike_name=bike_name
        self.bike_engine=bike_engine
        self.bike_price=bike_price
        self.bike_speed=bike_speed
        self.bike_milege=bike_milege

    def __str__(self):
        return f"bike_name :{self.bike_name},\nbike_engine :{self.bike_engine},\nbike_price :{self.bike_price}"
    
    def greet ():
        print("hii")

print(Bike.greet())