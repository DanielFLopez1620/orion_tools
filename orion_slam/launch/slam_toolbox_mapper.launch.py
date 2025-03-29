from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    
    slam_package = 'slam_toolbox'
    orion_slam = 'orion_slam'

    filter_node = Node(
        package="laser_filters",
        executable="scan_to_scan_filter_chain",
        name="lidar_filter",
        parameters=[PathJoinSubstitution([FindPackageShare(orion_slam), "config", "laser_filter.yaml"])],
        remappings=[("scan", "/lidar/raw_scan"), ("scan_filtered", "/scan")]
    )

    slam_config = os.path.join(
                get_package_share_directory(orion_slam),'config','online_async_mapper.yaml')
    slam_toolbox = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(slam_package),'launch','online_async_launch.py')]), 
                launch_arguments={'use_sim_time': use_sim_time, 'slam_params_file': slam_config}.items()
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        filter_node,
        slam_toolbox    
    ])