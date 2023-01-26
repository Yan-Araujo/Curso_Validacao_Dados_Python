import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.validar_telefone(telefone):
            self._numero = telefone
        else:
            raise ValueError("Número inválido!!")

    def __str__(self):
        return self.formartar_telefone()

    def validar_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        validacao = re.findall(padrao, telefone)
        if validacao:
            return True
        else:
            return False

    def formartar_telefone(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self._numero)
        numero_formatado = f"+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado
