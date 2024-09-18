#!/bin/bash

# Get the directory containing the current script
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
PYTHON_DIR=$(which python)
echo "Current script directory: $SCRIPT_DIR" | tee -a /autorun.log

# Path to Python files

# Log file for errors
LOG_FILE="autorun.log"

# # Insert kernel module and log any errors
# {
#     echo "$(date '+%Y-%m-%d %H:%M:%S') - Inserting kernel module..."
#     sudo insmod $SCRIPT_DIR/acer-wmi-battery/acer-wmi-battery.ko
#     echo "$(date '+%Y-%m-%d %H:%M:%S') - Kernel module inserted successfully."
# } 2>&1 | tee -a $LOG_FILE

# Run the Python script to clean the file log and log any errors
{
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Running clean_file_log.py..."
    $PYTHON_DIR $SCRIPT_DIR/clean_file_log.py
    echo "$(date '+%Y-%m-%d %H:%M:%S') - clean_file_log.py completed."
} 2>&1 | tee -a $LOG_FILE

# Infinite loop to ensure run.py restarts if it crashes
while true
do
    {
        echo "$(date '+%Y-%m-%d %H:%M:%S') - Starting run.py..."
        # Run the Python script using Anaconda Python
        $PYTHON_DIR $SCRIPT_DIR/run.py
        # Check if run.py exited normally
        if [ $? -ne 0 ]; then
            echo "$(date '+%Y-%m-%d %H:%M:%S') - run.py crashed with an error. Restarting..."
        fi
    } 2>&1 | tee -a $LOG_FILE

    # Wait for 5 seconds before restarting
    sleep 5
done

