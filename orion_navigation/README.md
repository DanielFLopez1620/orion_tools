# ORION Navigation Tools

Package that integrates a basic implementation of Nav2 for autonomous navigation through manual waypoints on RViz2.

## 📝 License

The source code is released under a [BSD 3 Clause license](/LICENSE)

**Author**: [Daniel Felipe López Escobar](https://github.com/DanielFLopez1620).

The *orion_teleop* package has been tested under *ROS* Jazzy.

## 📚 Table of contents

- [🚀 Launch files](#-launch-files)
- [📚 Additional configurations](#-additional-configurations)

## 🚀 Launch files

### nav2_default

Launches the [nav2_bringup](https://index.ros.org//p/nav2_bringup/) package under a compatible configuration for ORION with the visualization node.

~~~bash
# Basic usage:
# ros2 launch orion_navigation nav2_default.launch.py
# Additional args:
#   - use_sim_time: Whether or not to use simulation clock
#   - namespace: Robot namespace
#   - map: Path to the map file
#   - params_file: Path to the nav2 config file.
#   - use_namespace: Whether or not to apply namespace to nav stack
#   - slam: Whether or not to run SLAM.
#   - autostart: To indicate if it starts automatically the nav2 stack
#   - use_composition: To use composed bringup
#   - use_respawn: Whether to try respawn if a node fails
#   - log_level: Info, debug or error.
#   - use_lifecycle_manager: Enable bond connection
#   - use_localization: To enable localization or not.
#   - slam_params_file: Path to slam config under slam_toolbox/config dir.
#   - container_name: Name of the container if composition is enabled.
~~~

