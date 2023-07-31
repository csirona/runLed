import time
import math
from led_simulation import LEDTimeSimulation

def simulate_neo_pixels():
    # Example usage
    seconds = int(input('time: '))
    distance_meters_pool = float(input('meters swimming pool: '))
    distance_meters = float(input('meters: '))
    n_of_led_per_meter = int(input('n leds per meter: '))

    number_of_leds_total = n_of_led_per_meter*distance_meters

    number_of_leds_pool = n_of_led_per_meter*distance_meters_pool
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
    print("distance per led: ",distance_per_led)

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
    print('change direction: '+str(direction_change_led))
    

    # Calculate the LED number at which the intermittent effect should end
    intermittent_end_to_led = round(number_of_leds_total - color_change_led_3) /2
    intermittent_end_led=round(number_of_leds_total - intermittent_end_to_led)
    print('intermitencia'+str(intermittent_end_led))

# Calculate the LED number at which the forward-backward movement should start
    forward_backward_start_led = round(number_of_leds_total - LEDTimeSimulation.led_number_at_distance(17.0, distance_per_led))

    # Calculate the LED number at which the intermittent effect should start and end
    intermittent_start_led = round((color_change_led_3 + number_of_leds_total) / 2)
    intermittent_end_led = number_of_leds_total
    last_led = ''
    start_time = time.time()
    count=0
    n_loop=1
    # Simulate NeoPixel LEDs
    for i in range(int(number_of_leds_total)):
        distance_traveled = (i + 1)

        

        if n_loop%2!=0 and distance_traveled  < direction_change_led:
            if distance_traveled  < direction_change_led:
                count+=1
                     
                if distance_traveled <= color_change_led_1:
                    last_led='R'
                    print(f"LED {count}: R > *")  # Use "R" to represent red color for the first section of LEDs
                elif distance_traveled <= color_change_led_2:
                    last_led='G'
                    print(f"LED {count}: G > *")  # Use "G" to represent green color for the second section of LEDs
                elif distance_traveled <= color_change_led_3:
                    last_led='B'
                    print(f"LED {count}: B > *")  # Use "B" to represent blue color for the third section of LEDs
                elif distance_traveled <= intermittent_start_led:
                    last_led='Y'
                    print(f"LED {count}: Y > *")
                else:
                    if distance_traveled >= intermittent_start_led and i + 1 <= intermittent_end_led and last_led == 'Y':
                        last_led = 'Off'
                        print(f"LED {count}: Y>*")  # Use "Y" to represent the intermittent color
                    else:
                        last_led='Y'
                        print(f"LED {count}: Off")  # Turn off the LEDs for the rest of the cycle    
        elif count==direction_change_led:
            n_loop+=1
            print("n_loop"+str(n_loop))

        elif n_loop%2==0 and distance_traveled  < direction_change_led:
                
            count-=1
            distance_traveled = (distance_traveled - 1)
            if distance_traveled <= color_change_led_1:
                last_led='R'
                
                print(f"LED {count}: R < *")  # Use "R" to represent red color for the first section of LEDs
            elif distance_traveled <= color_change_led_2:
                last_led='G'
                print(f"LED {count}: G < *")  # Use "G" to represent green color for the second section of LEDs
            elif distance_traveled <= color_change_led_3:
                last_led='B'
                print(f"LED {count}: B < *")  # Use "B" to represent blue color for the third section of LEDs
            elif distance_traveled <= intermittent_start_led:
                last_led='Y'
                print(f"LED {count}: Y < *")
            else:
                if distance_traveled >= intermittent_start_led and i + 1 <= intermittent_end_led and last_led == 'Y':
                    last_led = 'Off'
                    print(f"LED {count}: Y<*")  # Use "Y" to represent the intermittent color
                else:
                    last_led='Y'
                    print(f"LED {count}: Off")  # Turn off the LEDs for the rest of the cycle
            n_loop+=1

        time.sleep(time_per_led_seconds)  # Add a delay to simulate LED movement

    end_time = time.time()
    led_1_to_300_time = end_time - start_time
    print(f"Time for LED 1 to LED 300: {led_1_to_300_time:.3f} seconds")


if __name__ == "__main__":
    simulate_neo_pixels()



