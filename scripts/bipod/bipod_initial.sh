#!/bin/bash

/bin/bash ./bipod_move_tibia.sh "left"   "0.0" & 
          ./bipod_move_tibia.sh "middle" "0.0" &
          ./bipod_move_tibia.sh "right"  "0.0" &
          ./bipod_move_femur.sh "left"   "0.0" & 
          ./bipod_move_femur.sh "middle" "0.0" &
          ./bipod_move_femur.sh "right"  "0.0" &
          ./bipod_move_coxa.sh  "left"   "0.0" &
          ./bipod_move_coxa.sh  "middle" "0.0" &
          ./bipod_move_coxa.sh  "right"  "0.0"