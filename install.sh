#!/bin/bash

main() {
    if ! [ -x "$(command -v git)" ]; then
        echo 'Error: git is not installed.'
        exit 1
    fi
    if ! [ -x "$(command -v pip)" ]; then
        echo 'Error: pip is not installed.'
        exit 1
    fi
    if [ -f ~/.tldrrc ]; then
        echo "found ~/.tldrrc, skip install process"
        exit 1
    fi

    read -r -p "input the dir you want to store the tldr pages, e.g. /home/lord63/code/: " download_dir
    tldr_pages_path="$download_dir/tldr"
    if [ ! -d "$tldr_pages_path" ]; then
        mkdir -p "$tldr_pages_path"
    fi

    echo "clone tldr pages..."
    git clone git@github.com:tldr-pages/tldr.git "$tldr_pages_path"

    echo "install tldr.py..."
    if [[ `which python | grep -o '/usr'` == "/usr" ]]; then
        sudo pip install -U tldr.py
    else
        pip install -U tldr.py
    fi

    echo "init tldr.py..."
    platform="unknown"
    case "$OSTYPE" in
        solaris*) platform="sunos" ;;
        darwin*)  platform="macos" ;;
        linux*)   platform="linux" ;;
        bsd*)     platform="bsd" ;;
        msys*)    platform="windows" ;;
        *)        echo "unknown: $OSTYPE" ;;
    esac
    supported_platform=("linux" "sunos" "macos")
    if [[ ! " ${supported_platform[*]} " == *" ${platform} "* ]]; then
        echo "$platform is not in supported platform ${supported_platform[*]}"
        exit 1
    fi
    cat <<-EOF > ~/.tldrrc
colors:
    command: cyan
    description: blue
    usage: green
platform: $platform
repo_directory: $tldr_pages_path
EOF

    echo "rebuild tldr.py..."
    tldr reindex
}

main
