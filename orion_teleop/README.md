# ORION Teleoperation

Package oriented for teleoperation of the ORION robot by using a controller or keyboard.

## 📝 License

The source code is released under a [BSD 3 Clause license](/LICENSE)

**Author**: [Daniel Felipe López Escobar](https://github.com/DanielFLopez1620).

The *orion_teleop* package has been tested under *ROS* Jazzy.

## 📚 Table of contents

- [🚀 Launch files](#-launch-files)
- [🧩 Additional utilities](#-additional-utilities)

## 🚀 Launch files

### 🎮 Joystick stamped

Launch the **joy node** and the **teleop joy node** set up for the Xbox Controller, in order to teleoperate the robot by using **Stamped Twist** messages.

~~~bash
# Basic usage:
# ros2 launch orion_teleop joystick_stamped.launch.py
# Additional arguments:
#  joy_vel: Topic name, by default /mobile_base_controller/cmd_vel
#  joy_config: Select the platform, can be ps3 or xbox (xbox by default)
#  joy_dev: Device/port of the controller, by default 0 for /dev/ttyUSB0
#  publish_stamped_twist: true for using Twist Stamped messages
#  config_filepath: Path ot search for the config under teleop_twist_joy/config
ros2 launch orion_teleop joystick_stamped.launch.py
~~~

## 🧩 Additional utilities

You can run the teleop for keyboard by using the next command:

~~~bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard \
    --ros-args \
    -p stamped:=true \
    -p frame_id:="base_link" \
    --remap cmd_vel:=/mobile_base_controller
~~~
