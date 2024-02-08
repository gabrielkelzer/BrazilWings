import os
clear = lambda: os.system('clear')
#maioria dos softwares estão na pasta principal, ou seja.... algumas funções do menu estão neste arquivo
iniciar_helewings = lambda: os.system('cd;cd HeleWings;. ./HeleWings.sh;cd;cd BrazilWings')
iniciar_TentameKelzer = lambda: os.system('cd;cd Tentame_Kelzer;. ./TentameKelzer.sh;cd;cd BrazilWings')
iniciar_SYSTEMNERF = lambda: os.system('cd;cd SYSTEM_NERF;. ./systemnerf.sh;cd;cd BrazilWing')
copiar_app_virusapk = lambda: os.system('cp -i Virus.apk /data/data/com.termux/files/home/storage/downloads')
copiar_app_smsbomber = lambda: os.system('cp -i Smsbomber.apk /data/data/com.termux/files/home/storage/downloads')
abrir_site_livro = lambda: os.system('termux-open-url https://clubedeautores.com.br/livro/achado-nao-e-roubado-2')
sleep = lambda: os.system('sleep 2')
umarquivoemshell = lambda: os.system('. ./baixarresto.sh')
link_manual = lambda: os.system('termux-open-url https://zonamestre.blogspot.com/2024/02/software-para-hacking-e-pentest-do.html')
iniciar_kelzerscan = lambda: os.system('cd;cd KelzerScan;python KelzerScan.py;cd;cd BrazilWings')
iniciar_kelzerstar = lambda: os.system('cd;cd KelzerStar;python kelzerstar.py;cd;cd BrazilWings')

MENU_CONFG = 0
MENU_BW = 0

while MENU_CONFG != "1":
     clear()
     print('''
          \033[36m--------------------\033[0m
         \033[33m SEJA BEM-VINDO(A) :D\033[0m
        \033[36m  --------------------\033[0m
        \033[1m  MENU DE CONFIGURAÇÕES INICIAIS:\033[0m
        \033[32m  1 - INICIAR
          2 - BAIXAR O RESTANTE DO SCRIPT
          3 - MANUAL COMPLETO \033[0m
''')
     MENU_CONFG = input('\033[33mDIGITE UM NÚMERO:\033[0m')
     clear()



     # condicional encadeado
     if MENU_CONFG == "1":
          print('\033[31mOK\033[0m')
          sleep()
          print('\033[31mINICIANDO...\033[0m')
          sleep()
     elif MENU_CONFG == "2":
          umarquivoemshell()
     elif MENU_CONFG == "3":
          link_manual()
     else:
          print('\033[31mVOCÊ DIGITOU UM NÚMERO DIFERENTE ! ;-; \033[0m')
          sleep()



while MENU_BW != "10" and MENU_BW != "2":
     clear()
     print('''
\033[1;36ml=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=l\033[0m
\033[1;36ml\033[0m\033[1;33m                  LICENÇA GPL \033[0m       \033[1;36m            l\033[0m\033[1;36m
l=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=l             
l\033[0m\033[1;31m 卐                                           卐 \033[0m\033[1;36ml\033[0m
\033[1;36ml\033[0m                                                \033[1;36m l\033[0m
l\033[0m\033[1;31m             ─▄────▄▄▄▄▄▄▄────▄─               \033[0m\033[1;36ml\033[0m
\033[1;36ml\033[0m         \033[1;31m     ▀▀▄─▄█████████▄─▄▀▀       \033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m        \033[1;31m      ────██─▀███▀─██────     \033[0m          \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31m     ──▄─▀████▀████▀─▄──     \033[0m          \033[1;36m l\033[0m
\033[1;36ml\033[0m        \033[1;31m      ▀█────██▀█▀██────█▀    \033[0m           \033[1;36m l\033[0m
\033[1;36ml\033[0m                                                \033[1;36m l\033[0m
\033[1;36ml\033[0m              \033[1;31m   BrazilWings V1      \033[0m           \033[1;36m l\033[0m
\033[1;36ml\033[0m      \033[1;31m   /-----------------------------\   \033[0m     \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m1\033[1;36m] PortScan em Python \033[0m     \033[1;31ml\033[0m         \033[1;36ml\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m2\033[1;36m] BruteForce para achar \033[0m  \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m   \033[1;36m  pastas e arquivos de \033[0m   \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m   \033[1;36m  sites.            \033[0m      \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m3\033[1;36m] Menu de instalações e \033[0m  \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m   \033[1;36m  de personalizar o   \033[0m    \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m   \033[1;36m  o Termux          \033[0m      \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m4\033[1;36m] Enviar aúdio falso no  \033[0m \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m    \033[1;36m WhatsApp.     \033[0m          \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m5\033[1;36m] Sistema antitravas Zap\033[0m  \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m    \033[1;36m (ROOT)             \033[0m     \033[1;31ml\033[0m      \033[1;36m   l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m6\033[1;36m] Obter Apks de Hacking\033[0m   \033[1;31ml\033[0m       \033[1;36m  l   \033[0m                     
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m7\033[1;36m] Código de cor para  \033[0m    \033[1;31ml\033[0m      \033[1;36m   l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m     \033[1;36mcriar meus próprios    \033[0m \033[1;31ml\033[0m      \033[1;36m   l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m    \033[1;36m Scripts.        \033[0m        \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m8\033[1;36m] O que é licença GPL ?  \033[0m \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m9\033[1;36m] Comprar o livro do  \033[0m    \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m    \033[1;36m  desenvolvedor   \033[0m       \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m10\033[1;36m] Sair \033[0m                  \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m       \033[1;31m  \-----------------------------/  \033[0m      \033[1;36m l\033[0m
\033[1;36ml\033[0m      \033[1;31m   By: Gabriel Kelzer(@bielkelzer)   \033[0m     \033[1;36m l\033[0m
\033[1;36ml\033[0m\033[1;31m 卐                ┌∩┐(◣_◢)┌∩┐                卐 \033[0m\033[1;36ml\033[0m
\033[1;36m---------------------------------------------------\033[0m ''')      
     MENU_BW = input('\033[35mDIGITE UM NÚMERO: \033[0m')
     print('\n\033[90mA ideia do criador do script era criar um Lazymux Brasileiro\033[0m')
     sleep()
     clear()


     match MENU_BW:  
          case "1":
               iniciar_kelzerscan()
          case "2":
               iniciar_kelzerstar()
          case "3":
               iniciar_helewings()
          case "4":
               iniciar_TentameKelzer()
          case "5":
               iniciar_SYSTEMNERF()
          case "6":
               copiar_app_virusapk()
               copiar_app_smsbomber()
               clear()
               print ('''\033[31mPRONTO, AGORA VERIFIQUE A SUA PASTA DE DOWNLOADS.\033[0m:
                      ''')
               OP_PAUSAR = input('\033[33mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "7":
               print('\033[1mNEGRITO\033[m     \ 0 3 3 [ 1 m')
               print('\033[3mITÁLICO\033[m     \ 0 3 3 [ 3 m')
               print('\033[4mSUBLINHADO\033[m     \ 0 3 3 [ 4 m')
               print('\033[7mCOR INVERTIDA\033[m     \ 0 3 3 [ 7 m')
               print('\033[9mTACHADO\033[m     \ 0 3 3 [ 9 m')
               print('\033[21mSUBLINHADO\033[m     \ 0 3 3 [ 2 1 m')
               print('\033[30mTEXTO PRETO\033[m     \ 0 3 3 [ 3 0 ')
               print('\033[31mTEXTO VERMELHO\033[m     \ 0 3 3 [ 3 1 m')
               print('\033[32mTEXTO VERDE\033[m     \ 0 3 3 [ 3 2 m')
               print('\033[33mTEXTO AMARELO\033[m     \ 0 3 3 [ 3 3 m')
               print('\033[34mTEXTO AZUL\033[m     \ 0 3 3 [ 3 4 m')
               print('\033[35mTEXTO MAGENTA\033[m     \ 0 3 3 [ 3 5 m')
               print('\033[36mTEXTO CIANO\033[m     \ 0 3 3 [ 3 6 m')
               print('\033[37mTEXTO CINZA\033[m     \ 0 3 3 [ 3 7 m')
               print('\033[40mFUNDO PRETO\033[m     \ 0 3 3 [ 4 0 m')
               print('\033[41mFUNDO VERMELHO\033[m     \ 0 3 3 [ 4 1 m')
               print('\033[42mFUNDO VERDE\033[m     \ 0 3 3 [ 4 2 m')
               print('\033[43mFUNDO AMARELO\033[m     \ 0 3 3 [ 4 3 m')
               print('\033[44mFUNDO AZUL\033[m     \ 0 3 3 [ 4 4 m')
               print('\033[45mFUNDO MAGENTA\033[m     \ 0 3 3 [ 4 5 m')
               print('\033[46mFUNDO CIANO\033[m     \ 0 3 3 [ 4 6 m')
               print('\033[47mFUNDO CINZA\033[m     \ 0 3 3 [ 4 7 m')
               print('\033[51mTEXTO COM BORDA\033[m     \ 0 3 3 [ 5 1 m')
               print('\033[52mTEXTO COM BORDA\033[m     \ 0 3 3 [ 5 2 m')
               print('\033[90mTEXTO AZUL ESCURO\033[m     \ 0 3 3 [ 9 0 m')
               print('\033[100mFUNDO AZUL CLARO\033[m     \ 0 3 3 [ 1 0 0 m')
               OP_PAUSAR = input('\033[33mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "8":
               print ('''\033[34m
Este código tem licença GPL, isso quer dizer que os usuários podem modificar o script e trocar o nome do criador. Porém, eles precisam dizer em alguma parte do programa a seguinte frase "Este Software foi baseado no código-fonte do script BrazilWings.
                    \033[0m  ''')
               OP_PAUSAR = input('\033[33mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "9":
               abrir_site_livro()
          case "10":
               print('''
\033[1;32mDESENVOLVEDOR:\033[0m
     \033[1;34mGabriel Kelzer.\033[0m
\033[1;32mINSTAGRAM:\033[0m
     \033[1;34m@bielkelzer.\033[0m
\033[1;32mCOMUNIDADE ADMINISTRADORA DA SCRIPT:\033[0m
     \033[1;34mKelzer Comunity\033[0m\033[1;32m
GRUPO DO TELEGRAM:\033[0m\033[1;34m
     HTTPS://T.ME/KELZERCOMUNITY\033[0m
\033[03;32m"Às vezes criatividade é continuar criando coisas mesmo não sendo reconhecido", Gabriel Kelzer.\033[0m
''')
          case _:
               print ('''\033[31mO número que você digitou é inválido !!!\033[0m
                      ''')
               OP_PAUSAR = input('\033[33mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
