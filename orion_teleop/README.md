ros2 run teleop_twist_keyboard teleop_twist_keyboard \
    --ros-args \
    -p stamped:=true \
    -p frame_id:="base_link" \
    --remap cmd_vel:=/mobile_base_controller
