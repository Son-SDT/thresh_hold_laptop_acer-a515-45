import controller as ctl
fc = ctl.function()


current_dir = fc.get_current_dir()
python_path = fc.run_cmd("which python")
set = f'{python_path} {current_dir}/set_threshold.py'
set = set.replace("\n","")
alias = f"alias set='{set}'"


cmd = f"""
sudo apt install build-essential linux-headers-$(uname -r) git\n
git clone https://github.com/frederik-h/acer-wmi-battery.git\n
cd acer-wmi-battery\n
make\n
pip install psutil\n
(sudo crontab -l 2>/dev/null; echo "@reboot {current_dir}/autorun.sh") | sudo crontab -\n
chmod 777 {current_dir}/autorun.sh\n
sudo insmod {current_dir}/acer-wmi-battery/acer-wmi-battery.ko\n
echo 'son ALL=(ALL) NOPASSWD: /usr/bin/tee, /sys/bus/wmi/drivers/acer-wmi-battery/health_mode' | sudo EDITOR='tee -a' visudo

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




