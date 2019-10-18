from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random 



class aleatorio(BoxLayout):
    girar=0
    total= 0
    def rodar(self,valor):
        girar = (str(random.randint(1,valor)))
        self.total+=str(girar)
        return self.total
    
 #   def total(self):
     
    #    return self.total
        
        


class teste(App):
    def build(self):
        return aleatorio()


teste().run()
