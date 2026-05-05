"""
Software License Agreement (BSD)

Redistribution and use in source and binary forms, with or without modification, are permitted provided that
the following conditions are met:
 * Redistributions of source code must retain the above copyright notice, this list of conditions and the
   following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
   following disclaimer in the documentation and/or other materials provided with the distribution.
 * Neither the name of Clearpath Robotics nor the names of its contributors may be used to endorse or promote
   products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WAR-
RANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, IN-
DIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE

From: https://github.com/ros2/teleop_twist_joy
Modified by: DanielFLopez1620
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


ARGS = [
    DeclareLaunchArgument(
        'joy_vel', default_value='/mobile_base_controller/cmd_vel',
        description="Topic to publish the Twist / Twist Stamped msg"),
    DeclareLaunchArgument(
        'joy_config', default_value='xbox',
        description="Select controller platform to choose the params",
        choices=['ps3', 'xbox']),
    DeclareLaunchArgument(
        'joy_dev', default_value='0',
        description="Number of USB device, for example, 0 in case of /dev/ttyUSB0"),
    DeclareLaunchArgument(
        'publish_stamped_twist', default_value='true',
        description="Whether to use stamped twist or not",
        choices=['true', 'false']),
    DeclareLaunchArgument('config_filepath', default_value=os.path.join(
            get_package_share_directory('orion_teleop'), 'config', 'joystick_config.yaml'),
            description="Path to the config file of the respective controller device"),
]

def generate_launch_description():
    """
    Modified launch file from the teleop_twist_joy focused on moving and using
    the ORION robot with a controller, by default a Xbox controller to
    interact with the /mobile_base_controller/cmd_vel topic.
    """

    ld = LaunchDescription(ARGS)

    ld.add_action(
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{
                'device_id': LaunchConfiguration('joy_dev'),
                'deadzone': 0.3,
                'autorepeat_rate': 20.0,
            }])
    )

    ld.add_action(
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy_node',
            parameters=[
                LaunchConfiguration('config_filepath'),
                {'publish_stamped_twist': LaunchConfiguration('publish_stamped_twist')}],
            remappings={('/cmd_vel', LaunchConfiguration('joy_vel'))},
            )
    )

    return ld
