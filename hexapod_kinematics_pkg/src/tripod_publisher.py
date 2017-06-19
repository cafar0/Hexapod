#!/usr/bin/env python
import  rospy
from std_msgs.msg import  Float64
from movement.tripod import Tripod
from publisher_singleton import PublisherSingleton

_is_moving = False
rospy.init_node('tripod_publisher')

singleton = PublisherSingleton()
internal_pub = rospy.Publisher('/hexapod/tripod_internal/command', Float64, queue_size=2)
rate    =   rospy.Rate(3.2)

kinematic = Tripod(singleton.leftFemurPublishers(),
                     singleton.rightFemurPublishers(),
                     singleton.leftCoxaPublishers(),
                     singleton.rightCoxaPublishers())
    
def callback(msg):
    global _is_moving
    
    if msg.data == 0:
        _is_moving = False
        internal_pub.publish(0)
    elif _is_moving == False:
        _is_moving = True
        internal_pub.publish(msg.data)
        

def internal_callback(msg):
    global _is_moving
    _forward = True
    print('publishing...' + str(msg.data))

    if msg.data == 1 :
        _is_moving = True
        _forward = True
    elif msg.data == 2:
        _is_moving = True
        _forward = False
    
    kinematic.liftLeftLeg()
    rate.sleep()
    while True :
        if _forward == True:
            kinematic.moveLeftLegForward()
        else:
            kinematic.moveLeftLegBackward()
        rate.sleep()
    
        kinematic.lowerLeftLeg()
        if _is_moving == False:
            break
        rate.sleep()

        kinematic.liftRightLeg()
        kinematic.moveLeftLegNeutral()
        
        if _forward == True:            
            kinematic.moveRightLegForward()
        else:
            kinematic.moveRightLegBackward()
        rate.sleep()

        kinematic.lowerRightLeg()
        if _is_moving == False:
            break
        rate.sleep()
        
        kinematic.liftLeftLeg()
        kinematic.moveRightLegNeutral()
    kinematic.initial_position()

internal_sub = rospy.Subscriber('/hexapod/tripod_internal/command', Float64,  internal_callback)
sub = rospy.Subscriber('counter', Float64, callback)
rospy.spin()
   