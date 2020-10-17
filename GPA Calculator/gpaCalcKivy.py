# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:37:39 2020

@author: jorge
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class MainApp(App):
    def build(self):
        self.state=0
        self.curgpa=0.0
        self.pts=0
        self.cred=0
        self.gdCred=[]
        self.credit = ["1", "2", "3", "4", "5","6","7","8","9","0","."]
        self.last_was_credit = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=True, readonly=True, halign="right",size_hint=(1,1.8)
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["A", "B", "1", "2", "3"],
            ["C", "D", "4", "5", "6"],
            ["F", "", "7", "8", "9"],
            ["Clear","Add","Next","0","."],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        done_button = Button(
            text="Done", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.solution.text='Please enter current GPA\n"Next" to continue'
        done_button.bind(on_press=self.on_done)
        main_layout.add_widget(done_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text == "Clear":
            # Clear the solution widget
            self.solution.text = ""                        
        if self.state==0:
            if button_text == 'Next' and current!='Please enter current GPA\n"Next" to continue':
                self.curgpa=float(current)
                self.solution.text='Great! Please enter current "Quality Points"\n"Next" to continue'
                self.state=1
            elif button_text!='Next'and button_text in self.credit:
                if current=='Please enter current GPA\n"Next" to continue':
                        current=''
                new_text = current + button_text
                self.solution.text = new_text
            else:
                return
        
        elif self.state==1:
            if button_text == 'Next' and current!='Great! Please enter current"Quality Points"\n"Next" to continue':
                self.pts=float(current)
                self.cred= self.pts/self.curgpa
                self.solution.text='Great! Now for each class being taken this semester\nenter the letter grade you expect to earn followed by the\nnumber of credits that class is worth\nPush "Add" after entering the values for each class\n"Next" when all classes have been entered'
                self.state=2
            elif button_text!='Next':
                if current=='Great! Please enter current "Quality Points"\n"Next" to continue':
                        current=''
                new_text = current + button_text
                self.solution.text = new_text
            else:
                return
        
        elif self.state==2:
            if button_text == "Add":
                v=self.solution.text.split(' ')
                print(v)
                self.gdCred.append([v[1],int(v[2])])
                self.solution.text='Class added!'
            elif button_text=="Next":
                self.solution.text = 'Entered\n'
                text = self.solution.text
                for i in self.gdCred:
                    self.solution.text+= i[0]+' '+str(i[1])+'\n'
                self.solution.text+='\nIf correct, press "Done" to continue'
                self.state=3
            elif current and (
                self.last_was_credit and button_text in self.credit):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.credit:
                # First character cannot be an operator
                return
            else:
                if current=='Class added!' or len(current)>10:
                    current=''
                new_text = current + ' ' + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_credit = self.last_button in self.credit

    def on_done(self, instance):
        if self.state==3:
            L=['A','B','C','D','F']
            P=[4,3,2,1,0]
            for i in self.gdCred:
                letter=i[0]
                cred=i[1]
                for j in range(len(L)):
                    if L[j]==letter:
                        self.pts+= cred * P[j]
                self.cred+=i[1]
            newtxt=str(math.floor((self.pts/self.cred) * 10 ** 2) / 10 ** 2)
            self.solution.text='Projected GPA: '+newtxt
            self.state=0
            self.curgpa=0.0
            self.pts=0
            self.cred=0
            self.gdCred=[]
                

if __name__ == "__main__":
    app = MainApp()
    app.run()
