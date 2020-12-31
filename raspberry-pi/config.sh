#!/bin/bash
# setup and configure Raspberry Pi.

# update packages
#sudo apt-get update && sudo apt-get upgrade -y

## Configuration
CONFIG=/boot/config.txt
CMDLINE=/boot/cmdline.txt

# enable i2c
sed $CONFIG -i -e "s/^#dtparam=i2c_arm=on/dtparam=i2c_arm=on/"


# install pip libraries
cd ./python
sudo python3 -m pip install -r requirements.txt
cd ..
