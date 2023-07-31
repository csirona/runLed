class LEDTimeSimulation:
    @staticmethod
    def calculate_total_distance(distance, number_of_leds):
        return distance

    @staticmethod
    def calculate_speed(total_distance, seconds):
        return total_distance / seconds

    @staticmethod
    def calculate_time_per_led(seconds, number_of_leds):
        return seconds / number_of_leds

    @staticmethod
    def calculate_speed_kmph(speed_mps):
        return speed_mps * 3.6

    @staticmethod
    def calculate_single_led_distance(distance_meters, number_of_leds):
        return distance_meters / number_of_leds

    @staticmethod
    def led_number_at_distance(distance, distance_per_led):
        # Calculate the LED number based on the given distance and distance_per_led
        led_number = distance // distance_per_led
        return led_number + 1  # Adding 1 to convert to 1-based indexing (LEDs are typically indexed from 1)
