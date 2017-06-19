#!/usr/bin/env python
from movement import Movement

FEMUR_UP = 0.6
DOWN = 0.0
SIDE_VALUE = 0.2



class TurnSide(Movement) :

    def moveLegVertical(self, legSide, direction):
        value = 0.0
        
        if direction == "up":
            value = FEMUR_UP
        elif direction == "down":
            value = DOWN

        if legSide == "left":
            self.pub_femur_l1.publish(value)
            self.pub_femur_r2.publish(value)
            self.pub_femur_l3.publish(value)
        elif legSide == "right":
            self.pub_femur_r1.publish(value)
            self.pub_femur_l2.publish(value)
            self.pub_femur_r3.publish(value)
    
    def moveLeftLegHorizontal(self, direction):
        if direction == "left":
            value = SIDE_VALUE
        elif direction == "right":
            value = -SIDE_VALUE

        self.pub_coxa_l1.publish(value)
        self.pub_coxa_r2.publish(value)
        self.pub_coxa_l3.publish(value)
       
        
    def moveRightLegHorizontal(self, direction):
        if direction == "left":
            value = SIDE_VALUE
        elif direction == "right":
            value = -SIDE_VALUE

        self.pub_coxa_r1.publish(value)
        self.pub_coxa_l2.publish(value)
        self.pub_coxa_r3.publish(value)