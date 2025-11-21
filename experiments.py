from main import *
import time

UAVS = ["SIMPLE_QUAD", "QUAD_PURPLE", "X8_DEFAULT", "X8", "X8_TEST"]
CONTROLLERS = ["PID", "PID", "TwoLayerMRAC", "TwoLayerMRAC", "MRAC"]
ADD_PAYLOAD = [False, False, False, True, True]
PAYLOAD_TYPE = ["two_steel_balls", "two_steel_balls", "two_steel_balls", "ten_steel_balls_in_two_lines", "many_steel_balls_in_random_position"]
SEQUENTIAL_DROP = [False, False, False, False, True]
SEQUENTIAL_DROP_START = [0, 0, 0, 0.5, 1]
INCLUDE_ENVIRONMENT = [False, True, False, False, False]
APPLY_MOTOR_FAILURE = [False, False, True, False, False]
MOTOR_FAILURE_TIME = [1, 0, 1, 0, 0]


for uav, controller, add_payload, payload_type, sequential_drop, sequential_drop_start, include_environment, apply_motor_failure, motor_failure_time in zip(UAVS, CONTROLLERS, ADD_PAYLOAD, PAYLOAD_TYPE, SEQUENTIAL_DROP, SEQUENTIAL_DROP_START, INCLUDE_ENVIRONMENT, APPLY_MOTOR_FAILURE, MOTOR_FAILURE_TIME):
    run_experiment(
        uav=uav,
        controller=controller,
        no_visualize=False,
        # no_wrapper_mode=True,
        simulation_duration=2,
        add_payload=add_payload,
        payload_type=payload_type,
        sequential_drop=sequential_drop,
        sequential_drop_start=sequential_drop_start,
        include_environment=include_environment,
        apply_motor_failure=apply_motor_failure,
        motor_failure_time=motor_failure_time,
    )
    time.sleep(.1)
