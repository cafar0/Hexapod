#!/bin/bash
# Set initial position
/bin/bash ./tripod_move_tibia.sh "right" "0.0" & ./tripod_move_tibia.sh "left" "0.0"

/bin/bash ./tripod_move_femur.sh "right" "0.0" & ./tripod_move_femur.sh "left" "0.0"

# Prepare for Right Step
/bin/bash ./tripod_move_femur.sh "right" "1.0" 


 while [  1  ]; do
    # Right step
	/bin/bash ./tripod_move_coxa.sh "right" "0.4"

	/bin/bash ./tripod_move_femur.sh "right" "0.0"

	/bin/bash ./tripod_move_coxa.sh "right" "0.0" & ./tripod_move_femur.sh "left" "1.0"

	# Left step
	/bin/bash ./tripod_move_coxa.sh "left" "-0.4"

	# sleep $SLEEP_PERIOD
	/bin/bash ./tripod_move_femur.sh "left" "0.0"

	# sleep $SLEEP_PERIODs
	/bin/bash ./tripod_move_coxa.sh "left" "0.0" & ./tripod_move_femur.sh "right" "1.0"
 done