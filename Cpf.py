from validate_docbr import CPF


class ValidarCpf:

    def __init__(self, documento):
        documento = str(documento)

        if self.cpf_eh_valido(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF Inválido")

    def cpf_eh_valido(self, documento):

        if len(documento) == 11:
            return True
        else:
            raise ValueError("Quantidade de digitos inválida")

    def __str__(self):
        return self.padronizar_cpf()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_documento):
        self.cpf = novo_documento

    def padronizar_cpf(self):
        formatacao = CPF()
        return formatacao.mask(self.cpf)

