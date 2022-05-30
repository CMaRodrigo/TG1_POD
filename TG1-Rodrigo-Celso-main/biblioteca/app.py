from acervo import*
from livro import*
from usuario import*

def main():
    comandos = []
    lista_arquivos = str(input('lista de arquivos'))
    lista_arquivos = lista_arquivos.split(' ')


    print(lista_arquivos)
    for i in lista_arquivos:
        with open(i, 'r') as rd:
            for comando in rd.readlines():
                comando = comando.replace('\n', '')
                comandos.append(comando.split('-->'))
    
    for comandos in comandos:
        for arg in comando:
            print(arg + '', end= '')
    
    print(comandos)
    if (__name__ == "__main__"):
        main()
