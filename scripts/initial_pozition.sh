#!/bin/bash

/bin/bash ./tripod_move_tibia.sh "right" "0.0" & 
          ./tripod_move_tibia.sh "left"  "0.0" &
          ./tripod_move_femur.sh "right" "0.0" & 
          ./tripod_move_femur.sh "left"  "0.0" &
          ./tripod_move_coxa.sh  "right" "0.0" &
          ./tripod_move_coxa.sh  "left"  "0.0"