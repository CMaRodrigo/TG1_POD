from abc import ABCMeta, abstractmethod

arquivo = "C:\\Users\\User\\OneDrive\\Área de Trabalho\\TG1-Rodrigo-Celso-main\\TG1-Rodrigo-Celso-main\\database\\usuarios.dat"

class Usuario(metaclass=ABCMeta):
    def __init__(self, nome, CPF, matricula, multa = 0):
        self.nome = nome
        self.CPF = CPF
        self.matricula = matricula
        self.multa = multa

# Métodos que vão manipular o arquivo usuarios.dat

    @abstractmethod
    def cadastrar_usuario(self):
        pass


# def get para retornar os dados dos usuários já cadastrados (manipular arquivo)

    @abstractmethod

    def calculo_multa(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def retornar_dados(self):
        pass



class Aluno(Usuario):
  def __init__(self, nome, CPF, matricula, multa, curso):
      super().__init__(nome, CPF, matricula, multa)
      self.curso = curso
      self.cadastrar_usuario()
      self.calculo_multa()

  def cadastrar_usuario(self):
      arquivo.seek(0)
      if self.CPF != 11:
        raise 'CPF necessariamente precisa ter 11 digitos'
      if self.matricula != 8:
        raise 'Matricula necessariamente precisa ter 8 dígitos'
      if self.CPF not in arquivo.read():
        with open(arquivo) as arq:
            arq.writelines(self.__str__())
      else:
          raise 'O CPF JÁ ESTÁ CADASTRADO'


  def __str__(self):
    return 'aluno__' + self.nome + '__' + self.CPF  + '__' +   self.matricula  + '__' +  self.multa  + '__' +  self.curso


  def retornar_dados(self):
        with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'r') as arq:
            content = arq.readlines()
            print('----------------------------- LISTA DE USUARIOS -----------------------------------')
        for line in content:
            print(line)

  def calculo_multa(self):
      pass


class Funcionario(Usuario):
  def __init__(self, nome, CPF, matricula, multa, departamento):
      super().__init__(nome, CPF, matricula, multa)
      self.departamento = departamento
      self.cadastrar_usuario()
      #self.calculo_multa()

  def cadastrar_usuario(self):
      arquivo.seek(0) # File pointer will be at the begining of file
      if self.CPF not in arquivo.read():
        with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'a') as arq:
            arq.write(self.__str__())
      else:
          raise 'O CPF JÁ ESTÁ CADASTRADO'



  def __str__(self):
        return 'funcionario__' + self.nome + '__' + self.CPF  + '__' +   self.matricula  + '__' +  self.multa  + '__' +  self.departamento


  def retornar_dados(self):
        with open('C:/Users/User/Downloads/TG1-Rodrigo-Celso-main/TG1-Rodrigo-Celso-main/database/usuarios.dat', 'r') as arq:
            content = arq.readlines()
            print('----------------------------- LISTA DE USUARIOS -----------------------------------')
        for line in content:
            print(line)


  def calculo_multa(self):
      pass

#P1 = Funcionario('Rodrigo', '05130414004', '21101526', '0', 'Ciencia de Dados')
