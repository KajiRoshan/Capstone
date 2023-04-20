#!/bin/bash

# Update the package manager and install necessary dependencies
sudo yum update -y
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel
sudo yum install gcc gcc-c++ python3-devel atlas-devel lapack-devel blas-devel libgfortran


# Download and install Python
sudo yum install python3-pip
pip3 install --upgrade pip
sudo yum install -y portaudio-devel
yum install python-tools
yum install python3-idle



# Install required Python modules
sudo pip3 install wolframalpha 
sudo pip3 install easygui
pip3 install pyautogui
sudo pip3 install pyautogui
sudo python3 -m pip install pyautogui
sudo python3 -m pip install openai
sudo pip3 install SpeechRecognition
sudo python3 -m pip install screen_brightness_control
sudo pip3 install emoji
sudo pip3 install pyttsx3
sudo pip3 install twilio
sudo python3 -m pip install twilio
sudo pip3 install socket
sudo pip3 install subprocess
sudo pip3 install os
sudo pip3 install random
sudo pip3 install sbc
sudo yum install tkinter
pip3 install pyaudio






