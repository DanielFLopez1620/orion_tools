import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch_ros.actions import Node

ARGS = [
    DeclareLaunchArgument('use_sim_time', default_value='false',
        description='Use simulation clock'),
    DeclareLaunchArgument('carto_config_dir',
        default_value=os.path.join(
            get_package_share_directory('orion_slam'), 'config'),
        description='Lua config path'),
    DeclareLaunchArgument('configuration_basename',
        default_value='cartographer.lua',
        description='Lua name file'),
    DeclareLaunchArgument('resolution',
        default_value='0.05',
        description='Grid resolution'),
    DeclareLaunchArgument('publish_period_sec',
        default_value='1.0',
        description='Update period (seconds) of the grid'),
    DeclareLaunchArgument('use_rviz', default_value='true',
        description='Whether to visualize on rviz with the default config',
        choices=['true', 'false'])
]

def generate_launch_description():
    """
    Launch the configurations required to use Cartographer (ROS version) with
    the ORION robot to explore environments, create maps and get position of
    the robot by using this SLAM app
    """

    rviz_config_file = os.path.join(get_package_share_directory('orion_slam'),
        'rviz', 'cartographer_config.rviz')

    ld = LaunchDescription(ARGS)

    ld.add_action(
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
            arguments=[
                '-configuration_directory', LaunchConfiguration('carto_config_dir'),
                '-configuration_basename', LaunchConfiguration('configuration_basename')
            ],
            remappings=[
                ('odom', '/mobile_base_controller/odom'),
                ('scan', '/scan_filtered')
            ]
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [ThisLaunchFileDir(), '/occupancy_grid.launch.py']),
            launch_arguments={
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'resolution': LaunchConfiguration('resolution'),
                'publish_period_sec': LaunchConfiguration('publish_period_sec')}.items(),
        )
    )

    ld.add_action(
         Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
            condition=IfCondition(LaunchConfiguration('use_rviz')),
            output='screen'),
    )

    return ld
