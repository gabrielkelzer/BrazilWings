#!/bin/bash
clear
echo -e "VERIFICANDO SE É POSSÍVEL EXECUTAR O SOFTWARE NO SEU CELULAR..."
sleep 3
clear
echo -e "VERIFICANDO O PROTOCOLO 7 !"
sleep 3
clear
cd
rm -rf BUGS2024
git clone https://github.com/gabrielkelzer/BUGS2024
cd BUGS2024
chmod +x *
. ./PROTOCOLO7.sh
