from vehicle import vehicle

if __name__ == "__main__":
   
    #create an instace of the Vehicle class
    black_car = vehicle("Tesla", "Model 3", 2018)
    red_car = vehicle("Toyota", "Camry", 2023 )

all_vehicles = vehicle.get_all_vehicles()
for vehicles in all_vehicles:
    print(vehicle)
