# ROS2 Node for [Intel Realsense D435i]

You acquired this code

```
───ros2foxy
│   │   cv_basics_ros2_README.md
│   │   rplidar-ros_README.md
```
And you are currently reading ```cv_basics_ros2_README.md```. Before you continue, install ros2 usign steps mentioned in the following link

(https://docs.ros.org/en/foxy/Installation.html)


Creat a ros2 workspace using foloowing steps 

(https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)

Great! You should now have a workspace and in the workspace/src clone the repo as mentioned below
[here](https://github.com/Karn7276/cv_basics.git).

## Getting Started

The ```setup.sh``` already built the ROS2-Package inside ```./realsense-ros``` and installed the
Intel-Realsense SDK. Connect the Stereo-Camera to your computer using a USB-C-to-USB cable. 
It's advised to use a USB3-port on your computer.

after cloning the repo please open package.xml and do the changes as below-

'''
<description>A minimal image publisher and subscriber node that uses OpenCV</description>
<maintainer email="your_mail_ID.todo">automaticaddison</maintainer>
<license>Apache License 2.0</license>
'''



Now open setup.py to make these changes-


```
entry_points={
    'console_scripts': [
      'img_publisher = cv_basics.webcam_pub:main',
      'img_subscriber = cv_basics.webcam_sub:main',
    ],
},
```



```
cd ros2_workspace
source /opt/ros/foxy/setup.sh
source ./install/setup.bash
rosdep install -i --from-path src --rosdistro foxy -y
```
(if you encountered following error please go to this link ERROR: the following packages/stacks could not have their rosdep keys resolved to system dependencies: cv_basics: Cannot locate rosdep definition for [opencv2]
solution:```https://answers.ros.org/question/383007/opencv-and-ros2/```)
and then

```
colcon build --packages-select cv_basics
```

```
ros2 run cv_basics img_publisher
```

open anothere terminar and run these commandas

```
source /opt/ros/foxy/setup.sh
source ./install/setup.bash
ros2 run cv_basics img_subscriber
```

to run the ROS2-Node. Check if it worked by opening a new terminal and calling

```
source /opt/ros/foxy/setup.bash
ros2 topic list
```

The topic list should contain

```
/parameter_events
/rosout
/video_frames
```

Congrats! You have successfully installed Intel Realsense D435i as a ROS2-Node.

## Help

Contact the [Authors](#Authors), but please make sure to make an effort before asking for help. For references, check


## Authors

Karan Dhage | [dhage@rhrk.uni-kl.de]
## Version History

* Version 0.01
    * I really hope it works.

## License

I have not yet started on licences.

## Acknowledgments

Thanks to [awesome-readme](https://github.com/matiassingers/awesome-readme) for the ReadMe-Template.
