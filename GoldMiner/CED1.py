# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:28:01 2020

@author: Jorge Favela
"""

#CreateCred.py 
#Creates a credential file. 
from cryptography.fernet import Fernet 
import pyinputplus as pyip
import re 
import ctypes 
import time 
import os 
import sys 
import getpass

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

   
# GUI #####################################################################################################################
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

# Support ###############################################################################################################
def set_Tk_var():
    global tch52
    tch52 = tk.StringVar()
    global tch54
    tch54 = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w2, top_level, root
    w2 = gui
    top_level = top
    root = top

def CredDone():
    # print('Credentials_support.CredDone')
    sys.stdout.flush()
    creds.username = w2.TEntry1.get() 
    creds.password = w2.TEntry1_1.get()
    creds.create_cred()
    destroy_window()



def chrome():
    print('Credentials_support.chrome')
    sys.stdout.flush()
    creds.brwsr_pref = 1


def firefox():
    print('Credentials_support.firefox')
    sys.stdout.flush()
    creds.brwsr_pref = 2


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
#######################################################################################################################

def vp_start_gui2():
    '''Starting point when module is the main routine.'''
    global val, w2, root
    root = tk.Tk()
    set_Tk_var()
    top = Toplevel2 (root)
    init(root, top)
    root.mainloop()

w2 = None
def create_Toplevel2(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel2(root, *args, **kwargs)' .'''
    global w2, w2_win, root
    #rt = root
    root = rt
    w2 = tk.Toplevel (root)
    set_Tk_var()
    top = Toplevel2 (w2)
    init(w2, top, *args, **kwargs)
    return (w2, top)

def destroy_Toplevel2():
    global w2
    w2.destroy()
    w2 = None

class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("533x224+732+389")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("GoldMiner v0.6 (Credentials)")
        top.configure(background="#d9d9d9")

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.227, rely=0.277, relheight=0.156
                , relwidth=0.518)
        self.TEntry1.configure(foreground="#000000")
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="fleur")

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.038, rely=0.237, height=39, width=102)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Username:''')

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=-0.019, rely=0.0, relheight=0.237
                , relwidth=1.026)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Enter Goldmine Username (Your UTEP Email without '@miners.utep.edu'), password, and select your prefered browser below.''')
        self.Message1.configure(width=543)

        self.TEntry1_1 = ttk.Entry(top)
        self.TEntry1_1.place(relx=0.227, rely=0.473, relheight=0.143
                , relwidth=0.522)
        self.TEntry1_1.configure(foreground="#000000")
        self.TEntry1_1.configure(takefocus="")
        self.TEntry1_1.configure(cursor="fleur")

        self.TLabel2_1 = ttk.Label(top)
        self.TLabel2_1.place(relx=0.038, rely=0.433, height=39, width=102)
        self.TLabel2_1.configure(background="#d9d9d9")
        self.TLabel2_1.configure(foreground="#000000")
        self.TLabel2_1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.TLabel2_1.configure(relief="flat")
        self.TLabel2_1.configure(anchor='w')
        self.TLabel2_1.configure(justify='left')
        self.TLabel2_1.configure(text='''Password:''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(top)
        self.TCheckbutton1.place(relx=0.263, rely=0.714, relwidth=0.152
                , relheight=0.0, height=23)
        self.TCheckbutton1.configure(variable=tch52)
        self.TCheckbutton1.configure(command=chrome)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Chrome''')

        self.TCheckbutton2 = ttk.Checkbutton(top)
        self.TCheckbutton2.place(relx=0.563, rely=0.714, relwidth=0.129
                , relheight=0.0, height=23)
        self.TCheckbutton2.configure(variable=tch54)
        self.TCheckbutton2.configure(command=firefox)
        self.TCheckbutton2.configure(takefocus="")
        self.TCheckbutton2.configure(text='''Firefox''')

        self.TLabel2_2 = ttk.Label(top)
        self.TLabel2_2.place(relx=0.038, rely=0.67, height=23, width=97)
        self.TLabel2_2.configure(background="#d9d9d9")
        self.TLabel2_2.configure(foreground="#000000")
        self.TLabel2_2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.TLabel2_2.configure(relief="flat")
        self.TLabel2_2.configure(anchor='w')
        self.TLabel2_2.configure(justify='left')
        self.TLabel2_2.configure(text='''Browser:''')

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.769, rely=0.759, height=30, width=98)
        self.TButton1.configure(command=CredDone)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Finished''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)







class Credentials(): 
   
    def __init__(self): 
        self.__username = "" 
        self.__key = "" 
        self.__password = "" 
        self.__key_file = 'key.key'
        self.__brwsr_pref = 1
        # self.__time_of_exp = -1
   
#---------------------------------------- 
# Getter setter for attributes 
#---------------------------------------- 
    
    @property
    def username(self): 
        return self.__username 
   
    @username.setter 
    def username(self,username): 
        while (username == ''): 
            username = input('Username cannot be blank:') 
        self.__username = username 
   
    @property
    def password(self): 
        return self.__password 
   
    @password.setter 
    def password(self,password): 
        self.__key = Fernet.generate_key() 
        f = Fernet(self.__key) 
        self.__password = f.encrypt(password.encode()).decode() 
        del f 
   
    @property
    def brwsr_pref(self): 
        return self.__brwsr_pref 
   
    @brwsr_pref.setter 
    def brwsr_pref(self,brwsr_pref): 
        self.__brwsr_pref = brwsr_pref 
    
    # @property
    # def expiry_time(self): 
    #     return self.__time_of_exp 
   
    # @expiry_time.setter 
    # def expiry_time(self,exp_time): 
    #     if(exp_time >= 2): 
    #         self.__time_of_exp = exp_time 
   
   
    def create_cred(self): 
        """ 
        This function is responsible for encrypting the password and create  key file for 
        storing the key and create a credential file with user name and password 
        """
   
        cred_filename = 'Crd.ini'
   
        with open(cred_filename,'w') as file_in: 
            file_in.write("#Credential file:\nUsername={}\nPassword={}\nBrowser={}\n"
            .format(self.__username,self.__password,self.__brwsr_pref)) 
            file_in.write("++"*20) 
   
   
        #If there exists an older key file, This will remove it. 
        if(os.path.exists(self.__key_file)): 
            os.remove(self.__key_file) 
   
        #Open the Key.key file and place the key in it. 
        #The key file is hidden. 
        try: 
   
            os_type = sys.platform 
            if (os_type == 'linux'): 
                self.__key_file = '.' + self.__key_file 
   
            with open(self.__key_file,'w') as key_in: 
                key_in.write(self.__key.decode()) 
                #Hidding the key file. 
                #The below code snippet finds out which current os the scrip is running on and does the taks base on it. 
                if(os_type == 'win32'): 
                    ctypes.windll.kernel32.SetFileAttributesW(self.__key_file, 2) 
                else: 
                    pass
   
        except PermissionError: 
            os.remove(self.__key_file) 
            print("A Permission error occurred.") 
            sys.exit() 
   
        self.__username = "" 
        self.__password = "" 
        self.__key = "" 
        self.__key_file 
   
   

   
# Creating an object for Credentials class 
creds = Credentials() 
vp_start_gui2()
#Accepting credentials 
# creds.username = input("Enter Goldmine Username (Your UTEP Email without '@miners.utep.edu'): ") 
# creds.password = getpass.getpass()
# print("How long would you like credentials saved for? \n(1) 1 WEEK\n(2) 1 MONTH\n(3) FOREVER") 
# op=input("Enter option(1,2 or 3): ")
# if op == '1':
#     creds.expiry_time = 10080
# elif op == '2':
#     creds.expiry_time = 40800
# else:
#     creds.expiry_time = -1
# print('\nChoose installed browser:\n(1) Chrome\t(2) Firefox')
# creds.brwsr_pref = pyip.inputInt()

#calling the Credit 
# creds.create_cred() 
   
   
# if not(creds.expiry_time == -1): 
#     os.startfile('expire.py') 
    
   
