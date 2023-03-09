import socketserver
import sys
import subprocess
import pickle
import os
import data_structures as ds
from data_structures import Commands, Command, Host
from flask import Flask, render_template, request

app = Flask(__name__)


command_map_path = "command_map.pick"
command_map: dict[Commands, Command] = None

if os.path.exists(command_map_path):
    with open(command_map_path, "rb") as com_pick:
        command_map = pickle.load(com_pick)
else:
    command_map = {Commands.ROSCORE: Command(Host.ROS, "roscore"),
                    Commands.CAMERA_INTRINSIC: Command(Host.ROS, "roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch").make_option("mode", "action"),
                    Commands.CAMERA_EXTRINSIC: Command(Host.ROS, "roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch").make_option("mode", "action"),
                    Commands.LANE_DETECT: Command(Host.ROS, "roslaunch turtlebot3_autorace_detect detect_lane.launch").make_option("mode", "action"),
                    Commands.TRAFFIC_DETECT: Command(Host.ROS, "roslaunch turtlebot3_autorace_detect detect_traffic_light.launch").make_option("mode", "action"),
                    Commands.DRIVING: Command(Host.ROS, "roslaunch turtlebot3_autorace_driving turtlebot3_autorace_control_lane.launch")\
                                .make_option("b_delta_y", 300).make_option("b_delta_w", 300).make_option("cutoff", -1)\
                                .make_option("delta_w", 5).make_option("delta_y", 20).make_option("custom_cutoff", False)\
                                .make_option("short_thresh", 550),
                    Commands.CAMERA_PUBLISH: Command(Host.TURTLEBOT, "roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch").make_option("rate", 20),
                    Commands.PI_BRINGUP: Command(Host.TURTLEBOT, "roslaunch turtlebot3_bringup turtlebot3_robot.launch")
                    }

@app.route("/")
def index():
	# Read GPIO Status
	buttonSts = GPIO.input(button)
	senPIRSts = GPIO.input(senPIR)
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	ledGrnSts = GPIO.input(ledGrn)
	templateData = {
      		'button'  : buttonSts,
      		'senPIR'  : senPIRSts,
      		'ledRed'  : ledRedSts,
      		'ledYlw'  : ledYlwSts,
      		'ledGrn'  : ledGrnSts,
      	}
	return render_template('index.html', **templateData)
	
@app.route("/<deviceID>/<action>")
def action(deviceID, action):
	command_map[deviceID]
   
	# if action == "on":
	# 	GPIO.output(actuator, GPIO.HIGH)
	# if action == "off":
	# 	GPIO.output(actuator, GPIO.LOW)
		     
	# buttonSts = GPIO.input(button)
	# senPIRSts = GPIO.input(senPIR)
	# ledRedSts = GPIO.input(ledRed)
	# ledYlwSts = GPIO.input(ledYlw)
	# ledGrnSts = GPIO.input(ledGrn)
   
	# templateData = {
	#  	'button'  : buttonSts,
    #   		'senPIR'  : senPIRSts,
    #   		'ledRed'  : ledRedSts,
    #   		'ledYlw'  : ledYlwSts,
    #   		'ledGrn'  : ledGrnSts,
	# }
	# return render_template('index.html', **templateData)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
