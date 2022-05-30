from abc import ABCMeta, abstractmethod
dia = 0

arquivo = 'usuarios.dat'


class Usuario(metaclass=ABCMeta):
    def __init__(self, nome, CPF, matricula, multa):
        self.nome = nome
        self.CPF = CPF
        self.matricula = matricula
        self.multa = multa

# Métodos que vão manipular o arquivo usuarios.dat

    @abstractmethod
    def cadastrar_usuario(self):
        pass

# Garantir que o mesmo CPF não possa ser cadastrado

# def get para retornar os dados dos usuários já cadastrados (manipular arquivo)

    @abstractmethod
    def calculo_multa(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def retornar_dados(self):
        pass
# Aluno: if dia > 20:
            # acrescenta multa de 0,25
# Funcionario: if dia > 10:
                    # acrescenta multa de 0,50

# Usar decorador para controlar o acesso ao atributo multa

class Aluno(Usuario):
  def __init__(self, nome, CPF, matricula, multa, curso, classe = 'aluno'):
      super().__init__(nome, CPF, matricula, multa)
      self.classe = classe
      self.curso = curso
      self.cadastrar_usuario()
      self.calculo_multa()

  def cadastrar_usuario(self):
    with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'a') as arq:
      arq.writelines(self.__str__())

  def __str__(self):
    return self.classe + '__' + self.nome + '__' + self.CPF  + '__' +   self.matricula  + '__' +  self.multa  + '__' +  self.curso + '\n'

  def retornar_dados(self):
    with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'r') as arq:
        content = arq.readlines()
        print('----------------------------- LISTA DE USUARIOS -----------------------------------')
    for line in content:
        print(line)

  def calculo_multa(self):
      with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'a') as arq:
          #arq.write(self.__str__())
          arq.write('')


class Funcionario(Usuario):
  def __init__(self, nome, CPF, matricula, multa, departamento, classe = 'funcionario'):
      super().__init__(nome, CPF, matricula, multa)
      self.classe = classe
      self.departamento = departamento
      self.cadastrar_usuario()
      self.calculo_multa()

  def cadastrar_usuario(self):
        with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'a') as arq:
            arq.write(self.__str__())


  def __str__(self):
        return self.classe + '__' + self.nome + '__' + self.CPF  + '__' +   self.matricula  + '__' +  self.multa  + '__' +  self.departamento


  def retornar_dados(self):
        with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'r') as arq:
            content = arq.readlines()
            print('----------------------------- LISTA DE USUARIOS -----------------------------------')
        for line in content:
            print(line)


  def calculo_multa(self):
      if dia > 10:
          multa += 0,50


class Livro:
    dia = 0

    def __init__(self, titulo, autor, ano, exemplares):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.exemplares = exemplares

    # Métodos que vão manipular o arquivo emprestimos.dat

    # Vou precisar ir mais a funda no protocolo de gerenciamento de contexto
    def emprestimo(Livro):
        Livro.dia +=1
        pass

    def devolucao(Livro):
        pass

    def book_control(Livro):
        pass
    #Vou controlar quandos exemplares dde livros foram emprestados e devolvidos


arquivo = 'acervo.dat'

class Acervo:
    # Métodos para manipular o arquivo acervo.dat
    def __init__(self, codigo, titulo, autor, ano, nmr_exemplares):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.nmr_exemplares = nmr_exemplares
        self.adicao()

    def adicao(self):
        with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/acervo.dat', 'a') as arq:
            arq.writelines(self.__str__())

    def __str__(self):
        return self.codigo + '__' + self.titulo + '__' + self.autor + '__' + self.ano + '__' + self.nmr_exemplares


    def remocao(self):
        pass

    def pesquisa(Acervo):
        pass
        # pesquisar livro
