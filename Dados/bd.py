import pandas as pd

def DadosFerramentas():
    dadosF = {
        'FERRAMENTA': [],
        'MODELO': [],
        'FABRICANTE': [],
        'PESO': [],
        'QUANTIDADE': [],
        'VOLTAGEM': [],
        'TIPO': [],
    }

    dadosF_df = pd.DataFrame(dadosF)
    dadosFerramentas = pd.read_excel('ferramentas.xlsx')
    print(dadosFerramentas)

def DadosTecnicos():
    dadosT = {
        'TECNICOS': [],
        'FERRAMENTAS': [],
        'DATA DA RESERVA': [],
        'DATA DA DEVOLUÇÃO': [],
    }

    dadosT_df = pd.DataFrame(dadosT)
    dadosTecnicos = pd.read_excel('tecnicos.xlsx')
    print(dadosTecnicos)

def DadosResevas():
    dadosR = {
        'TECNICOS': [],
        'FERRAMENTAS': [],
        'DATA DA RESERVA': [],
        'DATA DA DEVOLUÇÃO': [],
    }

    dadosR_df = pd.DataFrame(dadosR)
    dadosReservas = pd.read_excel('reservas.xlsx')
    print(dadosReservas)

