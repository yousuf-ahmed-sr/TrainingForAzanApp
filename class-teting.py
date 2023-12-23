import time

class CarType:
    def __init__(self, speed, battery):
        self.speed = speed
        self.battery = battery

player_choice = input('What car do you want? Options (blue, red): ')

if player_choice == 'blue':
    car_type = CarType(speed=1, battery=5)
elif player_choice == 'red':
    car_type = CarType(speed=2, battery=8)
else:
    print("Invalid choice. Please select 'blue' or 'red'")
    exit()

distance = car_type.speed * car_type.battery
print('driving...')
time.sleep(distance / car_type.speed)
print(f"You went {distance}m")
