#!/usr/bin/env python
from movement import Movement

FEMUR_UP = 0.6
COXA_FWD = 0.4
DOWN = 0.1
NEUTRAL = 0.0

class Bipod(Movement):

    def liftLeftStep(self) :
        self.pub_femur_l1.publish(FEMUR_UP)
        self.pub_femur_r3.publish(FEMUR_UP)

    def lowerLeftStep(self) :
        self.pub_femur_l1.publish(DOWN)
        self.pub_femur_r3.publish(DOWN)

    def leftStepFwd(self) :
        self.pub_coxa_l1.publish(COXA_FWD) 
        self.pub_coxa_r3.publish(-COXA_FWD)

    def leftStepNeutral(self) :
        self.pub_coxa_l1.publish(NEUTRAL) 
        self.pub_coxa_r3.publish(NEUTRAL)

    def liftMiddleStep(self) :
        self.pub_femur_l2.publish(FEMUR_UP) 
        self.pub_femur_r2.publish(FEMUR_UP)

    def lowerMiddleStep(self) :
        self.pub_femur_l2.publish(DOWN) 
        self.pub_femur_r2.publish(DOWN)

    def middleStepFwd(self) :
        self.pub_coxa_l2.publish(COXA_FWD) 
        self.pub_coxa_r2.publish(-COXA_FWD)

    def middleStepNeutral(self) :
        self.pub_coxa_l2.publish(NEUTRAL) 
        self.pub_coxa_r2.publish(NEUTRAL)

    def liftRightStep(self) :
        self.pub_femur_l3.publish(FEMUR_UP)
        self.pub_femur_r1.publish(FEMUR_UP)

    def lowerRightStep(self) :
        self.pub_femur_l3.publish(DOWN)
        self.pub_femur_r1.publish(DOWN)

    def rightStepFwd(self) :
        self.pub_coxa_l3.publish(COXA_FWD) 
        self.pub_coxa_r1.publish(-COXA_FWD)

    def rightStepNeutral(self) :
        self.pub_coxa_l3.publish(NEUTRAL) 
        self.pub_coxa_r1.publish(NEUTRAL)