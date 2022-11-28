import eel
import contato
import pyautogui 

@eel.expose    
def cadastrarContato(nome, email, telefone):
    contato.gravar(nome, email, telefone)

@eel.expose
def listar():
    return contato.listar()

@eel.expose
def buscar(busca):
    return contato.buscar(busca)

@eel.expose 
def deletar(id):
    contato.deletar(id)

@eel.expose
def editar(id, nome, email, telefone):
    contato.editar(id, nome, email, telefone)


eel.init('web')
eel.start('main.html', size=(pyautogui.size()))
