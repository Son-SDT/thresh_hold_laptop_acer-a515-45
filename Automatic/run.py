import controller as ctl # file .py



def get_num():
    # Get the path to the config file
    file_path = f"{fc.get_current_dir()}/config.txt"
    
    try:
        # Open the file and read the contents
        with open(file_path, "r") as file:
            # Read the first line (assuming it contains the key-value pair)
            line = file.readline().strip()
            
            # Split the line into key and value
            if '=' in line:
                key, value = line.split('value_to_replace=', 1)
                # Convert the value to an integer
                number = int(value.strip())
            else:
                raise ValueError("Invalid format in config.txt")
    
    except Exception as e:
        # In case of any error (file not found, invalid format), use a default value
        print(f"Error reading {file_path}: {e}")
        number = 80
    
    # Ensure the number does not exceed 100
    if number > 99:
        number = 100
    
    return number

def is_not_full(goal):
    bat = fc.get_battery_percentage()
    if bat >= goal:
        return False
    else :
        return True
fc = ctl.function()





num = get_num()
while is_not_full(num) :
    battery = fc.get_battery_percentage()
    if not fc.check_plugin(): 
        print("Not plugging")
        break
    print(f"Battery: {battery}%")
    print(f"Charge from {battery}% to {num}%")
    mode = 1
    if mode != 0:
        print("Charging...")
        mode = fc.chargeto(num)
fc.set_battery_mode(1)
print(f"Battery: {fc.get_battery_percentage()}%")

