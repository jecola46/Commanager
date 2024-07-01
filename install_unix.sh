#!/bin/bash

#### Install Python 3.11.9

# Get it
wget -c https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tar.xz
tar -Jxf Python-3.11.9.tar.xz

# Compile and install
cd Python-3.11.9/
./configure --enable-optimizations
sudo make -j4 && sudo make altinstall

# Clean up :)
sudo rm -rf Python-3.11.9
rm -rf Python-3.11.9.tar.xz

# Verify the installation
if [[ "$(python3.11 -V)" =~ "Python 3.11.9" ]]; then
   echo "Python 3.11.9 was successfully installed!"
else
   echo "Ermmm something went wrong ..."
fi
