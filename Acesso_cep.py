import re
import requests


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
            raise TypeError(f"Tipo do parámetro inválido. Tipo esperado: <class 'str'>, Tipo recebido: {type(cep)}")
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

    def acesso_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        requisicao = requests.get(url)
        dados = requisicao.json()
        '''
        Tentativa de retorno usando for loop
        Status: return retorna primeira incidencia do loop então não consigo faz o output de todos os dados sem usar uma
        estrutura de dados
        '''
        informacoes = []
        dados_requisitados = ["localidade", "bairro", "uf"]
        for key in dados:
            if key in dados_requisitados:
                informacoes.append(f"{str(key).capitalize()}: {dados[key]}")
        return informacoes

        # Output de dados inserido individualmente
        # return dados.get["cep"], \
        #        dados["logradouro"], \
        #        dados["complemento"], \
        #        dados["bairro"], \
        #        dados["localidade"], \
        #        dados["uf"], \
        #        dados["ibge"], \
        #        dados["gia"], \
        #        dados["ddd"], \
        #        dados["siafi"]

