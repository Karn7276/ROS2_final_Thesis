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
            'video_frames',
            self.callback_scan2,
            50)
        self.subscription2  # prevent unused variable warning
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
        
     #filtering those angles that I do not want them (based on the question

        for x in range(25,346):
            ranges_filter[x] = 0
            intensities_filter[x] = 0
            data.ranges[x] = 0
            data.intensities[x] = 0
        
        new = np.nonzero(np.array(ranges_filter))
        new_min = np.argmin(np.array(ranges_filter)[new])
        #print(new_min, ranges_filter[new_min])
        self.publisher_.publish(data)
        #self.get_logger().info('I ranges: "%s"' % filterScan)
        #self.get_logger().info('I ranges: "%s"' % data)
        #self.get_logger().info('I intensities: "%s"' % filterScan.intensities)
    def callback_scan2(self, data):
        global current_frame
        current_frame = self.br.imgmsg_to_cv2(data)
        #cv2.rectangle(current_frame,(bound[0].xmin,bound[0].ymin), (bound[0].xmax,bound[0].ymax), color='red')
        img_blur = cv2.GaussianBlur(current_frame,(3,3), SigmaX=0, SigmaY=0)
        edges = cv2.Canny(img_blur,150,200)
        cv2.imshow('edges', edges)
        cv2.waitKey(1)
        #corners = cv2.goodFeaturesToTrack(edges,1,100,10,)
        #corners = np.int0(corners)
        #for i in corners:
        #    x,y = i.ravel()
        #print(x)
        #print(box)
        """ if corners:
            x_cen = x
            if x_cen <417:
                dept = ranges_filter[int(0+(x_cen*6/100))]
            else:
                dept = ranges_filter[int((x_cen*6/100)-385)]
            self.get_logger().info('bounding data: "%s"' % dept)
            self.get_logger().info('bounding data: "%s"' % x_cen)
        #self.get_logger().info('min point: "%s"' % min1)
        #self.get_logger().info('min intensity: "%s"' % min_inst) """
        
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