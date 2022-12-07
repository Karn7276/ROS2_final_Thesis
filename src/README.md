# ROS2 Nodes for RC Car

The Robot Operating System (ROS) is a set of software libraries and tools that help you build robot applications. 
From drivers to state-of-the-art algorithms, and with powerful developer tools, ROS has what you need for your 
next robotics project. And it's all open source.

Please familiarize yourself with ROS2, before use! See https://docs.ros.org/en/foxy/Tutorials.html

## Description

You acquired this code:

```
lem_rc
└───cmake
└───external
└───ros2foxy
│   │   setup.sh
│   │   README.md
```
  

## Getting Started

### Prerequisites

You need to have [ROS2 Foxy installed](https://docs.ros.org/en/foxy/Installation.html) and the ```setup.bash``` must be in the directory ```/opt/ros/foxy/```. Also
you need to have [```Colcon``` installed](https://colcon.readthedocs.io/en/released/user/installation.html). 

### Dependencies

There are no further dependencies you need to install manually. Follow the instructions
in [Installing](###installing).


## Installing
```
───ros2foxy
│   │   setup.sh
│   │   README.md
```
when inside the direcory ```ros2foxy``` you need to run ```setup.sh``` as root, i.e. 

```
 sudo sh ./setup.sh
```

which will install everything you need to run all sensors. 

## Help

Contact the [Authors](##authors), but please make sure to make an effort before asking for help.

## Authors

Contributor names and contact info

Eric Schöneberg | [schoeneberg@eit.uni-kl.de](schoeneberg@eit.uni-kl.de)

## Version History

* Version 0.01
    * I really hope it works.

## License

I have not yet started on licences.

## Acknowledgments

Thanks to [awesome-readme](https://github.com/matiassingers/awesome-readme) for the ReadMe-Template.
