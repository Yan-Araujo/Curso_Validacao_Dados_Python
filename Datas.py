from datetime import datetime, timedelta


class DatasBR:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formatar_data()

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
        numero_mes_cadastro = self.momento_cadastro.month
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
        dia = self.momento_cadastro.weekday()

        dia_da_semana = semana[dia]

        return dia_da_semana

    def formatar_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M:%S")
        return data_formatada

    def tempo_de_cadastro(self):
        return (datetime.today() + timedelta(days=15, hours=12)) - self.momento_cadastro
