from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_cb = CallbackData('button','type','action','data', sep=';')

def setActionFor(state):
    def decorator(func):
        if type(state) == list:
            for s in state:
                s.setAction(func)
        else:
            state.setAction(func)
    return decorator

class Buttons:
    def __init__(self, has_back_button=False):
        self.markup = InlineKeyboardMarkup()
        self.has_back_button = has_back_button

    def add(self,text:str,action:str,data='-',btype = 'main'):
        self.markup.add(InlineKeyboardButton(text, callback_data=button_cb.new(type=btype, action=action, data=data)))
    
    def addLink(self, text:str, action:str, link: str, data='-', btype = 'main'):
        self.markup.add(InlineKeyboardButton(text, url=link, callback_data=button_cb.new(type=btype, action=action, data=data)))

    def row(self,buttons):
        '''[[text,action,data='-',type='main'],[text2,action2,data2='-',type='main']]'''
        mButtons = []
        for button in buttons:
            data = button[2] if len(button)>2 else '-'
            btype = button[3] if len(button)>3 else 'main'
            mButtons.append(InlineKeyboardButton(button[0],callback_data=button_cb.new(type=btype, action=button[1], data=data)))
        self.markup.row(*mButtons)

    def getMarkup(self):
        if self.has_back_button:
            self.add('🔙','back')
        return self.markup

def addLeftRightArrows(markup: Buttons, index, n, data):
    arrows = []
    if index > 0:
        arrows.append(['⬅️', 'left', f'{index-1}:{data}', 'master_service_arrow'])
    if index < n-1:
        arrows.append(['➡️', 'right', f'{index+1}:{data}', 'master_service_arrow'])
    n_arrows = len(arrows)
    if n_arrows == 1:
        markup.add(*arrows[0])
    elif n_arrows == 2:
        markup.row(arrows)