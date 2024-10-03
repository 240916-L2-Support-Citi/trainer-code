
# Bash Command Line Demo

## Table of Contents

- [Bash Command Line Demo](#bash-command-line-demo)
  - [Table of Contents](#table-of-contents)
  - [1. Accessing the Manual](#1-accessing-the-manual)
  - [2. Navigating Directories](#2-navigating-directories)
  - [3. Working with Files](#3-working-with-files)
  - [4. Copying and Moving Files](#4-copying-and-moving-files)
  - [5. Editing and Deleting Files](#5-editing-and-deleting-files)
  - [6. Working with Environment Variables](#6-working-with-environment-variables)
  - [7. Setting Permissions](#7-setting-permissions)
  - [8. Clearing the Terminal](#8-clearing-the-terminal)
  - [Summary of Key Commands](#summary-of-key-commands)

---

## 1. Accessing the Manual

```bash
man cp
```

- The `man` command provides manuals for various commands.
- Example: Use `man cp` to view the manual for the `cp` (copy) command, including flags and options.

---

## 2. Navigating Directories

```bash
pwd                  # Print the current directory path
cd /                 # Change to the root directory
cd ~                 # Go to the home directory
cd ..                # Move one directory up
mkdir demo           # Create a new directory called 'demo'
cd demo              # Change to the 'demo' directory
ls                   # List the contents of the current directory
ls -a                # List all contents, including hidden files
```

- `pwd`: Prints the current directory path.
- `cd /`: Moves to the root directory.
- `mkdir demo`: Creates a directory called `demo`.
- `ls`: Lists directory contents. Use `-a` to see hidden files.

---

## 3. Working with Files

```bash
touch hello.txt                      # Create a new file 'hello.txt'
echo "Hello World" > hello.txt        # Write "Hello World" to 'hello.txt'
cat hello.txt                         # Display contents of 'hello.txt'
wc -w hello.txt                       # Count the words in 'hello.txt'
```

- `touch`: Creates an empty file.
- `echo`: Writes a string to a file (or outputs to terminal).
- `cat`: Displays file contents.
- `wc -w`: Counts words in a file.

---

## 4. Copying and Moving Files

```bash
cp hello.txt goodbye.txt              # Copy 'hello.txt' to 'goodbye.txt'
mv goodbye.txt hello_backup.txt       # Rename 'goodbye.txt' to 'hello_backup.txt'
mkdir backup                          # Create a directory 'backup'
mv hello_backup.txt backup/.          # Move 'hello_backup.txt' to the 'backup' directory
```

- `cp`: Copies files or directories.
- `mv`: Moves or renames files or directories.
- `mkdir`: Creates directories.

---

## 5. Editing and Deleting Files

```bash
head hello.txt                        # Show the first 10 lines of 'hello.txt'
tail hello.txt                        # Show the last 10 lines of 'hello.txt'
rm hello.txt                          # Remove the file 'hello.txt'
rm -r backup                          # Remove the 'backup' directory and its contents
```

- `head` and `tail`: Display the first or last lines of a file.
- `rm`: Deletes files or directories (`-r` to delete directories recursively).

---

## 6. Working with Environment Variables

```bash
env                                   # Display all environment variables
echo $HOME                            # Show the value of the HOME variable
export MY_VAR="Hello Environment"     # Create a new environment variable
echo $MY_VAR                          # Display the value of 'MY_VAR'
unset MY_VAR                          # Remove the environment variable 'MY_VAR'
```

- `env`: Lists all environment variables.
- `export`: Creates or modifies environment variables.
- `unset`: Removes an environment variable.
- `$VAR`: Accesses the value of an environment variable.
- `PATH`: Manages the system's command lookup paths.

---

## 7. Setting Permissions

```bash
touch script.sh                       # Create a script file 'script.sh'
echo '#!/bin/bash\necho "Script executed"' > script.sh   # Add a simple script to 'script.sh'
chmod +x script.sh                    # Make 'script.sh' executable
./script.sh                           # Execute the script
```

- `chmod +x`: Gives a file executable permissions.
- `./`: Executes a file in the current directory.

---

## 8. Clearing the Terminal

```bash
clear                                 # Clear the terminal screen
```

- `clear`: Clears the terminal window, making it easier to see new output.
- **Shortcut**: Press `ctrl + l` for a faster way to clear the terminal.

---

## Summary of Key Commands

- **man**: View the manual for a command.
- **pwd, cd, ls**: Navigate and explore directories.
- **touch, echo, cat, rm**: Work with files (create, display, delete).
- **cp, mv**: Copy and move files.
- **env, export**: Manage environment variables.
- **chmod**: Modify file permissions.
- **crontab**: Schedule tasks.
- **clear**: Clear the terminal.
