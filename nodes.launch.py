import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a7817f49a52d7366ae925a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7817f49a52d7366ae925a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781b249a52d7366ae92a8","source_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a7818749a52d7366ae9265",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7818749a52d7366ae9265",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781b449a52d7366ae92ab","source_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a7818949a52d7366ae926a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7818949a52d7366ae926a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781b549a52d7366ae92ae","source_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69a7818149a52d7366ae925f",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7818149a52d7366ae925f",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781b049a52d7366ae92a5","source_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_n69a7818b49a52d7366ae926f",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7818b49a52d7366ae926f",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e71bcd15153dec61d7f8:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3e71bcd15153dec61d7f8:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3e71bcd15153dec61d7f8:encoder_left","name":"encoder_left","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3e71bcd15153dec61d7f8:encoder_right","name":"encoder_right","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:odometry","name":"odometry","direction":"output","msg_type":"nav_msgs/Odometry"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781a649a52d7366ae9296","source_node_id":"69a781a349a52d7366ae9292","source_pin_id":"encoder_state","target_pin_id":"encoder_right"},{"connection_id":"69a781a749a52d7366ae9299","source_node_id":"69a7819f49a52d7366ae928c","source_pin_id":"encoder_state","target_pin_id":"encoder_left"},{"connection_id":"69a781a949a52d7366ae929c","source_node_id":"69a7819149a52d7366ae927a","source_pin_id":"mode","target_pin_id":"mode"},{"connection_id":"69a781ab49a52d7366ae929f","source_node_id":"69a7819349a52d7366ae927f","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a781ae49a52d7366ae92a2","source_node_id":"69a7819549a52d7366ae9284","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781b049a52d7366ae92a5","target_node_id":"69a7818149a52d7366ae925f","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69a781b249a52d7366ae92a8","target_node_id":"69a7817f49a52d7366ae925a","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69a781b449a52d7366ae92ab","target_node_id":"69a7818749a52d7366ae9265","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69a781b549a52d7366ae92ae","target_node_id":"69a7818949a52d7366ae926a","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="logger",
            executable="logger_node",
            name="logger_n69a7818f49a52d7366ae9275",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7818f49a52d7366ae9275",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"log_file":"","log_to_stdout":true}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_n69a7819549a52d7366ae9284",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7819549a52d7366ae9284",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e702cd15153dec61d7da:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3e702cd15153dec61d7da:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3e702cd15153dec61d7da:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781ae49a52d7366ae92a2","target_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="mission_runner",
            executable="mission_runner_node",
            name="mission_runner_n69a7819349a52d7366ae927f",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7819349a52d7366ae927f",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"mission":[],"linear_speed":0.5,"angular_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":10,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a4851d5722fce47266b4f1:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a4851d5722fce47266b4f1:status","name":"status","direction":"output","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781ab49a52d7366ae929f","target_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_n69a7819149a52d7366ae927a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7819149a52d7366ae927a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"stopped","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e74fcd15153dec61d870:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3e74fcd15153dec61d870:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781a949a52d7366ae929c","target_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_n69a7819f49a52d7366ae928c",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a7819f49a52d7366ae928c",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e733cd15153dec61d834:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3e733cd15153dec61d834:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781a749a52d7366ae9299","target_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"encoder_state","target_pin_id":"encoder_left"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_n69a781a349a52d7366ae9292",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a781a349a52d7366ae9292",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e733cd15153dec61d834:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3e733cd15153dec61d834:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a781a649a52d7366ae9296","target_node_id":"69a7818b49a52d7366ae926f","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
            }
        ),
        Node(
            package="camera",
            executable="camera_node",
            name="camera_n69a79a0549a52d7366ae94ab",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a79a0549a52d7366ae94ab",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"camera_id":"camera_0","device_index":0,"width":640,"height":480,"fps":30}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":30,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e728cd15153dec61d816:capture","name":"capture","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3e728cd15153dec61d816:frame","name":"frame","direction":"output","msg_type":"polyflow_msgs/CameraFrame"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
    ])