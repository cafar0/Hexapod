#!/usr/bin/env python
from movement import Movement

FEMUR_UP = 1.0
COXA_FWD = 0.4
DOWN = 0.1
NEUTRAL = 0.0


class Tripod(Movement) :

    def moveLeftLeg(self,value) : 
        self.pub_femur_l1.publish(value)
        self.pub_femur_r2.publish(value)
        self.pub_femur_l3.publish(value)

    def moveRightLeg(self,value) :
        self.pub_femur_r1.publish(value)
        self.pub_femur_l2.publish(value)
        self.pub_femur_r3.publish(value)

    def liftLeftLeg(self) :
        self.pub_femur_l1.publish(0.8)
        self.pub_femur_r2.publish(0.8)
        self.pub_femur_l3.publish(0.8)
        # self.moveRightLeg(-0.2)

    def lowerLeftLeg(self) :
        self.pub_femur_l1.publish(DOWN)
        self.pub_femur_r2.publish(DOWN)
        self.pub_femur_l3.publish(DOWN)
        # self.moveRightLeg(0.0)

    def liftRightLeg(self) :
        self.pub_femur_r1.publish(FEMUR_UP)
        self.pub_femur_l2.publish(FEMUR_UP)
        self.pub_femur_r3.publish(FEMUR_UP)
        # self.moveLeftLeg(-0.2)

    def lowerRightLeg(self) :
        self.pub_femur_r1.publish(DOWN)
        self.pub_femur_l2.publish(DOWN)
        self.pub_femur_r3.publish(DOWN)
        # self.moveLeftLeg(0.0)

    def moveLeftLegForward(self) :
        self.pub_coxa_l1.publish(0.3)
        self.pub_coxa_r2.publish(-0.3)
        self.pub_coxa_l3.publish(0.3)

    def moveLeftLegNeutral(self) :
        self.pub_coxa_l1.publish(NEUTRAL)
        self.pub_coxa_r2.publish(NEUTRAL)
        self.pub_coxa_l3.publish(NEUTRAL)

    def moveRightLegForward(self) :
        self.pub_coxa_r1.publish(-COXA_FWD)
        self.pub_coxa_l2.publish(COXA_FWD)
        self.pub_coxa_r3.publish(-COXA_FWD)

    def moveRightLegNeutral(self) :
        self.pub_coxa_r1.publish(-0.06)
        self.pub_coxa_l2.publish(-0.06)
        self.pub_coxa_r3.publish(-0.06)