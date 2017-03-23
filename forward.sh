#!/bin/bash

SLEEP_PERIOD=3

# Set initial position
sleep $SLEEP_PERIOD
/bin/bash ./tripod_move_tibia.sh "right" "0.0" & ./tripod_move_tibia "left" "0.0"

sleep $SLEEP_PERIOD
/bin/bash ./tripod_move_femur.sh "right" "0.0" & ./tripod_move_femur "left" "0.0"

# Prepare for Right Step
sleep $SLEEP_PERIOD
/bin/bash ./tripod_move_femur.sh "right" "1.0" 


 while [  1  ]; do
    # Right step
	sleep $SLEEP_PERIOD
	/bin/bash ./tripod_move_coxa.sh "right" "0.4"

	sleep $SLEEP_PERIOD
	/bin/bash ./tripod_move_femur.sh "right" "0.0"

	sleep $SLEEP_PERIOD
	/bin/bash ./tripod_move_coxa.sh "right" "0.0" & ./tripod_move_femur.sh "left" "1.0"

	# Left step
	sleep $SLEEP_PERIOD
	/bin/bash ./tripod_move_coxa.sh "left" "-0.4"

	sleep $SLEEP_PERIOD
	/bin/bash ./tripod_move_femur.sh "left" "0.0"

	sleep $SLEEP_PERIODs
	/bin/bash ./tripod_move_coxa.sh "left" "0.0" & ./tripod_move_femur.sh "right" "1.0"
 done