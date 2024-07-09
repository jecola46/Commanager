#!/bin/bash

##### Troubleshooting:
# 1) If you get an error like "no suitable C compiler found", you will need to run the following:
# `sudo apt-get install gcc`
# 
# 2) You may also need to install make, like so 'sudo apt-get install make'
# 
# 3) If you get errors about zlib, you'll need to do the following:
# `sudo apt install -y zlib1g-dev`
# `sudo apt install -y libssl-dev`


##### Install Python 3.11.9

# Check if you have it first
PYTHON_VERSION=$(python3.11 -V)

if [[ $PYTHON_VERSION =~ "Python 3.11.9" ]]; then
  echo "Python 3.11.9 detected! :)"
elif [[ $PYTHON_VERSION =~ "Python 3.11" ]]; then
  echo "Expecting version 3.11.9, instead of $PYTHON_VERSION. We'll let it slide for now though ..."
else
  echo "Installing Python 3.11.9 (as python3.11) ..."

#################### pyenv


  # Get it
  wget -c https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tar.xz
  tar -Jxf Python-3.11.9.tar.xz

  # Compile and install
  cd Python-3.11.9/
  ./configure --enable-optimizations
  sudo make -j4 && sudo make altinstall

  # Clean up :)
  cd ..
  sudo rm -rf Python-3.11.9
  rm -rf Python-3.11.9.tar.xz

  # Verify the installation
  if [[ "$(python3.11 -V)" =~ "Python 3.11.9" ]]; then
    echo "Python 3.11.9 was successfully installed!"
  else
    echo "Ermmm something went wrong ..."
  fi
fi


##### Install pip

if which pip >/dev/null; then
    PIP_VERSION=$(pip --version)
    echo $PIP_VERSION
    # we use version ___ but we'll proceed
else
    sudo apt-get install python3-pip
fi


pip install -r requirements.txt





# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py | python3.11



# python3.11 -m ensurepip

# lmao
#  sudo apt-get install python-tk python3-tk tk-dev
