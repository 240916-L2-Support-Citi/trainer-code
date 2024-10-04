#!/bin/bash

# Im going to create a variable and store the name of my file in it. 
# Note that the first time this runs, the file won't exist yet.
LOG_FILE="/home/jon/revature/l2-support-citi/cronjobdemo/time_log.txt"


# This line sticks the output of the echo (including the call of the date command)
# into my LOG_FILE... which is set to be time_log.txt

echo "Current date and time is: $(date)" >> "$LOG_FILE"
