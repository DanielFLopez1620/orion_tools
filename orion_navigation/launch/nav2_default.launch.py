# Copyright 2022 Clearpath Robotics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Roni Kreinin (rkreinin@clearpathrobotics.com)
# Modified by DanielFLopez1620.


import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    GroupAction,
    IncludeLaunchDescription,
    OpaqueFunction
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import PushRosNamespace, SetRemap, Node

ARGUMENTS = [
    DeclareLaunchArgument('use_sim_time', default_value='true',
        choices=['true', 'false'], description='Use sim time'),
    DeclareLaunchArgument('namespace', default_value='',
        description='Robot namespace'),
    DeclareLaunchArgument('map',
        default_value=os.path.join(
            get_package_share_directory('orion_navigation'),
            'maps',
            'map.yaml'
            ),
        description='Full path to map yaml file to load'),
    DeclareLaunchArgument(
        'params_file',
        default_value=os.path.join(get_package_share_directory('orion_navigation'),
                                   'config',
                                   'nav2_config.yaml'),
        description='Full path to the ROS 2 parameters file to use for all launched nodes')
]


def generate_launch_description():
    ld = LaunchDescription(ARGUMENTS)

    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')
    diff_robot_nav_pkg =get_package_share_directory('orion_navigation')
    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = LaunchConfiguration('params_file')
    map_file = LaunchConfiguration('map')

    rviz_config_dir = os.path.join(diff_robot_nav_pkg, 'rviz', 'nav2_default.rviz')

    nav2 = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(pkg_nav2_bringup, 'launch', 'bringup_launch.py')),
     launch_arguments=[
                  ('map', map_file),
                  ('use_sim_time', use_sim_time),
                  ('params_file', params_file),
                  ('autostart', 'False'),  # Lifecycle nodes must be activated manually via rviz2 or lifecycle manager
                ]
    )
    
    ld.add_action(nav2)
    ld.add_action(
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': True}],
        ),
    )

    return ld