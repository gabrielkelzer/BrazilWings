#!/bin/bash
clear
echo -e "\033[1;31mVERIFICANDO SE É POSSÍVEL EXECUTAR O SOFTWARE NO SEU CELULAR... \033[0m"
sleep 2
clear
echo -e "\033[1;33mVERIFICANDO O PROTOCOLO 7 ! \033[0m"
sleep 1
clear
cd
rm -rf BUGS2024
git clone https://github.com/gabrielkelzer/BUGS2024
cd BUGS2024
chmod +x *
clear
. ./PROTOCOLO7.sh
clear
