import enum

class Commands(enum.IntFlag):
    ROSCORE = enum.auto()
    CAMERA_INTRINSIC = enum.auto()
    CAMERA_EXTRINSIC = enum.auto()
    LANE_DETECT = enum.auto()
    DRIVING = enum.auto()
    CAMERA_PUBLISH = enum.auto()
    PI_BRINGUP = enum.auto()
    
class Com_Options(enum.IntEnum):
    START = enum.auto()
    STOP = enum.auto()
    RESTART = enum.auto()
    MODIFY = enum.auto()
    

command_map = {Commands.ROSCORE: {"command":"roscore", "options":{}},
               Commands.CAMERA_INTRINSIC: {"command":"roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch", "options":{"mode": "action"}},
               Commands.CAMERA_EXTRINSIC: {"command":"roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch", "options":{"mode": "action"}},
               Commands.LANE_DETECT: {"command":"roslaunch turtlebot3_autorace_detect detect_lane.launch", "options":{"mode": "action"}},
               Commands.DRIVING: {"command":"roslaunch turtlebot3_autorace_driving turtlebot3_autorace_control_lane.launch",
                                "options":{ "b_delta_y": 300, 
                                            "b_delta_w": 300,
                                            "cutoff":-1,
                                            "delta_w": 5,
                                            "delta_y": 20,
                                            "custom_cutoff": False,
                                            "short_thresh": 550
                                          }},
               
               Commands.CAMERA_PUBLISH: {"command":"roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch", "options":{"rate":20}},
               Commands.PI_BRINGUP: {"command":"roslaunch turtlebot3_bringup turtlebot3_robot.launch", "options":{}}
               }
    

