#   Notice:
# 0 is charge and 1 is uncharge

# your command : python directory-of-chargeto.py your-percentage-here
# ex: python /home/son/chargeto.py 80

# you can set alias for "python chargeto.py": 
# echo "alias short-name='python directory-of-chargeto.py'" >> ~/.bash
# then the command : short-name your-percentage-here

import sys
import psutil,math
import subprocess,time


def run_cmd(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            '''print("Command executed successfully.")
            print("Output:")
            print(result.stdout)'''
            return result.stdout
        else:
            print("Error:", result.stderr)
    except Exception as e:
        print("An error occurred:", e)
def set_battery_mode(mode):
    run_cmd(f"echo {mode} | sudo tee /sys/bus/wmi/drivers/acer-wmi-battery/health_mode &")
        
def get_battery_percentage():
    battery_get = psutil.sensors_battery()
    
    percent = battery_get.percent
    return math.floor(percent)
def check_plugin():
    battery_get = psutil.sensors_battery()
    plugged = battery_get.power_plugged
    return plugged

def check_battery(bat,x,output):
    if bat >= x and output !=1 :
        output = set_battery_mode(1)
        return False,output
    elif bat <x and output !=0 :
        output = set_battery_mode(0)
        return True,output
    else:
        set_battery_mode(1)
        return False
def count(seconds=60):
    for i in range(seconds, 0, -1):
        time.sleep(1)
    return i
def chargeto(x):
    output = 1
    battery = get_battery_percentage()
    check,output = check_battery(battery,x,output)
    while check:
        if x-battery <= 1 : seconds = 30 
        else : seconds = 60
        if count(seconds) == 1:
            battery = get_battery_percentage()
            print(f"battery : {battery}%")
            check,output = check_battery(battery,x,output)
        if check == False:
                output = 1
                break
    return output
        
if __name__ == "__main__":
    try :
        try:
            x = int(sys.argv[1])
        except:
            x=80
        getbat = get_battery_percentage()
        if getbat < x and x<=100:
            set_battery_mode(0)
            print("Checking...")
            count(5)
            if check_plugin() :
                print("Pluged")
                print(f"Charging from {getbat}% to {x}%")
                chargeto(x)
            else:
                set_battery_mode(1)
                print("Unpluged")
        else:
            if getbat == x :
                print(f"Your battery is {getbat}")
            else:
                print(f"Your battery {getbat}% over {x}%")
            set_battery_mode(1)
            pass
    except :
        set_battery_mode(1)
        
# 0 is charge and 1 is uncharge
