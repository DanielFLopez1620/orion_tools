from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    resolution = LaunchConfiguration('resolution', default='0.05')
    publish_period_sec= LaunchConfiguration('publish_period_sec', default='1.0')

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false',
                               description='Use simulation clock'),
        DeclareLaunchArgument('resolution', default_value=resolution,
                               description='Grid cell resolution'),
        DeclareLaunchArgument('publish_period_sec', default_value=publish_period_sec,
                               description='Periodo de publicación'),
        Node(package='cartographer_ros', executable='cartographer_occupancy_grid_node',
             name='cartographer_occupancy_grid_node', output='screen',
             parameters=[{'use_sim_time': use_sim_time}],
             arguments=['-resolution', resolution,
                        '-publish_period_sec', publish_period_sec], remappings=[
                ('odom', '/mobile_base_controller/odom')
            ]),
    ])
