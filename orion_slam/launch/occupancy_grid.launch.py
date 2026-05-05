from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

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

def generate_launch_description():
    ld = LaunchDescription(ARGS)

    ld.add_action(
        Node(package='cartographer_ros', executable='cartographer_occupancy_grid_node',
            name='cartographer_occupancy_grid_node', output='screen',
            parameters=[{
                 'use_sim_time': LaunchConfiguration('use_sim_time', default='false')}],
            arguments=[
                '-resolution', LaunchConfiguration('resolution'),
                '-publish_period_sec', LaunchConfiguration('publish_period_sec')],
            remappings=[
                ('odom', '/mobile_base_controller/odom')  # ros2_control diff_drive_controller topic
            ])
    )

    return ld
