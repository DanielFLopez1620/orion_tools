import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    config_dir   = LaunchConfiguration('carto_config_dir', default=os.path.join(
                     get_package_share_directory('orion_slam'), 'config'))
    lua_file     = LaunchConfiguration('configuration_basename', default='cartographer.lua')
    resolution   = LaunchConfiguration('resolution', default='0.05')
    publish_sec  = LaunchConfiguration('publish_period_sec', default='1.0')
    use_rviz = LaunchConfiguration('use_rviz', default='true')

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false',
                               description='Use simulation clock'),
        DeclareLaunchArgument('carto_config_dir', default_value=config_dir,
                               description='Ruta de configs Lua'),
        DeclareLaunchArgument('configuration_basename', default_value=lua_file,
                               description='Nombre de archivo Lua'),
        Node(package='cartographer_ros', executable='cartographer_node',
             name='cartographer_node', output='screen',
             parameters=[{'use_sim_time': use_sim_time}],
             arguments=['-configuration_directory', config_dir,
                        '-configuration_basename', lua_file]),
        DeclareLaunchArgument('resolution', default_value=resolution,
                               description='Resolución del grid'),
        DeclareLaunchArgument('publish_period_sec', default_value=publish_sec,
                               description='Periodo de publicación del grid'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [ThisLaunchFileDir(), '/occupancy_grid.launch.py']),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'resolution': resolution,
                'publish_period_sec': publish_sec}.items(),
        ),

         Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            parameters=[{'use_sim_time': use_sim_time}],
            condition=IfCondition(use_rviz),
            output='screen'),
    ])
