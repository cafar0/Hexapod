import  rospy
from std_msgs.msg import  Float64

class PublisherSingleton:
    class __OnlyOne:
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

        pub_tibia_l1 = rospy.Publisher('/hexapod/tibia_l1_joint_position_controller/command',  Float64, queue_size=2)
        pub_tibia_l2 = rospy.Publisher('/hexapod/tibia_l2_joint_position_controller/command',  Float64, queue_size=2)
        pub_tibia_l3 = rospy.Publisher('/hexapod/tibia_l3_joint_position_controller/command',  Float64, queue_size=2)

        pub_tibia_r1 = rospy.Publisher('/hexapod/tibia_r1_joint_position_controller/command',  Float64, queue_size=2)
        pub_tibia_r2 = rospy.Publisher('/hexapod/tibia_r2_joint_position_controller/command',  Float64, queue_size=2)
        pub_tibia_r3 = rospy.Publisher('/hexapod/tibia_r3_joint_position_controller/command',  Float64, queue_size=2)
            
        def __str__(self):
            return repr(self) + self.val
    
        def leftFemurPublishers(self):
            return (self.pub_femur_l1,self.pub_femur_l2,self.pub_femur_l3)

        def rightFemurPublishers(self):
            return (self.pub_femur_r1,self.pub_femur_r2,self.pub_femur_r3)

        def leftCoxaPublishers(self):
            return (self.pub_coxa_l1,self.pub_coxa_l2,self.pub_coxa_l3)

        def rightCoxaPublishers(self):
            return (self.pub_coxa_r1,self.pub_coxa_r2,self.pub_coxa_r3)

        def leftTibiaPublishers(self):
            return (self.pub_tibia_l1,self.pub_tibia_l2,self.pub_tibia_l3)

        def rightTibiaPublishers(self):
            return (self.pub_tibia_r1,self.pub_tibia_r2,self.pub_tibia_r3)


    instance = None
    def __init__(self):
        if not PublisherSingleton.instance:
            PublisherSingleton.instance = PublisherSingleton.__OnlyOne()
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
