import time
from led_simulation import LEDTimeSimulation

def simulate_neo_pixels():
    # Example usage
    seconds = int(input('time: '))
    distance_meters = float(input('meters: '))
    number_of_leds = int(input('n leds: '))
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

    distance_change_color_1 = float(input('Distance (in meters) for first color change: '))
    distance_change_color_2 = float(input('Distance (in meters) for second color change: '))
    distance_change_color_3 = float(input('Distance (in meters) for third color change: '))

    # Calculate LED numbers for color change distances
    color_change_led_1 = LEDTimeSimulation.led_number_at_distance(distance_change_color_1, total_distance_meters)
    color_change_led_2 = LEDTimeSimulation.led_number_at_distance(distance_change_color_2, total_distance_meters)
    color_change_led_3 = LEDTimeSimulation.led_number_at_distance(distance_change_color_3, total_distance_meters)

    start_time = time.time()

    # Calculate the LED number at which the intermittent effect should end
    intermittent_end_led = color_change_led_3 + number_of_leds // 2

    # Simulate NeoPixel LEDs
    for i in range(number_of_leds):
        distance_traveled = (i + 1) * total_distance_meters / number_of_leds

        if distance_traveled <= distance_change_color_1:
            print(f"LED {i + 1}: R*")  # Use "R" to represent red color for the first section of LEDs
        elif distance_traveled <= distance_change_color_2:
            print(f"LED {i + 1}: G*")  # Use "G" to represent green color for the second section of LEDs
        elif distance_traveled <= distance_change_color_3:
            print(f"LED {i + 1}: B*")  # Use "B" to represent blue color for the third section of LEDs
        else:
            if i + 1 <= intermittent_end_led:
                print(f"LED {i + 1}: Y*")  # Use "Y" to represent the intermittent color
            else:
                print(f"LED {i + 1}: Off")  # Turn off the LEDs after the intermittent effect

        time.sleep(time_per_led_seconds)  # Add a delay to simulate LED movement

    end_time = time.time()
    led_1_to_300_time = end_time - start_time
    print(f"Time for LED 1 to LED 300: {led_1_to_300_time:.3f} seconds")


if __name__ == "__main__":
    simulate_neo_pixels()
