from led_simulation import LEDTimeSimulation


def main():
    # Example usage
    distance_meters = 100
    number_of_leds = 300

    # Calculate the total distance in meters (distance traveled by a single LED)
    distance_per_led = LEDTimeSimulation.calculate_single_led_distance(distance_meters, number_of_leds)

    # Create an instance of LEDTimeSimulation to access other methods
    simulator = LEDTimeSimulation()

    # Calculate the speed in meters per second
    speed_mps = simulator.calculate_speed(distance_meters, seconds=10)

    # Calculate the time taken per LED in seconds
    time_per_led_seconds = simulator.calculate_time_per_led(seconds=10, number_of_leds=number_of_leds)

    # Calculate the LED number at certain distances
    distance_to_check_1 = 10
    distance_to_check_2 = 50
    distance_to_check_3 = 100

    led_number_1 = simulator.led_number_at_distance(distance_to_check_1, distance_per_led)
    led_number_2 = simulator.led_number_at_distance(distance_to_check_2, distance_per_led)
    led_number_3 = simulator.led_number_at_distance(distance_to_check_3, distance_per_led)

    print(f"LED number at {distance_to_check_1} meters: {led_number_1}")
    print(f"LED number at {distance_to_check_2} meters: {led_number_2}")
    print(f"LED number at {distance_to_check_3} meters: {led_number_3}")

if __name__ == "__main__":
    main()
