from Cpf_Cnpj import Documento
from Telefones import TelefonesBr
from Datas import DatasBR
from Acesso_cep import BuscaEndereco


def separar_codigos():
    print("-" * 35)


def validar_identidade():
    print("Validando CPF/CNPJ:\n")

    cpf1 = "96431082796"
    cnpj1 = "23189383000274"
    documento1 = Documento.criar_documento(cpf1)
    documento2 = Documento.criar_documento(cnpj1)
    print(documento1)
    print(documento2)


def validar_numero_telefone():
    print("Validando números telefonicos:\n")

    telefone = "558192869392"
    telefone_objeto = TelefonesBr(telefone)
    print(telefone_objeto)


def validar_datas():
    print("Validando Datas:\n")
    data = DatasBR()  # Instanciamento do objeto do tipo Data com a biblioteca datetime
    print(data)
    print(data.mes_cadastro())  # Retorna o mês usando o indice retornado pela função ".month" para checar no dicionário
    print(data.dia_semana_cadastro())  # Funciona como o último exemplo, porém checa o dia da semana utilizando weekday
    print(data.momento_cadastro)  # Comando executado pelo construtor no momento do instanciamento do objeto.
    print(data.tempo_de_cadastro())


def validar_cep():
    cep = BuscaEndereco("01529001")
    print(cep)


validar_datas()
