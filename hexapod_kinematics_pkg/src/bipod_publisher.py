#! /usr/bin/env python
import  rospy
from std_msgs.msg import  Float64
from movement.bipod import Bipod

rospy.init_node('bipod_publisher')

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

rate = rospy.Rate(2.5)

kinematic = Bipod((pub_femur_l1,pub_femur_l2,pub_femur_l3),
                   (pub_femur_r1,pub_femur_r2,pub_femur_r3),
                   (pub_coxa_l1, pub_coxa_l2, pub_coxa_l3),
                   (pub_coxa_r1, pub_coxa_r2, pub_coxa_r3))


def callback(msg):
    if msg.data == 0 :
        print('Publishing... ')

        kinematic.moveRightStepVertical(0.3)
        rate.sleep()

        while True :
            kinematic.moveLeftStepVertical(0.0)
            kinematic.moveMiddleStepVertical(0.3)
            kinematic.moveLeftStepHorizontal(-0.4)
            kinematic.moveMiddleStepHorizontal(0.0)
            rate.sleep()

            kinematic.moveRightStepVertical(0.0)
            kinematic.moveLeftStepVertical(0.3)
            kinematic.moveRightStepHorizontal(-0.4)
            kinematic.moveLeftStepHorizontal(0.06)
            rate.sleep()

            kinematic.moveMiddleStepVertical(0.0)
            kinematic.moveMiddleStepHorizontal(-0.4)
            kinematic.moveRightStepHorizontal(0.0)
            kinematic.moveRightStepVertical(0.3)
            rate.sleep()
        

sub = rospy.Subscriber('counter', Float64,  callback)
rospy.spin()