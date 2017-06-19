#!/usr/bin/env python
import  rospy
from  std_msgs.msg import  Float64


class Movement(): 
    #Publishers
    pub_tibia_l1 = None
    pub_tibia_l2 = None
    pub_tibia_l3 = None
    
    pub_tibia_r1 = None
    pub_tibia_r2 = None
    pub_tibia_r3 = None

    pub_femur_l1 = None
    pub_femur_l2 = None
    pub_femur_l3 = None

    pub_femur_r1 = None
    pub_femur_r2 = None
    pub_femur_r3 = None

    pub_coxa_l1 = None
    pub_coxa_l2 = None
    pub_coxa_l3 = None

    pub_coxa_r1 = None
    pub_coxa_r2 = None
    pub_coxa_r3 = None

    def __init__ (self, femur_left=(None,None,None), 
                        femur_right=(None,None,None), 
                        coxa_left=(None,None,None), 
                        coxa_right=(None,None,None),
                        tibia_left=(None,None,None),
                        tibia_right=(None,None,None)) :

        self.pub_tibia_l1 = tibia_left[0]
        self.pub_tibia_l2 = tibia_left[1]
        self.pub_tibia_l3 = tibia_left[2]

        self.pub_tibia_r1 = tibia_right[0]
        self.pub_tibia_r2 = tibia_right[1]
        self.pub_tibia_r3 = tibia_right[2]

        self.pub_femur_l1 = femur_left[0]
        self.pub_femur_l2 = femur_left[1]
        self.pub_femur_l3 = femur_left[2]

        self.pub_femur_r1 = femur_right[0]
        self.pub_femur_r2 = femur_right[1]
        self.pub_femur_r3 = femur_right[2]

        self.pub_coxa_l1 = coxa_left[0]
        self.pub_coxa_l2 = coxa_left[1]
        self.pub_coxa_l3 = coxa_left[2]

        self.pub_coxa_r1 = coxa_right[0]
        self.pub_coxa_r2 = coxa_right[1]
        self.pub_coxa_r3 = coxa_right[2]

    
    def initial_position(self):
        self.pub_femur_l1.publish(0.0)
        self.pub_femur_l2.publish(0.0)
        self.pub_femur_l3.publish(0.0)
        self.pub_femur_r1.publish(0.0)
        self.pub_femur_r2.publish(0.0)
        self.pub_femur_r3.publish(0.0)
        
        self.pub_coxa_l1.publish(0.0)
        self.pub_coxa_l2.publish(0.0)
        self.pub_coxa_l3.publish(0.0)
        self.pub_coxa_r1.publish(0.0)
        self.pub_coxa_r2.publish(0.0)
        self.pub_coxa_r3.publish(0.0)

        self.pub_femur_l1.publish(0.0)
        self.pub_femur_l2.publish(0.0)
        self.pub_femur_l3.publish(0.0)
        self.pub_femur_r1.publish(0.0)
        self.pub_femur_r2.publish(0.0)
        self.pub_femur_r3.publish(0.0)
    