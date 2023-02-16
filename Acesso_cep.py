import re


class BuscaEndereco:

    def __init__(self, cep):
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def __str__(self):
        return self.format_cep()

    @staticmethod
    def cep_e_valido(cep):
        if type(cep) != str:
            raise TypeError("Formato inválido")
        else:
            if len(cep) == 8:
                return True
            else:
                return False

    def format_cep(self):
        # O Retorno da função pode ser feito por fatiamento de Strings ou usando a biblioteca ReGex(re)
        # Usando ReGex
        padrao = "([0-9]{5})([0-9]{3})"
        cep_para_formartar = re.search(padrao, self.cep)
        cep_formatado = f"{cep_para_formartar.group(1)}-{cep_para_formartar.group(2)}"
        # Usando Fatiamento de Strings
        cep_formatado_2 = f"{self.cep[:5]}-{self.cep[5:]}"
        return cep_formatado


CEP = BuscaEndereco("01529001")
print(CEP)