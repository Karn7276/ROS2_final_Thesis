from email.headerregistry import DateHeader
import rclpy
from rclpy.node import Node
import math
from math import *
import numpy as np
import copy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge 
from bboxes_ex_msgs.msg import BoundingBoxes, BoundingBox
ranges_filter = []
intensities_filter = []
filterScan= LaserScan()
class MinimalSubscriber(Node):

    def __init__(self):
        global filterScan 
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.callback_scan,
            50)
        self.subscription  # prevent unused variable warning
        self.subscription2 = self.create_subscription(
            Image,
            'yolov5/image_raw',
            self.callback_scan2,
            50)
        self.subscription2  # prevent unused variable warning
        self.subscription3 = self.create_subscription(
            BoundingBoxes,
            'yolov5/bounding_boxes',
            self.callback_scan3,
            50)
        self.subscription3  # prevent unused variable warning
        self.publisher_ = self.create_publisher(LaserScan, '/filtere_data', 50)
        self.br = CvBridge()
    def callback_scan(self, data):
        global ranges_filter, intensities_filter, filterScan

        len(data.ranges) #360
        len(data.intensities) #360

        ranges_filter = copy.copy(data.ranges)
        intensities_filter = copy.copy(data.intensities)

    #convert them to list
        ranges_filter = list(ranges_filter)
        intensities_filter = list(intensities_filter)

     #filtering those angles that I do not want them (based on the question)
        for x in range(30, 330):
            ranges_filter[x] = 0
            intensities_filter[x] = 0
            data.ranges[x] = 0
            data.intensities[x] = 0
        
        self.publisher_.publish(data)
        #self.get_logger().info('I ranges: "%s"' % filterScan)
        #self.get_logger().info('I ranges: "%s"' % data)
        #self.get_logger().info('I intensities: "%s"' % filterScan.intensities)
    def callback_scan2(self, data):
        current_frame = self.br.imgmsg_to_cv2(data) 
        cv2.imshow("camera", current_frame)
        cv2.waitKey(1)
    def callback_scan3(self, data):
        self.get_logger().info('bounding data: "%s"' % data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
