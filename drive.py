#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tell Vector to drive on and off the charger.
"""

import anki_vector

from anki_vector.util import degrees, distance_mm, speed_mmps, Position


def main():
    args = anki_vector.util.parse_command_args()
    #anki_vector.nav_map.NavMapComponent.init_nav_map_feed(frequency=0.5)
    with anki_vector.Robot(args.serial, show_3d_viewer=True) as robot:
        robot.show_viewer=True
        robot.enable_camera_feed=True
        robot.viewer.show_video()
        
        robot.enable_custom_object_detection=True
        robot.enable_nav_map_feed=True



        current_robot_pose = robot.pose.position
        print (current_robot_pose)    
        print("Drive Vector off of charger...")
        robot.behavior.drive_off_charger()
        
        current_robot_pose = robot.pose.position
        print (current_robot_pose)    
        
        robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
        current_robot_pose = robot.pose.position
        print (current_robot_pose) 
        
        robot.behavior.turn_in_place(degrees(90))   
        current_robot_pose = robot.pose.position
        print (current_robot_pose) 

       

        robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
        current_robot_pose = robot.pose.position
        print (current_robot_pose)    

        robot.behavior.turn_in_place(degrees(90))   
        current_robot_pose = robot.pose.position
        print (current_robot_pose) 


        robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
        current_robot_pose = robot.pose.position
        print (current_robot_pose)    

        robot.behavior.turn_in_place(degrees(90))   
        current_robot_pose = robot.pose.position
        print (current_robot_pose) 


        robot.behavior.drive_straight(distance_mm(100), speed_mmps(100))
        current_robot_pose = robot.pose.position
        print (current_robot_pose)    

        robot.behavior.turn_in_place(degrees(90))   
        current_robot_pose = robot.pose.position
        print (current_robot_pose) 

        #latest_nav_map = robot.nav_map.latest_nav_map
        #throws exception not to be initialized

        robot.behavior.drive_on_charger()
        current_robot_pose = robot.pose.position
        print (current_robot_pose)    

    

if __name__ == '__main__':
    main()
