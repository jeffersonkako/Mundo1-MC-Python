import PySimpleGUI as sg

# Tema do programa ------------------------------------------------------------------------------
sg.theme('Black')


# tela de login ---------------------------------------------------------------------------------
def sg_Login():
    layoutLogin = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Text('', key='mensagem')],
        [sg.Button('Login', button_color='#5c2fd8'), 
        sg.Button('Sair', button_color='#a0a0a0'), sg.Text(),
        sg.Button('Equipe', button_color='#a0a0a0')
        ],
    ]
    
    janelaLogin = sg.Window('LOGIN', layout=layoutLogin, font='Roboto 15')

    while True:
        event, values = janelaLogin.read()
        if event == 'Equipe':
            Team2_inf = DadosEquipe()
            sg.popup(Team2_inf,
            font='Roboto 20', 
            background_color='#5c2fd8', 
            auto_close=True, 
            auto_close_duration=10,
            no_titlebar=True)
            janelaLogin.close()
            sg_Login()
        if event == 'Sair':
            sg.Exit()
            break
        elif event == sg.WIN_CLOSED:
            break
        elif event == 'Login':
            usuario_correto = 'admin'
            senha_correta = '1234'
            usuario = values['usuario']
            senha = values['senha']
            if senha == senha_correta and usuario == usuario_correto:
                janelaLogin['mensagem'].update('Login feito com sucesso.', text_color='#00FF00')
                janelaLogin.close()
                sg_Menu()
            else:
                janelaLogin['mensagem'].update('Senha ou Usuário incorreto', text_color='#ff0000')


# TELA DO MENU ---------------------------------------------------------------------------------
def sg_Menu():
    layoutMenu = [
        [sg.Text('Menu Principal', font='Roboto 30', text_color='#5c2fd8')],
        [sg.Text()],
        [sg.Button('CADASTRAR'), sg.Button('CONSULTAR')],
        [sg.Button('EDITAR')],
        [sg.Text()],
        [sg.Button('Sair', button_color='#a0a0a0', font='Roboto 15')],
    ]
    
    janelaMenu = sg.Window('PROGRAMA - TEAM 02', layout=layoutMenu, size=(400,300), element_justification='center', font='Roboto 15')
    
    while True:
        event, values = janelaMenu.read()
        if event == 'CADASTRAR':
            janelaMenu.close()
            sg_CadastroGeral()
        if event == 'CONSULTAR':
            janelaMenu.close()
            sg_Consultas()
        if event == 'EDITAR':
            janelaMenu.close()
            sg_Editar()
        if event == 'Sair':
            janelaMenu.close()
            sg.Exit()
            break
        elif event == sg.WIN_CLOSED:
            break


# TELA DO CADASTRO---------------------------------------------------------------------------------
def sg_CadastroGeral():
    layoutCadastroGeral = [
        [sg.Text('CADASTRAR', font='Roboto 30', text_color='#5c2fd8')],
        [sg.Text()],
        [sg.Button('FERRAMENTAS')],
        [sg.Button('TECNICOS')],
        [sg.Button('RESERVA')],
        [sg.Text()],
        [sg.Button('Voltar', button_color='#a0a0a0')],
        ]
        
    janelaCadastroGeral = sg.Window('CADASTRO', layout=layoutCadastroGeral, size=(400,300), element_justification='center', font='Roboto 15')

    while True:
        event, values = janelaCadastroGeral.read()
        if event =='FERRAMENTAS':
            janelaCadastroGeral.close()
            sg_CadastroF()
        elif event =='TECNICOS':
            janelaCadastroGeral.close()
            sg_CadastroT()
        elif event =='RESERVA':
            janelaCadastroGeral.close()
            sg_CadastroR()
        elif event =='Voltar':
            janelaCadastroGeral.close()
            sg_Menu()
        elif event == sg.WIN_CLOSED:
            break


# TELA DO CADASTRO DE FERRAMENTAS --------------------------------------------------------------
def sg_CadastroF():
    layoutCadF = [ 
            [sg.Text('Ferramenta'), sg.InputText(key='-Ferramenta-')],
            [sg.Text('Modelo'), sg.InputText(key='-Modelo-')],
            [sg.Text('Fabricante'), sg.InputText(key='-Fabricante-')],
            [sg.Text('Descrição'), sg.InputText(key='-Descrição-')],
            [sg.Text('Peso'), sg.InputText(key='-Peso-')],
            [sg.Text('Quantidade'), sg.InputText(key='-Quantidade-')],
            [sg.Text('Voltagem'), sg.InputText(key='-Voltagem-')],
            [sg.Text('Tipo'), sg.InputText(key='-Tipo-')],
            [sg.Button('Cadastrar'), sg.Button('Voltar', button_color='#a0a0a0')] 
            ]

    janelaCadastroF = sg.Window('CADASTRO DE FERRAMENTAS', layout=layoutCadF, font='Roboto 15')

    while True:
        event, values = janelaCadastroF.read()
        if event == 'Cadastrar':
            Ferramentas_inf = DadosFerramentas(values)
            sg.popup(Ferramentas_inf,
            font='Roboto 20', 
            background_color='#007d4d', 
            auto_close=True, 
            auto_close_duration=10,
            no_titlebar=True)
            janelaCadastroF.close()
            sg_CadastroF()
        if event == 'Voltar':
            janelaCadastroF.close()
            sg_CadastroGeral()
            break
        elif event == sg.WIN_CLOSED:
            break


# TELA DO CADASTRO DE TÉCNICOS -----------------------------------------------------------------
def sg_CadastroT():
    layoutCadT = [ 
            [sg.Text('CPF'), sg.InputText(key='-CPF-')],
            [sg.Text('Nome'), sg.InputText(key='-Nome-')],
            [sg.Text('Sobrenome'), sg.InputText(key='-Sobrenome-')],
            [sg.Text('Telefone'), sg.InputText(key='-Telefone-')],
            [sg.Text('Turno: '), sg.Radio('Manhã', 'RADIO', key='-MANHA-'), sg.Radio('Noite', 'RADIO', key='-Noite-')],
            [sg.Text('Equipe: '), 
            sg.Radio('Team 1', 'RADIO', key='-TEAM1-'), 
            sg.Radio('Team 2', 'RADIO', key='-TEAM2-'),
            sg.Radio('Team 3', 'RADIO', key='-TEAM3-'),
            sg.Radio('Team 4', 'RADIO', key='-TEAM4-')],
            [sg.Button('Cadastrar'), sg.Button('Voltar', button_color='#a0a0a0')] 
            ]

    janelaCadastroT = sg.Window('CADASTRO DE TÉCNICOS', layout=layoutCadT, font='Roboto 15')

    while True:
        event, values = janelaCadastroT.read()
        if event == 'Cadastrar':
            Tecnico_inf = DadosTecnico(values)
            sg.popup(Tecnico_inf,
            font='Roboto 20', 
            background_color='#007d4d', 
            auto_close=True, 
            auto_close_duration=10,
            no_titlebar=True)
            janelaCadastroT.close()
            sg_CadastroT()
        if event == 'Voltar':
            janelaCadastroT.close()
            sg_CadastroGeral()
            break
        elif event == sg.WIN_CLOSED:
            break


# TELA DO CADASTRO DE RESERVAS ---------------------------------------------------------------------------------------------------------------------------------------------------------
def sg_CadastroR():
    layoutCadR = [ 
            [sg.Text('Tecnico'), sg.InputText(key='-TECNICO-')],
            [sg.Text('Ferramenta'), sg.InputText(key='-FERRAMENTA-')],
            [sg.Input(key='DT-RESERVA', size=(20,1)) , sg.CalendarButton('Data da Reserva', close_when_date_chosen=True, target='DT-RESERVA',location=(800,400),no_titlebar=False)],
            [sg.Input(key='DT-DEVOLUCAO', size=(20,1)), sg.CalendarButton('Data da Devolução', close_when_date_chosen=True, target='DT-DEVOLUCAO',location=(800,400),no_titlebar=False)],
            [sg.Button('Cadastrar'), sg.Button('Voltar', button_color='#a0a0a0')] 
            ]

    janelaCadastroR = sg.Window('CADASTRO DE RESERVAS', layout=layoutCadR, font='Roboto 15')

    while True:
        event, values = janelaCadastroR.read()
        if event == 'Cadastrar':
            Reservas_inf = DadosReserva(values)
            sg.popup(Reservas_inf,
            font='Roboto 20', 
            background_color='#007d4d', 
            auto_close=True, 
            auto_close_duration=10,
            no_titlebar=True)
            janelaCadastroR.close()
            sg_CadastroR()
        if event == 'Voltar':
            janelaCadastroR.close()
            sg_CadastroGeral()
            break
        elif event == sg.WIN_CLOSED:
            break


# TELA DE CONSULTAS -------------------------------------------------------------------------------------------------------------------------------
def sg_Consultas():
    layoutCadastroGeral = [
        [sg.Text('CONSULTAR', font='Roboto 30', text_color='#5c2fd8')],
        [sg.Text()],
        [sg.Button('FERRAMENTAS')],
        [sg.Button('TECNICOS')],
        [sg.Button('RESERVAS')],
        [sg.Text()],
        [sg.Button('Voltar', button_color='#a0a0a0')],
        ]
        
    janelaConsultas = sg.Window('CONSULTAS', layout=layoutCadastroGeral, size=(400,300), element_justification='center', font='Roboto 15')

    while True:
        event, values = janelaConsultas.read()
        if event =='FERRAMENTAS':
            janelaConsultas.close()
            sg_Consultas()
        elif event =='TECNICOS':
            janelaConsultas.close()
            sg_Consultas()
        elif event =='RESERVAS':
            janelaConsultas.close()
            sg_Consultas()
        elif event =='Voltar':
            janelaConsultas.close()
            sg_Menu()
        elif event == sg.WIN_CLOSED:
            break

# TELA DE EDIÇÕES --------------------------------------------------------------------------------------
def sg_Editar():
    layoutCadastroGeral = [
        [sg.Text('EDITAR', font='Roboto 30', text_color='#5c2fd8')],
        [sg.Text()],
        [sg.Button('FERRAMENTAS')],
        [sg.Button('TECNICOS')],
        [sg.Button('RESERVAS')],
        [sg.Text()],
        [sg.Button('Voltar', button_color='#a0a0a0')],
        ]
        
    janelaCadastroGeral = sg.Window('EDITAR', layout=layoutCadastroGeral, size=(400,300), element_justification='center', font='Roboto 15')

    while True:
        event, values = janelaCadastroGeral.read()
        if event =='FERRAMENTAS':
            janelaCadastroGeral.close()
            sg_Editar()
        elif event =='TECNICOS':
            janelaCadastroGeral.close()
            sg_Editar()
        elif event =='RESERVA':
            janelaCadastroGeral.close()
            sg_Editar()
        elif event =='Voltar':
            janelaCadastroGeral.close()
            sg_Menu()
        elif event == sg.WIN_CLOSED:
            break


# DADOS INPUTS ---------------------------------------------------------------------------------------------
def DadosReserva(values):
    info = 'RESERVA CADASTRADA\n'
    nome = '\nNome: '+ values['-TECNICO-']
    info += nome
    ferramentaR = '\nFerramenta: '+ values['-FERRAMENTA-']
    info += ferramentaR
    dataR = '\nReserva: ' + values['DT-RESERVA']
    info += dataR
    dataD = '\nDevolução: ' + values['DT-DEVOLUCAO']
    info += dataD
    return info


def DadosFerramentas(values):
    info = 'FERRAMENTA CADASTRADA\n'
    Ferramenta = '\nFerramenta: '+ values['-Ferramenta-']
    info += Ferramenta
    Fabricante = '\nFabricante: '+ values['-Fabricante-']
    info += Fabricante
    Descrição = '\nDescrição: ' + values['-Descrição-']
    info += Descrição
    Peso = '\nPeso: ' + values['-Peso-']
    info += Peso
    Quantidade = '\nQuantidade: ' + values['-Quantidade-']
    info += Quantidade
    Voltagem = '\nVoltagem: ' + values['-Voltagem-']
    info += Voltagem
    Tipo = '\nTipo: ' + values['-Tipo-']
    info += Tipo
    return info


def DadosTecnico(values):
    info = 'Técnico Cadastrado\n'
    CPF = '\nCPF: '+ values['-CPF-']
    info += CPF
    Nome = '\nNome: '+ values['-Nome-']
    info += Nome
    Sobrenome = '\nSobrenome: ' + values['-Sobrenome-']
    info += Sobrenome
    Telefone = '\nTelefone: ' + values['-Telefone-']
    info += Telefone
    return info

def DadosEquipe():
    info = 'TEAM 2\n'
    Aluno1 = '\nJefferson'
    info += Aluno1
    Aluno2 = '\nAmandio'
    info += Aluno2
    Aluno3 = '\nAriel'
    info += Aluno3
    Aluno4 = '\nRaiza'
    info += Aluno4
    return info




