RPLIDAR ROS package
=====================================================================

ROS node and test application for RPLIDAR

Visit following Website for more details about RPLIDAR:

rplidar roswiki: http://wiki.ros.org/rplidar

rplidar HomePage:   http://www.slamtec.com/en/Lidar

rplidar SDK: https://github.com/Slamtec/rplidar_sdk

rplidar Tutorial:  https://github.com/robopeak/rplidar_ros/wiki

How to build rplidar ros package
=====================================================================

1) Clone this project to your colcon workspace src folder
2) Install ROS2 foxy and colcon compiler.


```
cd [your-ros-package-directory]/src

git clone git@github.com:babakhani/rplidar_ros2.git

cd [your-ros-package-directory]

colcon build --symlink-install

source ./install/setup.bash
```

Check if package exist

```
ros2 pkg list | grep rplidar
```

I. Run rplidar node and view in the rviz
------------------------------------------------------------

```
ros2 launch rplidar_ros view_rplidar.launch.py
```
The topic list should contain

```
/parameter_events
/rosout
/scan
/initialpos
.....
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

Thanks to (https://git@github.com:babakhani/rplidar_ros2.git-readme) for the ReadMe-Template.
