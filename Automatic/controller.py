import psutil
import math
import subprocess
import time
import os

class function():
    def __init__(self):
        pass
    
    def run_cmd(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                print("Error:", result.stderr)
        except Exception as e:
            print("An error occurred:", e)

    def set_battery_mode(self, mode):
        self.run_cmd(f"echo {mode} | sudo tee /sys/bus/wmi/drivers/acer-wmi-battery/health_mode &")
            
    def get_battery_percentage(self):
        battery_get = psutil.sensors_battery()
        percent = battery_get.percent
        return math.floor(percent)
    
    def check_plugin(self):
        self.set_battery_mode(0)
        self.count(10)
        battery_get = psutil.sensors_battery()
        plugged = battery_get.power_plugged
        self.set_battery_mode(1)
        return plugged

    def check_battery(self, bat, x, output):
        if self.check_plugin():
            if bat >= x and output != 1:
                output = self.set_battery_mode(1)
                return False, output
            elif bat < x and output != 0:
                output = self.set_battery_mode(0)
                return True, output
            else:
                self.set_battery_mode(1)
                return False, output  # Always return two values
        else:
            return False, output
    
    def chargeto(self, x):
        output = 1
        battery = self.get_battery_percentage()
        check, output = self.check_battery(battery, x, output)
        
        while check:
            if x - battery <= 1:
                seconds = 30
            else:
                seconds = 60
            
            if self.count(seconds) :
                battery = self.get_battery_percentage()
                print(f"battery : {battery}%")
                check, output = self.check_battery(battery, x, output)
                
            if not check:
                break
    
    def count(self, seconds=60):
        time.sleep(seconds)
        return True
    def get_file_path(self):
        return os.path.abspath(__file__)
    def get_current_dir(self):
        path = self.get_file_path()
        return os.path.dirname(path)

function().get_current_dir()