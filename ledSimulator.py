import time
from led_simulation import LEDTimeSimulation

def simulate_neo_pixels():
    # Example usage
    seconds = int(input('time: '))
    distance_meters_pool = float(input('meters swimming pool: '))
    distance_meters = float(input('meters: '))
    n_of_led_per_meter = int(input('n leds per meter: '))

    number_of_leds_total = int(n_of_led_per_meter * distance_meters) 
    number_of_leds_pool = n_of_led_per_meter * distance_meters_pool

    # Calculate the total distance in meters (distance traveled by a single LED)
    total_distance_meters = LEDTimeSimulation.calculate_total_distance(distance_meters, number_of_leds_total)

    # Calculate the speed in meters per second
    speed_mps = LEDTimeSimulation.calculate_speed(total_distance_meters, seconds)

    # Calculate the time taken per LED in seconds
    time_per_led_seconds = LEDTimeSimulation.calculate_time_per_led(seconds, number_of_leds_total)

    # Calculate the speed in kilometers per hour
    speed_kmph = LEDTimeSimulation.calculate_speed_kmph(speed_mps)

    # Calculate the distance traveled by a single LED in meters
    distance_per_led = LEDTimeSimulation.calculate_single_led_distance(distance_meters, number_of_leds_total)

    print("Speed (m/s):", speed_mps)
    print("Speed (km/h):", speed_kmph)
    print("Time per LED (seconds):", time_per_led_seconds)
    print("distance per led: ", distance_per_led)
    print('n total leds'+str(number_of_leds_total))

    distance_change_color_1 = float(input('Distance (in meters) for first color change: '))
    distance_change_color_2 = float(input('Distance (in meters) for second color change: '))
    distance_change_color_3 = float(input('Distance (in meters) for third color change: '))

    # Calculate LED numbers for color change distances
    color_change_led_1 = round(LEDTimeSimulation.led_number_at_distance(distance_change_color_1, distance_per_led))
    color_change_led_2 = round(LEDTimeSimulation.led_number_at_distance(distance_change_color_2, distance_per_led))
    color_change_led_3 = round(LEDTimeSimulation.led_number_at_distance(distance_change_color_3, distance_per_led))
    direction_change_led = round(LEDTimeSimulation.led_number_at_distance(distance_meters_pool, distance_per_led))

    print(color_change_led_1)
    print(color_change_led_2)
    print(color_change_led_3)
    print('change direction: ' + str(direction_change_led))

        # Calculate the LED number at which the intermittent effect should end
    intermittent_end_to_led = round(number_of_leds_total - color_change_led_3) // 2
    intermittent_end_led = round(number_of_leds_total - intermittent_end_to_led)
    print('intermittent end: ' + str(intermittent_end_led))

    # Calculate the LED number at which the intermittent effect should start
    intermittent_start_led = round((color_change_led_3 + number_of_leds_total) / 2)

    def print_led_status(distance_traveled, distance_change_leds, last_led, loop_number):
        count = int(distance_traveled) + 1

        if loop_number % 3 == 1:
            last_led = 'R'
            print(f"LED {count}: R*")
        elif loop_number % 3 == 2:
            last_led = 'G'
            print(f"LED {count}: G*")
        elif loop_number % 3 == 0:
            last_led = 'B'
            print(f"LED {count}: B*")
        else:
            if distance_traveled >= intermittent_start_led and distance_traveled <= intermittent_end_led and last_led == 'Y':
                last_led = 'Off'
                print(f"LED {count}: Y*")
            else:
                if count > number_of_leds_total - n_of_led_per_meter:
                    last_led = 'Y'
                    print(f"LED {count}: Off")
                else:
                    last_led = 'Y'
                    print(f"LED {count}: Y *")
        return last_led

    def calculate_loop_number(distance_traveled):
        loop_number = (distance_traveled // number_of_leds_pool) + 1  # Increment by 1 to start loop number from 1
        return loop_number

    last_led = ''
    loop_number = 0  # Initialize the loop number
    start_time = time.time()

    # Initialize decrease_counter outside the loop
    decrease_counter = number_of_leds_pool

    # Simulate NeoPixel LEDs
    for i in range(int(number_of_leds_total)):
        distance_traveled = i

        loop_number = calculate_loop_number(distance_traveled)

        if loop_number == 1:
            # First loop, moving forward
            last_led = print_led_status(distance_traveled, [color_change_led_1, color_change_led_2, color_change_led_3], last_led, loop_number)
        else:
            # Calculate the adjusted distance for even loops to start from LED 1
            starting_led = (loop_number - 1) * number_of_leds_pool + 1
            adjusted_distance_traveled = distance_traveled - starting_led

            if adjusted_distance_traveled < 0:
                adjusted_distance_traveled = 0

            if loop_number % 2 == 0:
                # Even loop, LED count decreases
                decrease_counter -= 1
                adjusted_distance_traveled = number_of_leds_pool - (distance_traveled % number_of_leds_pool) - 1

            last_led = print_led_status(adjusted_distance_traveled, [color_change_led_1, color_change_led_2, color_change_led_3], last_led, loop_number)

            # Handle the last LED of each loop
            if distance_traveled % number_of_leds_pool == number_of_leds_pool - 1:
                if loop_number % 2 == 0:
                    # Even loop, print the loop number and LED count
                    print(f"Loop {loop_number} - LED {distance_traveled}")
                else:
                    # Odd loop, print the next loop number and LED count
                    next_loop_number = loop_number + 1
                    next_led = distance_traveled + 1
                    print(f"Loop {next_loop_number} - LED {next_led}")
                    last_led = ''

        time.sleep(time_per_led_seconds) 
    end_time = time.time()
    led_1_to_300_time = end_time - start_time
    print(f"Time for LED 1 to LED 300: {led_1_to_300_time:.3f} seconds")

if __name__ == "__main__":
    simulate_neo_pixels()
