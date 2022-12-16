from Cpf_Cnpj import Documento

cpf1 = "96431082796"
cnpj1 = "23189383000274"

documento1 = Documento.criar_documento(cpf1)
documento2 = Documento.criar_documento(cnpj1)

print(documento1)
print(documento2)
