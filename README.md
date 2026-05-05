# ORION Tools

Additional tools you can integrate with ORION robot, for example, SLAM, Autonomous Navigation and Teleoperation.

## 📝 License

The source code is released under a [BSD 3 Clause license](/LICENSE)

**Current fork maintened by:** [Daniel Felipe López Escobar](https://github.com/DanielFLopez1620).

**Originally developed by**: [Daniel Felipe López Escobar](https://github.com/DanielFLopez1620), [Miguel Ángel Gonzalez Rodriguez](https://github.com/miguelgonrod), and [Alejandro Bermúdez Fajardo](https://github.com/alexoberco).

The ORION Tools packages have been tested under [ROS](https://www.ros.org/) **Jazzy** distribution.

## 📚 Table of contents

- [📦 Repository Summary](#-repository-summary)
- [📥 Installation](#-installation)

## 📦 Repository Summary

This repository contains the next ROS 2 packages:

- 🧭[orion_navigation](/orion_navigation/README.md)🗺️ Simple implementation of the Nav2 Toolkit with ORION for autonomous navigation.
- 🗺️[orion_slam](/orion_slam/README.md)📡 Integration of SLAM (with slam_toolbox and cartographer) for ORION robot.
- 🎮[orion_teleop](/orion_teleop/README.md)🕹️ Implementation of stamped teleoperation with keyboard or Xbox Controller for the ORION robot.

## 📥 Installation

Follow the next step to use these packages:

1. Complete the installation of [orion_commons](https://github.com/Tesis-ORION/orion_common/blob/main/README.md).

2. (Optional) Install the simulation package for the robot on [orion_gz](https://github.com/Tesis-ORION/orion_gz).

3. Clone this repository:

    ~~~bash
    cd ~/ros2_ws/src
    git clone https://github.com/Tesis-ORION/orion_tools
    ~~~

4. Install dependencies:

    ~~~bash
    sudo apt update
    sudo apt install python3-rosdep -y
    cd ~/ros2_ws
    sudo rosdep init  # Only needed once per system; skip if already initialized
    rosdep update
    rosdep install --from-paths src --ignore-src -r -y
    ~~~

5. Compile and build:

    ~~~bash
    cd ~/ros2_ws
    colcon build --packages-select orion_navigation orion_slam orion_teleop
    source install/setup.bash
    ~~~

6. You are ready to use the packages.
