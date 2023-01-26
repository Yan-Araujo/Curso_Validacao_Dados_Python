from Cpf_Cnpj import Documento
from Telefones import TelefonesBr
from Datas import DatasBR

print("Validando CPF/CNPJ:\n")
cpf1 = "96431082796"
cnpj1 = "23189383000274"
documento1 = Documento.criar_documento(cpf1)
documento2 = Documento.criar_documento(cnpj1)
print(documento1)
print(documento2)

print("-" * 30)

print("Validando números telefonicos:\n")
telefone = "558192869392"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

print("-" * 30)

print("Validando Datas:\n")
data = DatasBR()
print(data)
print(data.mes_cadastro())
print(data.dia_semana_cadastro())