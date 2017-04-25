#!/bin/bash

if [ $1 = left ] ; then
    echo `rostopic pub -1 /hexapod/tibia_l3_joint_position_controller/command std_msgs/Float64 "data: $2" & 
          rostopic pub -1 /hexapod/tibia_l1_joint_position_controller/command std_msgs/Float64 "data: $2" & 
          rostopic pub -1 /hexapod/tibia_r2_joint_position_controller/command std_msgs/Float64 "data: $2"
          `
else
    echo `rostopic pub -1 /hexapod/tibia_r3_joint_position_controller/command std_msgs/Float64 "data: $2" & 
          rostopic pub -1 /hexapod/tibia_r1_joint_position_controller/command std_msgs/Float64 "data: $2" & 
          rostopic pub -1 /hexapod/tibia_l2_joint_position_controller/command std_msgs/Float64 "data: $2" 
          `
fi
