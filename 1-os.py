import os

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do SO - executar o comando no terminal
os.system('ver')

# 4 - Configurações da máquina
os.system('systeminfo')

# 5 - Limpar a tela do terminal
os.system('cls')

# 6 - Desligar o computador
os.system('shutdown /s') # Desligar em 60s - com /t 0 é imediato
os.system('shutdown /a') # Cancelar a solicitação de shutdown

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')

def cancel_shutdown():
    os.system('shutdown /a')