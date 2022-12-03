import PySimpleGUI as sg

sg.theme('Black')

# tela de login ------------------------------------------------
def sg_Login():
    layoutLogin = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Login')],
        [sg.Text('', key='mensagem')],
    ]
    
    janelaLogin = sg.Window('Tela Login', layout=layoutLogin, font='Arial 15')

    while True:
        event, values = janelaLogin.read()
        if event == sg.WINDOW_CLOSED:
            sg.Exit()
            break
        elif event == 'Login':
            usuario_correto = 'admin'
            senha_correta = '1234'
            usuario = values['usuario']
            senha = values['senha']
            if senha == senha_correta and usuario == usuario_correto:
                janelaLogin['mensagem'].update('Login feito com sucesso.')
                janelaLogin.close()
                sg_Menu()
            else:
                janelaLogin['mensagem'].update('Senha ou Usuário incorreto.')

# ----------------------------------------------------------------------------------------------

# Tela de MENU ---------------------------------------------------------------------------------
def sg_Menu():
    layoutMenu = [
        [sg.Text('Menu Principal', font='Arial 30', text_color='Red')],
        [sg.Text()],
        [sg.Button('CADASTROS')],
        [sg.Button('FERRAMENTAS')],
        [sg.Button('TÉCNICOS')],
        [sg.Button('RESERVAS')],
        [sg.Text()],
        [sg.Button('Sair', button_color='red', font='Arial 15')],
    ]
    
    janelaMenu = sg.Window('Tela Login', layout=layoutMenu, size=(300,300), element_justification='center', font='Arial 15')
    
    while True:
        event, values = janelaMenu.read()
        if event == 'CADASTROS':
            janelaMenu.close()
            sg_CadastroGeral()
        if event == 'Sair':
            sg.Exit()
            break


# ----------------------------------------------------------------------------------------------

def sg_CadastroGeral():
    layoutCadastroGeral = [
        [sg.Text('Cadastrar', font='Arial 30', text_color='Red')],
        [sg.Button('FERRAMENTAS'), sg.Button('TECNICOS')],
        [sg.Button('RESERVA')],
        [sg.Text()],
        [sg.Button('Voltar', button_color='red')],
        ]
        
    janelaCadastroGeral = sg.Window('CADASTRO', layout=layoutCadastroGeral, size=(300,300), element_justification='center', font='Arial 15')

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
            sg_Menu()
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
            [sg.Button('Cadastrar'), sg.Button('Voltar')] 
            ]

    janelaCadastroF = sg.Window('CADASTRO DE FERRAMENTAS', layout=layoutCadF, size=(300,300), element_justification='center', font='Arial 15')

    while True:
        event, values = janelaCadastroF.read()
        if event == 'Voltar':
            janelaCadastroF.close()
            sg_Menu()
            break

# ----------------------------------------------------------------------------------------------

# Tela de CADASTRO DE TECNICOS -----------------------------------------------------------------

def sg_CadastroT():
    layoutCadT = [ 
            [sg.Text('CPF'), sg.InputText()],
            [sg.Text('Nome'), sg.InputText()],
            [sg.Text('Sobrenome'), sg.InputText()],
            [sg.Text('Telefone'), sg.InputText()],
            [sg.Text('Turno'), sg.InputText()],
            [sg.Text('Equipe'), sg.InputText()],
            [sg.Button('Cadastrar'), sg.Button('Voltar')] 
            ]

    janelaCadastroT = sg.Window('CADASTRO DE FERRAMENTAS', layout=layoutCadT, size=(300,300), element_justification='center', font='Arial 15')

    while True:
        event, values = janelaCadastroT.read()
        if event == 'Voltar':
            janelaCadastroT.close()
            sg_Menu()
            break

# ----------------------------------------------------------------------------------------------

# Tela de RESERVAS -----------------------------------------------------------------------------

def sg_CadastroR():
    layoutCadR = [ 
            [sg.Text('Tecnico'), sg.InputText()],
            [sg.Text('Data da reserva'), sg.InputText()],
            [sg.Text('Data da devolução'), sg.InputText()],
            [sg.Button('Cadastrar'), sg.Button('Voltar')] 
            ]

    janelaCadastroR = sg.Window('CADASTRO DE FERRAMENTAS', layout=layoutCadR, size=(300,300), element_justification='center', font='Arial 15')

    while True:
        event, values = janelaCadastroR.read()
        if event == 'Voltar':
            janelaCadastroR.close()
            sg_Menu()
            break
# ----------------------------------------------------------------------------------------------

# 

