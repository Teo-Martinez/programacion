#!/bin/zsh

find_git_configs() {
  find "$1" -type d | while read -r dir; do
    if [ -d "$dir/.git" ]; then
      echo "$dir/.git/config" # Regular repo
    elif [ -f "$dir/config" ]; then
      echo "$dir/config"      # Most probably 'Bare' repo
    fi
  done
}

# main

search_directory="${1:-.}" # default to the current directory if not provided

# search config files
find_git_configs "$search_directory"
