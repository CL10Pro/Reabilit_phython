#Perguntar ao usuario
from aluno import Aluno
from livro import Livro
from biblioteca import Biblioteca
def main():
	biblio1=Biblioteca() #istancio uma Biblioteca
	print("--Digite 0 para sair--")
	print("--Digite 1 para cadastrar livros--")
	print("--Digite 2 para consultar todos os livros--")
	print("--Digite 3 pegar livro emprestado--")
	print("--Digite 4 devolver livro--")
	print("--Digite 5 cadastrar aluno--")
	print("--Digite 6 para consultar todos os alunos--")
	opt=99
	while opt !=0:
		opt=int(input("Escolha uma opcao: "))
		if opt==1:
			print("--vc escolheu 1 cadastrar livros--")
			nome=input("nome: ")
			isbn=input("isbn: ")
			autor=input("autor: ")
			descricao=input("descricao: ")
			quantidade=int(input("quantidade: "))
			livro1=Livro(nome,isbn,autor,descricao,quantidade)#intancio um livro
			biblio1.setLivros(livro1)
		elif opt==2:
			print("--vc escolheu 2 consultar todos os livros --")
			biblio1.printarLivros()
		elif opt==3:
			print("--vc escolheu 3 pegar livro emprestado--")
		elif opt==4:
			print("--vc escolheu 4 devolver livro--")
		elif opt==5:
			print("--vc escolheu 5 cadastrar aluno--")
			nome=input("nome: ")
			cpf=input("cpf: ")
			idade=int(input("idade: "))
			turma=input("turma: ")
			aluno1=Aluno(nome,cpf,idade,turma)#intancio um aluno
			biblio1.setAlunos(aluno1)
		elif opt==6:
			print("--6 consultar todos os alunos ja cadastrados--")
			biblio1.printarAlunos()
		elif opt==0:
			print("--vc escolheu sair--")
		else:
			print("opcao invalida")
