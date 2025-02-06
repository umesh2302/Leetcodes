# https://www.codewars.com/kata/670fd4615f6c253786cd49a2/train/python#
def calculate_trips(distances, speeds):
    # Your code here
    taxi_dict ={}
    taxi_trip = {}
    
    for i in range(len(speeds)):
        taxi_dict[i] = speeds[i]
        taxi_trip[i] = 0
    allocate_taxi ={}
    
def get_max_speed_taxi(taxi_dict):
    max_speed_taxi = max(taxi_dict, key=taxi_dict.get)
    return max_speed_taxi, taxi_dict[max_speed_taxi]

def allocate_trip(taxi_trip, taxi_dict, distance, allocated_taxi, start_time):
    max_speed_taxi, max_speed = get_max_speed_taxi(taxi_dict)
    trip_time = distance / max_speed
    taxi_trip[max_speed_taxi] += 1
    # shift this taxi to allocated taxi with return time and remove from taxi_dict
    allocated_taxi[max_speed_taxi] = [start_time + trip_time, taxi_dict[max_speed_taxi]]
    del taxi_dict[max_speed_taxi]
    return taxi_trip, taxi_dict,allocated_taxi


def taxi_available(distances, speeds, start_time):
    
    result = []
    return result


calculate_trips([10, 20, 30], [1, 20, 3]) # {0: 1, 1: 2, 2: 3}


