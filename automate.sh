#!/bin/sh

# To run this, the first, modify the shell script permissions:
# $ chmod +x automate.sh
# To run this every time after, use the following command:
# $ ./automate.sh "Your optional commit message"

# Tooltip:
printf "\033[0;32m   Pulling Down Ghost Content...   \033[0m\n" 

# Run GitGhost:
python3 GitGhost.py

# If a command fails then the deploy stops
set -e

# Just a tooltip to let you know the script is running.
printf "\033[0;32m   Deploying updates to GitHub...    \033[0m\n" 

git init # Initiatilizes git
git add . # Adds changes

# Commit changes.
msg="Backup: $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi

git commit -m "$msg" # Makes your commit with a timestamp
git push origin master # Pushes the code to GitHub