# ////////////////////////// IMPORT LIBRARIES AND REQUIREMENTS ////////////////
# ------------------------------ LAUNCH DEPENDENCIES --------------------------
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

# ///////////////////////////// GLOBAL DEFINITIONS ///////////////////////////
ARGS = [
    DeclareLaunchArgument('use_sim_time',
        default_value='false',
        description='Use simulation clock',
        choices=['false', 'true']),
    DeclareLaunchArgument('resolution', 
        default_value='0.05',
        description='Grid cell resolution'),
    DeclareLaunchArgument('publish_period_sec', 
        default_value='1.0',
        description='Publish period in seconds'),
]
# ///////////////////////////// LAUNCH DESCRIPTION ///////////////////////////
def generate_launch_description():
    # Start launch description and load arguments
    ld = LaunchDescription(ARGS)
    
    # Add occupancy grid carto node
    ld.add_action(
        Node(package='cartographer_ros', executable='cartographer_occupancy_grid_node',
            name='cartographer_occupancy_grid_node', output='screen',
            parameters=[{
                 'use_sim_time': LaunchConfiguration('use_sim_time', default='false')}],
            arguments=[
                '-resolution', LaunchConfiguration('resolution'),
                '-publish_period_sec', LaunchConfiguration('publish_period_sec')], 
            remappings=[
                ('odom', '/mobile_base_controller/odom')
            ])
    )

    # Return launch description
    return ld
