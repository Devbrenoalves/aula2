funcionariosParaCadastrar = [
    {"nome": "Pablo", "sobrenome": "Araujo", "idade": 34, "altura": 1.71, "temHabilitacao": True},
    {"nome": "Ana", "sobrenome": "Silva", "idade": 28, "altura": 1.65, "temHabilitacao": False},
    {"nome": "Carlos", "sobrenome": "Souza", "idade": 40, "altura": 1.80, "temHabilitacao": True}
]

cadastrosParaEnviarParaOBanco = []


class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura, temHabilitacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.temHabilitacao = temHabilitacao


def cadastrar():
    for funcionario in funcionariosParaCadastrar:
        pessoa = Pessoa(
            funcionario["nome"],
            funcionario["sobrenome"],
            funcionario["idade"],
            funcionario["altura"],
            funcionario["temHabilitacao"]
        )
        cadastrosParaEnviarParaOBanco.append(pessoa)


def salvar():
    for pessoa in cadastrosParaEnviarParaOBanco:
        print(f"O usuario {pessoa.nome} {pessoa.sobrenome} foi salvo com sucesso.")


cadastrar()
salvar()
