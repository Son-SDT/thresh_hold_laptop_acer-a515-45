#!/bin/bash
source ~/.bashrc


# Get the directory containing the current script
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
# Log file for errors
LOG_FILE="$SCRIPT_DIR/autorun.log"  # Updated path to use username
# Read the Python path from the file
PYTHON_DIR=$(grep '^python_path=' $SCRIPT_DIR/config.txt | cut -d'=' -f2)
log_with_timestamp "Python directory: $PYTHON_DIR"

$PYTHON_DIR $SCRIPT_DIR/clean_file_log.py


# Function to log with timestamp
log_with_timestamp() {
    local message="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $message" >> $LOG_FILE
}




# Run the Python script to clean the file log and log any errors
{
    
    log_with_timestamp "Running clean_file_log.py..."
    log_with_timestamp "clean_file_log.py completed."
} 2>&1 | while IFS= read -r line; do log_with_timestamp "$line"; done

while true
do
source ~/.bashrc

log_with_timestamp "Python directory: $PYTHON_DIR"
log_with_timestamp "Current script directory: $SCRIPT_DIR"

# Path to Python files

# Insert kernel module and log any errors
{
    log_with_timestamp "Inserting kernel module..."
    sudo insmod $SCRIPT_DIR/acer-wmi-battery/acer-wmi-battery.ko
    log_with_timestamp "Kernel module inserted successfully."
} 2>&1 | while IFS= read -r line; do log_with_timestamp "$line"; done

# Infinite loop to ensure run.py restarts if it crashes
    {
        log_with_timestamp "Starting run.py..."
        # Run the Python script using Anaconda Python
        $PYTHON_DIR $SCRIPT_DIR/run.py
        log_with_timestamp "$PYTHON_DIR $SCRIPT_DIR/run.py"
        # Check if run.py exited normally
        if [ $? -ne 0 ]; then
            log_with_timestamp "run.py crashed with an error. Restarting..."
        fi
    } 2>&1 | while IFS= read -r line; do log_with_timestamp "$line"; done

    # Wait for 5 seconds before restarting
    sleep 5
    echo "--------------------------------------------------------------" >> $LOG_FILE
done

