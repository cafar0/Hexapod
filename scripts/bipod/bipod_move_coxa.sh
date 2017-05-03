#!/bin/bash

REVERSE=$2

if [[ $REVERSE =~ ^[-+]?[0-9]+\.?[0-9]*$ ]]; then
  if [[ $REVERSE =~ ^[-] ]]; then
    REVERSE=${REVERSE#-}
  else 
    REVERSE=-$REVERSE
  fi    
fi

if [ $1 = left ] ; then
    echo `rostopic pub -1 /hexapod/coxa_l1_joint_position_controller/command std_msgs/Float64 "data: $2" & 
          rostopic pub -1 /hexapod/coxa_r3_joint_position_controller/command std_msgs/Float64 "data: $REVERSE"
          `
else if [ $1 = middle ]; then
    echo `rostopic pub -1 /hexapod/coxa_l2_joint_position_controller/command std_msgs/Float64 "data: $2" & 
          rostopic pub -1 /hexapod/coxa_r2_joint_position_controller/command std_msgs/Float64 "data: $REVERSE"
          `
else
    echo `rostopic pub -1 /hexapod/coxa_l3_joint_position_controller/command std_msgs/Float64 "data: $2" & 
          rostopic pub -1 /hexapod/coxa_r1_joint_position_controller/command std_msgs/Float64 "data: $REVERSE" 
          `
fi
fi