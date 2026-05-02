#bouton de menu
class Button:
    def __init__(self,position, text, font , color, button_list):
        self.position= position
        self.text= text
        self.font = font
        self.color = color
        button_list.append(self)
        print()
        # do something