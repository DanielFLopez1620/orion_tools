cmake_minimum_required(VERSION 3.8)
project(orion_slam)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(slam_toolbox REQUIRED)
find_package(cartographer_ros REQUIRED)
find_package(cartographer_ros_msgs REQUIRED)

install(
  DIRECTORY launch config rviz
  DESTINATION share/${PROJECT\_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
