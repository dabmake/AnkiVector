"""
Copyright Kinvert All Rights Reserved
If you would like to use this code for
business or education please contact
us for permission at:
www.kinvert.com/
"""

import anki_vector
import time

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot() as robot:
        for _ in range(5):
            if robot.proximity.last_sensor_reading:
                distance = robot.proximity.last_sensor_reading.distance
                print("=====================================================================")
                print(distance.distance_inches)
                print("=====================================================================")
                robot.say_text(str(distance.distance_mm) + " millimeters or " + str("%.2f" % distance.distance_inches ) + "freedom units")
                time.sleep(4.0)
            else:
                print("Can't be bothered to work right now")
                robot.say_text("Hold your horses")
                time.sleep(3.0)

if __name__ == "__main__":
    main()

