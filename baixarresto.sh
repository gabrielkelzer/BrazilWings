#!/bin/bash
apt update 
apt upgrade 
pkg install python
pkg install pip
pip install --upgrade pip
pip install lolcat
pkg install espeak
cd
git clone https://github.com/gabrielkelzer/HeleWings
git clone https://github.com/gabrielkelzer/Tentame_Kelzer
git clone https://github.com/gabrielkelzer/KelzerScan
git clone https://github.com/gabrielkelzer/SYSTEM_NERF
git clone https://github.com/gabrielkelzer/KELZERX
cd KELZERX
chmod +x *
bash install.sh
cd
cd BrazilWings
