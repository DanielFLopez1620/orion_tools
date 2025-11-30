# ORION SLAM Tools

Package that integrates different SLAM configs and launches to use easily with ORION. This algorithms weren't made by the authors of this repository and they are rather calls and params modifications to enable SLAM applications with this robot.

## 📝 License

The source code is released under a [BSD 3 Clause license](/LICENSE)

**Author**: [Daniel Felipe López Escobar](https://github.com/DanielFLopez1620) and [Alejandro Bermúdez Fajardo](https://github.com/alexoberco).

The *orion_teleop* package has been tested under *ROS* Jazzy.

## 📚 Table of contents

- [🚀 Launch files](#-launch-files)
- [📚 Additional configurations](#-additional-configurations)

## 🚀 Launch files

### cartographer_launch

It uses [Cartographer SLAM](https://ros2-industrial-workshop.readthedocs.io/en/latest/_source/navigation/ROS2-Cartographer.html) integration for ROS 2 Jazzy, so you can achieve 2D SLAM with this algorithm in ORION, presented in the file [cartographer.launch.py](/orion_slam/launch/cartographer.launch.py).

~~~bash
# Basic usage:
# ros2 launch orion_slam cartographer.launch.py
# Additional args:
#   use_sim_time: Whether to use or not simulation clock
#   carto_config_dir: Lua config path for mapping
#   resolution: Floating number of resolution in meters
#   publish_period_sec: Floating number indicating refresh period of map
#   use_rviz: Whether to load or not visualization
ros2 launch orion_slam cartographer.launch.py
~~~

### occupancy_grid

Auxiliary launch for the cartographer slam oriented to load the occupancy grid manager, by calling the [occupancy_grid.launch.py](/orion_slam/launch/occupancy_grid.launch.py) file.

~~~bash
# Basic usage:
# ros2 launch orion_slam occupancy_grid.launch.py
# Additional args:
#   use_sim_time: Whether to use or not simulation clock.
#   resolution: Grid resolution in meters
#   publish_period_sec: Publish period in seconds
ros2 launch orion_slam occupancy_grid.launch.py
~~~

### slam_toolbox_mapper

Enables the usage of [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) with the ORION robot by launch the [slam_toolbox_mapper.launch.py](/orion_slam/launch/slam_toolbox_mapper.launch.py).

~~~bash
# Basic usage:
# ros2 launch orion_slam slam_toolbox_mapper.launch.py
# Additional args:
#   use_sim_time: Whether to use simulation clock.
#   use_gui: Whether or not to call the visualization.
#   autostart: Whether to start automatically or wait manual call.
#   use_lifecycle_manager: Enable bond connection during node activation
#   slam_params_file: Path to config file
~~~

## 📚 Additional configurations

You can set up the applications for your slam applications on the files of the [config](/orion_slam/config/) directory:

- For cartographer, modify [cartographer.lua](/orion_slam/config/cartographer.lua) and [occupancy_grid_params.yaml](/orion_slam/config/occupancy_grid_params.yaml).

- For slam_toolbox, modify the [online_async_mapper.yaml](/orion_slam/config/online_async_mapper.yaml)
