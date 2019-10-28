#aluno
class Aluno:
	#definindo como privados __Atributo
	def __init__(self,nome,cpf,idade,turma):
		self.__nome=nome
		self.__cpf=cpf
		self.__idade=idade
		self.__turma=turma
#gets--------------------------------------------------------------
	def getNome(self):
		return 	self.__nome
	def getCpf(self):
		return 	self.__cpf
	def getIdade(self):
		return 	self.__Idade
	def getTurma(self):
		return 	self.__Turma
def printarAluno(self):
		print("Nome:%s"%(self.__nome))
		print("cpf:%s"%(self.__cpf))
		print("idade:%i"%(self.__idade))
		print("Turma:%s"%(self.__turma))
