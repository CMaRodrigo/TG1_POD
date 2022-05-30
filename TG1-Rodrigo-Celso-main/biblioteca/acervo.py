from livro import Livro

acervo_dat = "C:\\Users\\User\\OneDrive\\Área de Trabalho\\TG1-Rodrigo-Celso-main\\TG1-Rodrigo-Celso-main\\database\\acervo.dat"


class Acervo:
    # Métodos para manipular o arquivo acervo.dat
    def __init__(self):
        self.livros = []
        with open(acervo_dat, "r") as f:
            for line in f.readlines():
                args = line.replace('\n', '').split("__")
                new_livro = Livro(args[0], args[1], args[2], args[3], args[4])
                self.add_livro(new_livro)

    def add_livro(self, new_livro):
        livro_em_acervo = False

        for livro in self.livros:
            if new_livro.titulo == livro.titulo:
                livro_em_acervo = True

        if livro_em_acervo:
            livro.exemplares = str(int(livro.exemplares) + 1)
        else:
            self.livros.append(new_livro)

        open(acervo_dat, 'w').close()

        with open(acervo_dat, 'a') as escrever:
            for livro in self.livros:
                escrever.write(livro.__str__())
                

    def remover_livro(self, livro):
        self.livro = acervo_dat
        if self.nmr_exemplares > 1:
            with open(acervo_dat, "r") as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if self.remove_titulo not in line:
                        f.write(line)
                f.truncate()
        else:
            raise "[Operação Inválida] O quantidade mínima no estoque é um livro"

    def pesquisa_livro(self, codigo):
        self.codigo = codigo
        with open(acervo_dat, "r") as f:
            for line in f.readlines():
                if codigo == line.replace('\n', '').split("__")[0]:
                    return line
            return 'Não encontrado'
