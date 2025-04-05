import os

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

ARGS = [
    DeclareLaunchArgument('use_sim_time', default_value='false',
        description='Use sim time if true'),
    DeclareLaunchArgument('use_gui', default_value='true',
        description="Use RViz to visualize SLAM in real time")
]


def generate_launch_description():
    # Generate launch description
    ld = LaunchDescription(ARGS)
    
    # 
    slam_package = 'slam_toolbox'
    orion_slam = 'orion_slam'
    slam_config = os.path.join(
        get_package_share_directory(orion_slam),'config','online_async_mapper.yaml')
    rviz_config_file = os.path.join(orion_slam, 'rviz', 'slam_config.rviz')

    # Include launch for slam_toolbox
    ld.add_action(
        IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(slam_package),'launch','online_async_launch.py')]), 
        launch_arguments={'use_sim_time': LaunchConfiguration('use_sim_time'), 
                          'slam_params_file': slam_config}.items()
        )
    )

    # Add Rviz2 node
    ld.add_action(
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen',
            condition=IfCondition(LaunchConfiguration('use_gui'))
        )
    )

    # Return launch description
    return ld