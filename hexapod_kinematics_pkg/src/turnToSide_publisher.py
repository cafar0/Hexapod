#!/usr/bin/env python
import  rospy
from std_msgs.msg import  Float64
from movement.turn_side import TurnSide
from publisher_singleton import PublisherSingleton

_is_moving = False
_leading_direction = "left"
_reverse_direction = "right"
rospy.init_node('turnToSide_publisher')

singleton = PublisherSingleton()
internal_pub = rospy.Publisher('/hexapod/turnToSide_internal/command', Float64, queue_size=2)
rate    =   rospy.Rate(3.2)

kinematic = TurnSide(singleton.leftFemurPublishers(),
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
    global _direction
    print('publishing...' + str(msg.data))

    if msg.data == 1 :
        _is_moving = True
        _leading_direction = "left"
        _reverse_direction = "right"
    elif msg.data == 2:
        _is_moving = True
        _leading_direction = "right"
        _reverse_direction = "left"
    kinematic.moveLegVertical("left","up")
    kinematic.moveLeftLegHorizontal("right")
    rate.sleep()

    while True :
       kinematic.moveLegVertical("left","down")
       if _is_moving == False:
        break
       rate.sleep()
       kinematic.moveLegVertical("right", "up")
       rate.sleep()

       kinematic.moveLeftLegHorizontal(_leading_direction)
       kinematic.moveRightLegHorizontal(_reverse_direction)
       rate.sleep()

       kinematic.moveLegVertical("right","down")
       if _is_moving == False:
        break
       rate.sleep()

       kinematic.moveLegVertical("left","up")
       rate.sleep()

       kinematic.moveLeftLegHorizontal(_reverse_direction)
       kinematic.moveRightLegHorizontal(_leading_direction)
       rate.sleep()
    kinematic.initial_position()
       
internal_sub = rospy.Subscriber('/hexapod/turnToSide_internal/command', Float64,  internal_callback)
sub = rospy.Subscriber('counter', Float64, callback)
rospy.spin()
   