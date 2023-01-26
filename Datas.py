from datetime import datetime


class DatasBR:

    def __init__(self):
        self.data_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }
        numero_mes_cadastro = self.data_cadastro.month
        mes_cadastro = meses_do_ano[numero_mes_cadastro]

        return mes_cadastro

    def dia_semana_cadastro(self):
        semana = {
            0: "Segunda",
            1: "Terça",
            2: "Quarta",
            3: "Quinta",
            4: "Sexta",
            5: "Sábado",
            6: "Domingo"
        }
        dia = self.data_cadastro.weekday()

        dia_da_semana = semana[dia]

        return dia_da_semana

