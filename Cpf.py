class Cpf:

    def __init__(self, cpf):
        cpf = str(cpf)

        if self.cpf_eh_valido(cpf):
            self._cpf = cpf
        else:
            raise ValueError("CPF Inválido")

    def __str__(self):
        return self.padronizar_cpf()

    @property
    def cpf(self):
        return self._cpf

    @staticmethod
    def cpf_eh_valido(cpf):
        if len(cpf) == 11:
            return True
        else:
            return False

    def padronizar_cpf(self):

        cpf_parte1 = self.cpf[: 3]
        cpf_parte2 = self.cpf[3: 6]
        cpf_parte3 = self.cpf[6: 9]
        cpf_parte4 = self.cpf[9:]

        return f"{cpf_parte1}.{cpf_parte2}.{cpf_parte3}-{cpf_parte4}"

