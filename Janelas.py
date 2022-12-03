import PySimpleGUI as sg

sg.theme('Black')

# tela de login ------------------------------------------------
def sg_Login():
    layoutLogin = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Login', button_color='#5c2fd8'), sg.Button('Sair', button_color='#a0a0a0')],
        [sg.Text('', key='mensagem')],
    ]
    
    janelaLogin = sg.Window('LOGIN', layout=layoutLogin, font='Roboto 15')

    while True:
        event, values = janelaLogin.read()
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

# ----------------------------------------------------------------------------------------------

# Tela de MENU ---------------------------------------------------------------------------------
def sg_Menu():
    layoutMenu = [
        [sg.Text('Menu Principal', font='Roboto 30', text_color='#5c2fd8')],
        [sg.Text()],
        [sg.Button('CADASTROS')],
        [sg.Button('FERRAMENTAS')],
        [sg.Button('TÉCNICOS')],
        [sg.Button('RESERVAS')],
        [sg.Text()],
        [sg.Button('Sair', button_color='#a0a0a0', font='Roboto 15')],
    ]
    
    janelaMenu = sg.Window('PROGRAMA - TEAM 02', layout=layoutMenu, size=(400,300), element_justification='center', font='Roboto 15')
    
    while True:
        event, values = janelaMenu.read()
        if event == 'CADASTROS':
            janelaMenu.close()
            sg_CadastroGeral()
        if event == 'Sair':
            janelaMenu.close()
            sg.Exit()
            break
        elif event == sg.WIN_CLOSED:
            break


# ----------------------------------------------------------------------------------------------

def sg_CadastroGeral():
    layoutCadastroGeral = [
        [sg.Text('Cadastrar', font='Roboto 30', text_color='#5c2fd8')],
        [sg.Button('FERRAMENTAS'), sg.Button('TECNICOS')],
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


# Tela de CADASTRO DE FERRAMENTAS --------------------------------------------------------------

def sg_CadastroF():
    layoutCadF = [ 
            [sg.Text('Ferramenta'), sg.InputText()],
            [sg.Text('Modelo'), sg.InputText()],
            [sg.Text('Fabricante'), sg.InputText()],
            [sg.Text('Descrição'), sg.InputText()],
            [sg.Text('Peso'), sg.InputText()],
            [sg.Text('Quantidade'), sg.InputText()],
            [sg.Text('Voltagem'), sg.InputText()],
            [sg.Text('Tipo'), sg.InputText()],
            [sg.Button('Cadastrar'), sg.Button('Voltar', button_color='#a0a0a0')] 
            ]

    janelaCadastroF = sg.Window('CADASTRO DE FERRAMENTAS', layout=layoutCadF, font='Roboto 15')

    while True:
        event, values = janelaCadastroF.read()
        if event == 'Voltar':
            janelaCadastroF.close()
            sg_Menu()
            break
        elif event == sg.WIN_CLOSED:
            break

# ----------------------------------------------------------------------------------------------

# Tela de CADASTRO DE TECNICOS -----------------------------------------------------------------

def sg_CadastroT():
    layoutCadT = [ 
            [sg.Text('CPF'), sg.InputText()],
            [sg.Text('Nome'), sg.InputText()],
            [sg.Text('Sobrenome'), sg.InputText()],
            [sg.Text('Telefone'), sg.InputText()],
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
        if event == 'Voltar':
            janelaCadastroT.close()
            sg_Menu()
            break
        elif event == sg.WIN_CLOSED:
            break

# ----------------------------------------------------------------------------------------------

# Tela de RESERVAS -----------------------------------------------------------------------------

def sg_CadastroR():
    layoutCadR = [ 
            [sg.Text('Tecnico'), sg.InputText()],
            [sg.Text('Ferramenta', key='-FERRAMENTA-'), sg.InputText()],
            [sg.Input(key='DT-RESERVA', size=(20,1)) , sg.CalendarButton('Data da Reserva', close_when_date_chosen=True, target='DT-RESERVA',location=(800,400),no_titlebar=False)],
            [sg.Input(key='DT-DEVOLUCAO', size=(20,1)), sg.CalendarButton('Data da Reserva', close_when_date_chosen=True, target='DT-DEVOLUCAO',location=(800,400),no_titlebar=False)],
            [sg.Button('Cadastrar'), sg.Button('Voltar', button_color='#a0a0a0')] 
            ]

    janelaCadastroR = sg.Window('CADASTRO DE RESERVAS', layout=layoutCadR, font='Roboto 15')

    while True:
        event, values = janelaCadastroR.read()
        if event == 'Voltar':
            janelaCadastroR.close()
            sg_Menu()
            break
        elif event == sg.WIN_CLOSED:
            break
# ----------------------------------------------------------------------------------------------

# 

