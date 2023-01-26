from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return ValidarCpf(documento)
        elif len(documento) == 14:
            return ValidarCnpj(documento)
        else:
            raise ValueError("Documento inválido")


class ValidarCpf:

    def __init__(self, documento):
        self._cpf = documento
        self.cpf_eh_valido(documento)

    def cpf_eh_valido(self, documento):
        if CPF().validate(documento):  # Método ".validate" já trata o erro caso o documento não tenha 11 numeros
            return self.cpf
        else:
            raise ValueError("CPF Inválido")

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


class ValidarCnpj:
    def __init__(self, documento):
        self._cnpj = documento
        self.validar_cnpj(documento)

    def __str__(self):
        return self.formatar_cnpj()

    def validar_cnpj(self, documento):
        if CNPJ().validate(documento):
            return self.cnpj
        else:
            raise ValueError("CNPJ Inválido")

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, novo_documento):
        self._cnpj = novo_documento

    def formatar_cnpj(self):
        return CNPJ().mask(self.cnpj)


class ValidarDocumentoEmUmaUnicaClasse:
    def __init__(self, documento, tipo_documento: str):
        self._documento = documento
        self._tipo_documento = tipo_documento.lower()
        self.validar_documento(documento, tipo_documento)

    def __str__(self):
        return self.formartar_documento()

    def validar_documento(self, documento, tipo_documento):
        if tipo_documento == "cpf" or tipo_documento == "CPF":
            if CPF().validate(documento):
                return self.documento
            else:
                raise ValueError("Documento inválido")

        elif tipo_documento == "cnpj":
            if CNPJ().validate(documento):
                return self.documento
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError("Documento Inválido")

    @property
    def documento(self):
        return self._documento

    @property
    def tipo_documento(self):
        return self._tipo_documento

    @documento.setter
    def documento(self, novo_documento):
        self._documento = novo_documento

    @tipo_documento.setter
    def tipo_documento(self, novo_documento):
        self._tipo_documento = novo_documento

    def formartar_documento(self):
        if self.tipo_documento == "cpf":
            validador_cpf = CPF()
            return validador_cpf.mask(self.documento)
        elif self.tipo_documento == "cnpj":
            validador_cnpj = CNPJ()
            return validador_cnpj.mask(self.documento)

