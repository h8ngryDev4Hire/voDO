#!/bin/bash

# Set the repository URL and the desired installation directory
REPO_URL="https://github.com/h8ngryDev4Hire/Voodoo"
INSTALL_DIR="$HOME/.local/bin"
TEMP=".temp"

# Clone the repository
git clone $REPO_URL $TEMP 

# Navigate to the cloned repository directory
cd $TEMP

# Create the installation directory if it doesn't exist
mkdir -p $INSTALL_DIR

# Move the Python script to the installation directory
mv voodoo.py $INSTALL_DIR/voodoo

# Clean up the temporary repository directory
cd ..
rm -rf $TEMP

# Make the installed script executable
chmod +x $INSTALL_DIR/voodoo

# Add the installation directory to PATH if not already present
if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.bashrc"
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.zshrc"
    source "$HOME/.bashrc"
    source "$HOME/.zshrc"
fi

echo "Installation completed successfully!"
echo "You can now run the program using the 'todo' command."
