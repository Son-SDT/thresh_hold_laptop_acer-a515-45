import controller as ctl
import os
fc = ctl.function()

def replace_value_in_file(file_path, path):
    try:
        # Read the current content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace the value in the content
        with open(file_path, 'w') as file:
            for line in lines:
                # Replace the placeholder with the given number
                if 'python_path=' in line:
                    line = f'python_path={path}'
                file.write(line)
                
    except Exception as e:
        print(f"An error occurred: {e}")



username = os.getlogin()
current_dir = fc.get_current_dir()
python_path = fc.run_cmd("which python")
set = f'{python_path} {current_dir}/set_threshold.py'
set = set.replace("\n","")
alias = f"alias set='{set}'"
config_file = f"{fc.get_current_dir()}/config.txt"
replace_value_in_file(config_file,python_path)





cmd = f"""
sudo apt install build-essential linux-headers-$(uname -r) git\n
git clone https://github.com/frederik-h/acer-wmi-battery.git\n
cd acer-wmi-battery\n
make\n
pip install psutil\n
(sudo crontab -l; echo "@reboot {current_dir}/autorun.sh > {current_dir}/autorun_crontab.log 2>&1") | sudo crontab - \n
chmod + x {current_dir}/autorun.sh\n
echo '{username} ALL=(ALL) NOPASSWD: /usr/bin/tee, /sys/bus/wmi/drivers/acer-wmi-battery/health_mode' | sudo EDITOR='tee -a' visudo
echo '{username} ALL=(ALL) NOPASSWD: /sbin/insmod, {current_dir}/acer-wmi-battery/acer-wmi-battery.ko' | sudo EDITOR='tee -a' visudo

"""



Guide = """\n
The process will be auto-runned \n
Set thereshold: set <number> \n
Ex: set 80 # it will set the threshold to 80\n
Setup complete. Please restart your terminal or run 'source ~/.bashrc' to apply the alias.
"""
fc.run_cmd(cmd)
fc.run_cmd(alias)
print(Guide)




