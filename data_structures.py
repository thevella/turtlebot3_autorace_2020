import enum
import subprocess
from time import sleep

class Commands(enum.IntFlag):
    ROSCORE = enum.auto()
    CAMERA_INTRINSIC = enum.auto()
    CAMERA_EXTRINSIC = enum.auto()
    LANE_DETECT = enum.auto()
    TRAFFIC_DETECT = enum.auto()
    DRIVING = enum.auto()
    CAMERA_PUBLISH = enum.auto()
    PI_BRINGUP = enum.auto()
    
class Com_Options(enum.IntEnum):
    START = enum.auto()
    STOP = enum.auto()
    RESTART = enum.auto()
    MODIFY = enum.auto()
    
class Command_State(enum.IntEnum):
    RUNNING = enum.auto()
    STOPPED = enum.auto()
    FAILED = enum.auto()
    
class Host(enum.Enum):
    TURTLEBOT = "172.26.181.111",
    ROS = "172.26.108.68"

class Command:
    base_command :str = ""
    options :dict = {}
    command : subprocess.Popen = None
    host : Host = None
    
    def __init__(self, host, base_command = "", options = {}):
        self.host = host
        
        self.options = options
            
        self.base_command = base_command
    
    
    def make_option(self, name, value, line_opt=True):
        self.options[name] = {'value': value, 'line_opt': line_opt}
        return self
    
    def update_options(self, name, value, line_opt = False):
        if name in self.options:
            self.options[name]['value'] = value
            
            if not self.options[name]['line_opt']:
                self.update_arg(name)
                
        else:
            self.make_option(name, value, line_opt)
                
    
    def check_state(self) -> Command_State:
        if self.command is None:
            return Command_State.STOPPED
            
        if self.command.poll() is None:
            return Command_State.RUNNING
        
        return Command_State.FAILED
    
    def build_command(self) -> str:
        com = self.base_command
        
        for name, fts in self.options.items():
            if fts['line_opt']:
                com += " {}:={}".format(name, fts['value'])
        
        return com
    
    def update_arg(self, name):
        if name in self.options and not self.options[name]['line_opt']:
            subprocess.call("rosparam set '{}' '{}'".format(name, self.options[name]['value']))
    
    def update_args(self):
        for name, fts in self.options.items():
            if not fts['line_opt']:
                self.update_arg(name)
        
    
    def start(self):
        state = self.check_state()
        
        if state == Command_State.RUNNING:
            return
        
        if state == Command_State.FAILED:
            self.command.terminate()
        
        self.command = subprocess.Popen(self.build_command())
        
        
        if any([ fts['line_opt'] == False for name, fts in self.options.items() ]):
            sleep(15)
        
            self.update_args()
        
        
    def restart(self):
        state = self.check_state()
        
        if state == Command_State.RUNNING:
            self.stop()
            self.start()
            return
        
        if state == Command_State.FAILED or state == Command_State.STOPPED:
            self.start()
            return
        

    def stop(self):
        state = self.check_state()
        
        if state == Command_State.STOPPED:
            return
        
        self.command.kill()
        self.command = None
        
    def __str__(self) -> str:
        r = {self.base_command: {"options": self.options, "state":self.check_state().name}}
        
        return str(r)


command_name_map = {Commands.ROSCORE: "Roscore",
                    Commands.CAMERA_INTRINSIC: "Intrinsic Calibration",
                    Commands.CAMERA_EXTRINSIC: "Extrinsic Calibration",
                    Commands.LANE_DETECT: "Lane Detection",
                    Commands.TRAFFIC_DETECT: "Traffic Detection",
                    Commands.DRIVING: "Driving Control",
                    Commands.CAMERA_PUBLISH: "Publish Camera",
                    Commands.PI_BRINGUP: "Bringup Controls"
                    
                    }



    
    
    
    
    
    
    
    