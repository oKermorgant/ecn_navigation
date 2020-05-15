#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


rospy.init_node('joy_bridge')

twist = Twist()
cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=100)

axes = [0 for i in range(10)]
buttons = [0 for i in range(10)]

def joy_callback(msg):
    global axes
    global buttons
    axes = msg.axes
    buttons = msg.buttons


rospy.Subscriber('/joy', Joy, joy_callback)


while not rospy.is_shutdown():


    twist.linear.x = axes[1]*6
    twist.angular.z = axes[0]*5
    cmd_pub.publish(twist)


    rospy.sleep(0.01)
    






