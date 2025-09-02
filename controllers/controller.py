
import Calculo as clc


class Controller:
    def __init__(self,view):
        self.view = view

    def click_comboox(self):
        produto = self.view.combo.get()
        self.view.lblresultado.comfigure(text= produto)
