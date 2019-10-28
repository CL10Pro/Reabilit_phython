#livro
class Livro:
	#definindo como privados __Atributo
	def __init__(self,nome,isbn,autor,descricao,quantidade):
		self.__nome=nome
		self.__isbn=isbn
		self.__autor=autor
		self.__descricao=descricao
		self.__quantidade=quantidade
#gets--------------------------------------------------------------
	def getNome(self):
		return 	self.__nome
	def getIsbn(self):
		return 	self.__isbn
	def getAutor(self):
		return 	self.__autor
	def getDescricao(self):
		return 	self.__descricao
	def getQuantidade(self):
		return 	self.__quantidade
#sets--------------------------------------------------------------	
	def setQuantidade(quant):
		self.__quantidade=quant
	
	def printarLivro(self):
		print("Nome:%s"%(self.__nome))
		print("Isbn:%s"%(self.__isbn))
		print("Autor:%s"%(self.__autor))
		print("Descricao:%s"%(self.__descricao))
		print("Quantidade:%i"%(self.__quantidade))
