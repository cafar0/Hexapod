#!/usr/bin/env python
import  rospy
from  std_msgs.msg import  Float64

stage_1 = 0
stage_2 = 1
stage_3 = 2
stage_4 = 3

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

rate    =   rospy.Rate(1.5)
rate_calib = rospy.Rate(1.0)
count   =   0

def stage_1_movement():
    # prepare for left step 
    # lift left leg
    pub_femur_l1.publish(1.0)
    pub_femur_r2.publish(1.0)
    pub_femur_l3.publish(1.0)
    rate.sleep()

def stage_2_left_movement():
    # move left leg fwd
    pub_coxa_l1.publish(0.4)
    pub_coxa_r2.publish(-0.4)
    pub_coxa_l3.publish(0.4)
    rate.sleep()
    
    # lower left leg
    pub_femur_l1.publish(0.0)
    pub_femur_r2.publish(0.0)
    pub_femur_l3.publish(0.0)
    rate.sleep()

def stage_2_left_complition():
    # move coxa bwd
    #TODO:remove additional sleep after calibrating joint's speed and effort
    rate.sleep()
    pub_coxa_l1.publish(0.0)
    pub_coxa_r2.publish(0.0)
    pub_coxa_l3.publish(0.0)
    # lift right leg
    pub_femur_r1.publish(1.0)
    pub_femur_l2.publish(1.0)
    pub_femur_r3.publish(1.0)
    

def stage_2_right_movement():
    # move right leg fwd
    pub_coxa_r1.publish(-0.4)
    pub_coxa_l2.publish(0.4)
    pub_coxa_r3.publish(-0.4)
    rate.sleep()
    
    # lower right leg
    pub_femur_r1.publish(0.0)
    pub_femur_l2.publish(0.0)
    pub_femur_r3.publish(0.0)
    rate.sleep()

def stage_2_right_completion():
    # move right leg bwd
    rate.sleep()
    pub_coxa_r1.publish(0.0)
    pub_coxa_l2.publish(0.0)
    pub_coxa_r3.publish(0.0)
    # lift left leg
    pub_femur_l1.publish(1.0)
    pub_femur_r2.publish(1.0)
    pub_femur_l3.publish(1.0)
    

def initial_position():
    pub_coxa_l1.publish(0.0)
    pub_coxa_l2.publish(0.0)
    pub_coxa_l3.publish(0.0)
    pub_coxa_r1.publish(0.0)
    pub_coxa_r2.publish(0.0)
    pub_coxa_r3.publish(0.0)

    pub_femur_l1.publish(0.0)
    pub_femur_l2.publish(0.0)
    pub_femur_l3.publish(0.0)
    pub_femur_r1.publish(0.0)
    pub_femur_r2.publish(0.0)
    pub_femur_r3.publish(0.0)
    rate.sleep()


def callback(msg):
    print('publishing...' + str(msg.data))

    if msg.data == 0 :
        loop_condition = True
        stage_1_movement()
        while loop_condition:
            stage_2_left_movement()
            stage_2_left_complition()
            stage_2_right_movement()
            stage_2_right_completion()
        initial_position()
#    else :      

    rate.sleep()

sub = rospy.Subscriber('counter', Float64,  callback)
rospy.spin()
   

