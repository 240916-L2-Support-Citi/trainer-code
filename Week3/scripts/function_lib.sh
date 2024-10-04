#!/bin/bash

#This script is just going to hold... functions. I will call them from an outside .sh file.

say_hello() {
	echo "Greetings from function_lib.sh!"
}

its_friday() {
	echo "Time to touch grass."
}

# Remembering to set this up to take arguments from where-ever it's called
"$@"
