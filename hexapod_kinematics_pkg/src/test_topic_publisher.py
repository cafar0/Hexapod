#!/usr/bin/env python
import  rospy
from std_msgs.msg import  Float64
from movement.tripod import Tripod

rospy.init_node('topic_publisher')

pub_femur_l1 = rospy.Publisher('/hexapod/femur_l1_joint_position_controller/command',  Float64, queue_size=2)
pub_femur_l2 = rospy.Publisher('/hexapod/femur_l2_joint_position_controller/command',  Float64, queue_size=2)
pub_femur_l3 = rospy.Publisher('/hexapod/femur_l3_joint_position_controller/command',  Float64, queue_size=2)

pub_femur_r1 = rospy.Publisher('/hexapod/femur_r1_joint_position_controller/command',  Float64, queue_size=2)
pub_femur_r2 = rospy.Publisher('/hexapod/femur_r2_joint_position_controller/command',  Float64, queue_size=2)
pub_femur_r3 = rospy.Publisher('/hexapod/femur_r3_joint_position_controller/command',  Float64, queue_size=2)

pub_coxa_l1 = rospy.Publisher('/hexapod/coxa_l1_joint_position_controller/command',  Float64, queue_size=2)
pub_coxa_l2 = rospy.Publisher('/hexapod/coxa_l2_joint_position_controller/command',  Float64, queue_size=2)
pub_coxa_l3 = rospy.Publisher('/hexapod/coxa_l3_joint_position_controller/command',  Float64, queue_size=2)

pub_coxa_r1 = rospy.Publisher('/hexapod/coxa_r1_joint_position_controller/command',  Float64, queue_size=2)
pub_coxa_r2 = rospy.Publisher('/hexapod/coxa_r2_joint_position_controller/command',  Float64, queue_size=2)
pub_coxa_r3 = rospy.Publisher('/hexapod/coxa_r3_joint_position_controller/command',  Float64, queue_size=2)

rate    =   rospy.Rate(1.7)
rate_calib = rospy.Rate(1.0)
count   =   0

kinematic = Tripod((pub_femur_l1,pub_femur_l2,pub_femur_l3),
                   (pub_femur_r1,pub_femur_r2,pub_femur_r3),
                   (pub_coxa_l1, pub_coxa_l2, pub_coxa_l3),
                   (pub_coxa_r1, pub_coxa_r2, pub_coxa_r3))
    


def callback(msg):
    print('publishing...' + str(msg.data))

    if msg.data == 0 :
        loop_condition = True
        
        
        kinematic.liftLeftLeg()
        rate.sleep()

        while True :
            kinematic.moveLeftLegForward()
            rate.sleep()
        
            kinematic.lowerLeftLeg()
            rate.sleep()

            kinematic.liftRightLeg()
            # rate.sleep()
            kinematic.moveLeftLegNeutral()
            # rate.sleep()
                
            kinematic.moveRightLegForward()
            rate.sleep()

            kinematic.lowerRightLeg()
            rate.sleep()
            
            kinematic.liftLeftLeg()
            kinematic.moveRightLegNeutral()


    rate.sleep()
        # initial_position()
#    else :      

sub = rospy.Subscriber('counter', Float64,  callback)
rospy.spin()
   

