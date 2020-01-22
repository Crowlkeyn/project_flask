from models import Pessoas


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome="Paulo", idade=22)
    pessoa.save()


# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Paulo').first()
    print(pessoa.idade)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marcos').first()
    pessoa.nome = 'Baptista'
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Baptista').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
