#!/bin/bash

# Set the repository URL and the desired installation directory
REPO_URL="https://github.com/h8ngryDev4Hire/voDO"
INSTALL_DIR="$HOME/.local/bin"
TEMP=".vodo-temp-build"

# Greeting
echo "voDO! Your Todo Task Manager | It's Not Magic, It's voDO!"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Either Python is not installed on your system or"
    echo "your system has an outdated version of Python installed."
    echo "Please visit the official Python website to download and install Python:"
    echo "https://www.python.org/downloads/"
    exit 1
else
	echo "Python is installed!"
fi

# Confirmation prompt
read -p "Do you want to install voDO? [y/n]: " choice
case "$choice" in
    y|Y)
        echo "Proceeding with the installation..."
        ;;
    *)
        echo "Installation aborted."
        exit 0
        ;;
esac

# Check if the program is already installed
if [ -f "$INSTALL_DIR/vodo" ]; then
    echo "The program is already installed."
    read -p "Do you want to overwrite the existing installation? [y/n]: " choice
    case "$choice" in
        y|Y)
            echo "Overwriting the existing installation..."
            ;;
        *)
            echo "Installation aborted."
            exit 0
            ;;
    esac
fi

# Clone the repository
git clone $REPO_URL $TEMP
echo "Cloned repo"

# Navigate to the cloned repository directory
cd $TEMP

# Create the installation directory if it doesn't exist
mkdir -p $INSTALL_DIR

# Move the Python script to the installation directory
mv vodo.py $INSTALL_DIR/vodo

# Clean up the temporary repository directory
cd ..
rm -rf $TEMP

# Make the installed script executable
chmod +x $INSTALL_DIR/vodo

# Add the installation directory to PATH if not already present
if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.bashrc"
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.zshrc"

    echo "$INSTALL_DIR was not found in PATH, added to PATH."
    echo "You should probably reload your terminal session to use voDO."

    echo "Installation completed successfully!"
else
	echo "You can now run the program using the 'vodo' command."
	echo "Installation completed successfully!"
fi
