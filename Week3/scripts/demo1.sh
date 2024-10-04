#!/bin/bash

# This is a comment. It is not treated as executable. Use it for documentation.
# We want our scripts/code to be internally documented.

# We can set and reuse variables within our script.
name="Isaac" 

echo "$name"

# We can create reusable functions as well. Bash is not a full-fledged OOP language like Python.
# But we have ways to easily reuse code throughout our script. 

#We can pass parameters to our functions like in other languages, but with a different syntax than we are used to.
get_name() {

 echo "$1 from get_name"
}
# To call a function, we need both $ and (), i.e. $(name_of_your_function)
echo "Your name is: $(get_name Miguel) nice to see you"

# If we have a repetitive calling of code, we can put it in a loop to call it automatically as many times as we need to.

# Just like in other languages, we start with "for"
for ((i = 0 ; i < 10 ; i++));  do 
	echo "My dog's name is pancake"
done

# We end our loop with the done keyword. 

# We do have access to conditional logic within our scripts.
# We can use this to have branching logical paths based on certain conditions being met (or not met)

# Lets write a conditional to pay someone if the day is infact, friday

current_day=1
dannys_bank_account=0

if [[ current_day==5 ]]; then
	dannys_bank_account=$((dannys_bank_account+500))
elif [[ current_day==1 ]]; then
	echo ":("
else
	echo "just another day..."
fi # However many conditionals you check as part of your if-elif-else block... you end with "fi"


echo "Danny's account balanace: $dannys_bank_account"

# Lets say that I want to call a specific function, from the CLI
called_from_cli() {
	echo "This function was called from outside my script."
}

# We can call other scripts from within our demo1.sh. We can even leverage arguments to call specific functions
# from those other scripts

# We can probably acomplish this in several different ways... 
# We went with "source", it's behavior is akin to an import statement in other languages.
# It gives us access to things written in another script.
source ./function_lib.sh

say_hello
its_friday

# To be able to CLI arguments when calling my script, I need to add this special character.
"$@"



