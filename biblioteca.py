#biblioteca
from aluno import Aluno
from livro import Livro
class Biblioteca:
	def __init__(self):         #metodo contrutor
		self.__listAlunos=[]    #list de Alunos
		self.__listLivros=[]    #list de Livros
	def printarAlunos(self):
		if (len(self.__listAlunos)==0):
			print("Nao ha Alunos cadastrados!")
		else:
			for a in self.__listAlunos:
				print("aluno:%s"%(a.getNome()))
	def printarLivros(self):
		if (len(self.__listLivros)==0):
			print("Nao ha Livros cadastrados!")
		else:
			for a in self.__listLivros:
				print("livro:%s"%(a.getNome()))
	def setAlunos(self,aluno):
		self.__listAlunos.append(aluno)
	def setLivros(self,livro1):
		self.__listLivros.append(livro1)
		
