#!/usr/bin/env python
import  rospy
from  std_msgs.msg import  Float64


FEMUR_UP = 1.0
COXA_FWD = 0.4
DOWN = 0.0
NEUTRAL = 0.0

class Movement(): 
    #Publishers
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

    def __init__ (self, femur_left, femur_right, coxa_left, coxa_right) :
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

    def liftLeftLeg(self) :
        self.pub_femur_l1.publish(FEMUR_UP)
        self.pub_femur_r2.publish(FEMUR_UP)
        self.pub_femur_l3.publish(FEMUR_UP)

    def lowerLeftLeg(self) :
        self.pub_femur_l1.publish(DOWN)
        self.pub_femur_r2.publish(DOWN)
        self.pub_femur_l3.publish(DOWN)

    def liftRightLeg(self) :
        self.pub_femur_r1.publish(FEMUR_UP)
        self.pub_femur_l2.publish(FEMUR_UP)
        self.pub_femur_r3.publish(FEMUR_UP)

    def lowerRightLeg(self) :
        self.pub_femur_r1.publish(DOWN)
        self.pub_femur_l2.publish(DOWN)
        self.pub_femur_r3.publish(DOWN)

    def moveLeftLegForward(self) :
        self.pub_coxa_l1.publish(0.4)
        self.pub_coxa_r2.publish(-0.4)
        self.pub_coxa_l3.publish(0.4)

    def moveLeftLegNeutral(self) :
        self.pub_coxa_l1.publish(NEUTRAL)
        self.pub_coxa_r2.publish(NEUTRAL)
        self.pub_coxa_l3.publish(NEUTRAL)

    def moveRightLegForward(self) :
        self.pub_coxa_r1.publish(-COXA_FWD)
        self.pub_coxa_l2.publish(COXA_FWD)
        self.pub_coxa_r3.publish(-COXA_FWD)

    def moveRightLegNeutral(self) :
        self.pub_coxa_r1.publish(NEUTRAL)
        self.pub_coxa_l2.publish(NEUTRAL)
        self.pub_coxa_r3.publish(NEUTRAL)