# ORION Navigation Tools

Package that integrates a basic implementation of Nav2 for autonomous navigation through manual waypoints on RViz2.

## 📝 License

The source code is released under a [BSD 3 Clause license](/LICENSE)

**Author**: [Daniel Felipe López Escobar](https://github.com/DanielFLopez1620).

The *orion_navigation* package has been tested under *ROS* Jazzy.

## 📚 Table of contents

- [🚀 Launch files](#-launch-files)
- [📚 Additional configurations](#-additional-configurations)

## 🚀 Launch files

### nav2_default

Launches the [nav2_bringup](https://index.ros.org//p/nav2_bringup/) package under a compatible configuration for ORION with the visualization node.

> **Note:** Nav2 lifecycle nodes start inactive (`autostart: false`). After launch, activate them manually from the RViz2 *Lifecycle Manager* panel or via `ros2 lifecycle`.

> **Note:** A pre-built map file is required for navigation. Generate one first with `orion_slam`.

~~~bash
# Basic usage:
ros2 launch orion_navigation nav2_default.launch.py
# Additional args:
#   - use_sim_time: Whether or not to use simulation clock (default: true)
#   - namespace:   Robot namespace (default: '')
#   - map:         Full path to the map yaml file (default: maps/map.yaml)
#   - params_file: Full path to the nav2 config yaml file
~~~

## 📚 Additional configurations

Tune the Nav2 stack by editing [config/nav2_config.yaml](/orion_navigation/config/nav2_config.yaml). Key sections:

- **amcl** — localization particle filter parameters
- **controller_server / FollowPath** — DWB local planner velocity and critic weights
- **local_costmap / global_costmap** — obstacle layer and inflation radius
- **behavior_server** — spin, backup, and recovery behavior limits
