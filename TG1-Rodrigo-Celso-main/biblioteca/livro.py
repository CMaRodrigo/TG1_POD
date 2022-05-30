class Livro:
    def __init__(self, codigo, titulo, autor, ano, exemplares):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.exemplares = exemplares

    # Métodos que vão manipular o arquivo emprestimos.dat

    def emprestimo(self):
        pass

    def devolucao(self):
        pass

    def book_control(self):
        pass

    def __str__(self):
        return self.codigo + '__' + self.titulo \
            + '__' + self.autor + '__' + self.ano \
            + '__' + self.exemplares

    # aqui posso colocar um contador em emprestimos e um em devolução ai vou saber as quantidades

    #Vou controlar quandos exemplares dde livros foram emprestados e devolvidos
