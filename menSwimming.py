# Import the LEDTimeSimulation class
from led_simulation import LEDTimeSimulation

# Given values for men's swimming
seconds = 51.71
distance_meters = 100
number_of_leds = 6000

# Calculate the total distance in meters (distance traveled by a single LED)
total_distance_meters = LEDTimeSimulation.calculate_total_distance(distance_meters, number_of_leds)

# Calculate the speed in meters per second
speed_mps = LEDTimeSimulation.calculate_speed(total_distance_meters, seconds)

# Calculate the time taken per LED in seconds
time_per_led_seconds = LEDTimeSimulation.calculate_time_per_led(seconds, number_of_leds)

# Calculate the speed in kilometers per hour
speed_kmph = LEDTimeSimulation.calculate_speed_kmph(speed_mps)

print("Speed (m/s):", speed_mps)
print("Speed (km/h):", speed_kmph)
print("Time per LED (seconds):", time_per_led_seconds)
print("total led time: "+str(time_per_led_seconds*6000))
