# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:06:55 2020

@author: jorge
"""


#! /usr/bin/env python
#  -*- coding: utf-8 -*-


import sys
import pyinputplus as pyip
from selenium import webdriver
import os, sys, autoit, getpass
from win32com.client import Dispatch
from time import sleep
from win32gui import GetWindowText, GetForegroundWindow
from cryptography.fernet import Fernet 

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

#import gmUITestS


pswrd, username, browsPic = '','',0

# GUI menu######################################################################################################################################################   
def vp_start_gui1():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    init1(root, top)
    root.mainloop()

def init1(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    init1(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
    
    
def TButton1Pressed():
    print('View Current Transcript (Unofficial)')
    browser= getBrowser(browsPic)
    exportTrans(browser, username, pswrd)

    
def TButton2Pressed():
    print('Export Current Transcript (PDF)')
    browser= getBrowser(browsPic)
    exportTrans(browser, username, pswrd, 1)
    
def TButton1_1Pressed():
    print('View Financial Aid Awarded For Current Term')
    browser= getBrowser(browsPic)
    viewFinAwrded(browser, username, pswrd)
    
def TButton1_2Pressed():
    print('Run Degree Evaluation')
    browser= getBrowser(browsPic)
    DegreeEval(browser, username, pswrd)

    
def TButton3Pressed():
    print('Export Current Class Schedule (PDF)')
    browser= getBrowser(browsPic)
    viewSchedule(browser, username, pswrd)

    
def TButton4Pressed():
    print('View Current Class Schedule')
    browser= getBrowser(browsPic)
    viewSchedule(browser, username, pswrd, 1)
    
def TButton5Pressed():
    print("Instant Course Registration (Must Know CRN's)")
    crns=getCRNs()   
    browser= getBrowser(browsPic)
    register(browser,crns,username,pswrd)
    
def TButton6Pressed():
    print('Save/Update Credentials')
    # os.system('python '+os.getcwd()+'\\CED1.py')
    os.system(os.getcwd()+'\\CED1.exe')
    pswrd, username, browsPic = getCreds()


class Toplevel1:
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

        top.geometry("600x450+564+342")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("GoldMiner v0.6")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label = tk.Label(top)
        self.Label.place(relx=0.3, rely=0.067, height=36, width=232)
        self.Label.configure(activebackground="#f9f9f9")
        self.Label.configure(activeforeground="black")
        self.Label.configure(background="#d9d9d9")
        self.Label.configure(disabledforeground="#a3a3a3")
        self.Label.configure(font="-family {Segoe UI} -size 13 -underline 1")
        self.Label.configure(foreground="#000000")
        self.Label.configure(highlightbackground="#d9d9d9")
        self.Label.configure(highlightcolor="black")
        self.Label.configure(text='''Main Menu''')

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.017, rely=0.156, relheight=0.133
                , relwidth=0.91)
        self.Message1.configure(anchor='w')
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Select an option to execute task. 
Please allow program to finish before interacting with browser.''')
        self.Message1.configure(width=546)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.033, rely=0.333, height=30, width=318)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''View Current Transcript (Unofficial)''')
        self.TButton1.configure(compound='left')
        self.TButton1.configure(command=TButton1Pressed)


        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.033, rely=0.4, height=30, width=318)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Export Current Transcript (PDF)''')
        self.TButton2.configure(compound='left')
        self.TButton2.configure(command=TButton2Pressed)

        self.TButton1_1 = ttk.Button(top)
        self.TButton1_1.place(relx=0.033, rely=0.467, height=30, width=318)
        self.TButton1_1.configure(takefocus="")
        self.TButton1_1.configure(text='''View Financial Aid Awarded For Current Term''')
        self.TButton1_1.configure(compound='left')
        self.TButton1_1.configure(command=TButton1_1Pressed)

        self.TButton1_2 = ttk.Button(top)
        self.TButton1_2.place(relx=0.033, rely=0.533, height=30, width=318)
        self.TButton1_2.configure(takefocus="")
        self.TButton1_2.configure(text='''Run Degree Evaluation''')
        self.TButton1_2.configure(compound='left')
        self.TButton1_2.configure(command=TButton1_2Pressed)

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.033, rely=0.6, height=30, width=318)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Export Current Class Schedule (PDF)''')
        self.TButton3.configure(command=TButton3Pressed)

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.033, rely=0.667, height=30, width=318)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''View Current Class Schedule''')
        self.TButton4.configure(command=TButton4Pressed)

        self.TButton5 = ttk.Button(top)
        self.TButton5.place(relx=0.033, rely=0.733, height=30, width=318)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Instant Course Registration (Must Know CRN's)''')
        self.TButton5.configure(command=TButton5Pressed)

        self.TButton6 = ttk.Button(top)
        self.TButton6.place(relx=0.033, rely=0.8, height=30, width=318)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''Save/Update Credentials''')
        self.TButton6.configure(command=TButton6Pressed)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.567, rely=0.289, relheight=0.2, relwidth=0.41)

        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''All exported document can be found in the file labeled "Exports" in the main program directory.''')
        self.Message2.configure(width=246)

        self.Message3 = tk.Message(top)
        self.Message3.place(relx=0.567, rely=0.467, relheight=0.4, relwidth=0.41)

        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''***WARNING*** Exporting another copy of the same document will overwrite the previouse version of it.

If you would like to keep both copies, rename or move older to a new folder before running export action.''')
        self.Message3.configure(width=246)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.8, rely=0.956, height=26, width=132)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''By Jorge Favela''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.8, rely=0.933, height=16, width=132)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''GoldMiner v0.6''')



# Welcome GUI ######################################################################################################################
def init2(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window2():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    
def vp_start_gui2():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel2 (root)
    init2(root, top)
    root.mainloop()

w = None
def create_Toplevel2(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel2 (w)
    init2(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel2():
    global w
    w.destroy()
    w = None

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

        top.geometry("600x450+660+210")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("GoldMiner v0.6 (Greeter)")
        top.configure(background="#d9d9d9")
        
        def dntStore():
            username = pyip.inputStr(prompt='Enter Goldmine Username (Your UTEP Email without "@miners.utep.edu"): ')
            pswrd=getpass.getpass()
            print('Choose installed browser:\n(1) Chrome\t(2) Firefox')
            browsPic= pyip.inputInt()
            destroy_window2()            
            
        def storeCreds():
            destroy_window2()
            # os.system('python '+ os.getcwd()+'\\CED1.py')
            os.system(os.getcwd()+'\\CED1.exe')
            pswrd, username, browsPic = getCreds()
            
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.0, rely=-0.044, relheight=0.156
                , relwidth=0.693)
        self.Message1.configure(anchor='w')
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''UTEP GoldMiner by Jorge Favela''')
        self.Message1.configure(width=416)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.017, rely=0.133, relheight=0.2
                , relwidth=0.893)
        self.Message2.configure(anchor='w')
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(font="-family {Segoe UI} -size 12")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Would you like to save time by storing your login credentials and browser preferance?''')
        self.Message2.configure(width=536)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.267, rely=0.4, height=50, width=268)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Yes, securely store my info!''')
        self.TButton1.configure(command=storeCreds)

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.267, rely=0.622, height=50, width=268)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''No, wipe my info when program exits.''')
        self.TButton2.configure(command=dntStore)




# Browser Function Methods#####################################################################################################################################        
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def getCreds():
    cred_filename = 'Crd.ini'
    key_file = 'key.key'
      
    key = '' 
      
    with open(key_file,'r') as key_in: 
        key = key_in.read().encode() 
        
    #os.remove(key_file) 
      
    f = Fernet(key) 
    with open(cred_filename,'r') as cred_in: 
        lines = cred_in.readlines() 
        config = {} 
        for line in lines: 
            tuples = line.rstrip('\n').split('=',1) 
            if tuples[0] in ('Username','Password','Browser'): 
                config[tuples[0]] = tuples[1] 
      
        passwd = f.decrypt(config['Password'].encode()).decode() 
        return passwd, config['Username'], int(config['Browser'])
    
    
def getBrowser(browsPic):
        if browsPic == 1:
            paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                     r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
            version = list(filter(None, [Get_Chrome_Version(p) for p in paths]))[0]
            cv=version[:2]
            return webdriver.Chrome(executable_path=os.getcwd()+"\\geko\\chromedriver"+cv+".exe")
        else:
            return webdriver.Firefox()
            
def printToPDF(BT):
    autoit.send("^p")
    sleep(4)
    if BT == "<class 'selenium.webdriver.chrome.webdriver.WebDriver'>": 
        autoit.send("{TAB 5}")
        sleep(1)
        autoit.send("{DOWN 5}")
        sleep(1)
        autoit.send('Save as PDF')
        sleep(1)
        autoit.send("{TAB 2}")
        sleep(1)
        autoit.send('{ENTER}')
        sleep(1)
        autoit.send("{TAB 4}")
        sleep(1)
        autoit.send('{ENTER}')
        sleep(3)
        autoit.control_click("Save As","[CLASS:ToolbarWindow32; INSTANCE:4]")   
        sleep(1)
        autoit.send(os.getcwd()+'\\Exports\\')
        sleep(1)
        autoit.send('{ENTER}')
        sleep(2)
        autoit.control_click("Save As","[CLASS:Button; INSTANCE:2]")   
        sleep(1)
    else:
        autoit.send('Microsoft Print To PDF')
        sleep(1)
        autoit.send('{ENTER}')
        sleep(2)
        autoit.send('Academic Transcript')
        sleep(2)
        autoit.control_click("Save Print Output As","[CLASS:ToolbarWindow32; INSTANCE:4]")   
        sleep(2)
        autoit.send(os.getcwd()+'\\Exports\\')
        sleep(1)
        autoit.send('{ENTER}')
        sleep(2)
        autoit.control_click("Save Print Output As","[CLASS:Button; INSTANCE:2]")   
        sleep(1)
    if GetWindowText(GetForegroundWindow()) == 'Confirm Save As':
        autoit.send('{LEFT}')
        sleep(1)
        autoit.send('{ENTER}')

    
def Get_Chrome_Version(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

# def dntStore():
#     username = pyip.inputStr(prompt='Enter Goldmine Username (Your UTEP Email without "@miners.utep.edu"): ')
#     pswrd=getpass.getpass()
#     print('Choose installed browser:\n(1) Chrome\t(2) Firefox')
#     browsPic= pyip.inputInt()
    
# def storeCreds():
#     os.system(os.getcwd()+'\\CED.exe')
#     pswrd, username, browsPic = getCreds()

def displayMenu():
    print("\n\t\t\t\t\tMain Menu\n")
    print("(1) View Current Transcript (Unofficial)\t\t(5) Export Current Transcript (PDF)\t")
    print("(2) Instant Course Registration (Must Know CRN's)\t(6) Run Degree Evaluation\t\t")
    print("(3) View Financial Aid Awarded For Current Term\t\t(7) View Current Class Schedule")
    print("(4) Export Current Class Schedule (PDF)\t\t\t(0) Exit")
    print("(10) Save/Change Credentials")
    
def getCRNs():
    print('Enter CRN for each course one at a time. ("0" when done)')
    crns=[]
    course= pyip.inputInt()
    while course != 0:
        crns.append(course)
        course= pyip.inputInt()
    return crns

def viewSchedule(browser, username, pswrd, E=0):
    browser.get('https://my.utep.edu/newgoldmine')
    browser.implicitly_wait(20)
    user = browser.find_element_by_id('usernameTextbox')
    passwrd = browser.find_element_by_id('passwordTextbox')
    user.send_keys(username)
    passwrd.send_keys(pswrd)
    passwrd.submit()
    browser.implicitly_wait(10)
    regLink = browser.find_element_by_xpath('/html/body/div[4]/table[2]/tbody/tr[2]/td[2]/a')
    regLink.click()
    browser.implicitly_wait(10)
    viewSchedLink = browser.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[5]/td[2]/a')
    viewSchedLink.click()
    if E==1:
        printToPDF(str(type(browser)))
        browser.quit()
    
def viewFinAwrded(browser, username, pswrd):
    browser.get('https://my.utep.edu/newgoldmine')
    browser.implicitly_wait(20)
    user = browser.find_element_by_id('usernameTextbox')
    passwrd = browser.find_element_by_id('passwordTextbox')
    user.send_keys(username)
    passwrd.send_keys(pswrd)
    passwrd.submit()
    browser.implicitly_wait(10)
    finAidLink = browser.find_element_by_xpath('/html/body/div[4]/table[2]/tbody/tr[1]/td[2]/a/img')
    finAidLink.click()
    browser.implicitly_wait(10)
    myAwrdLink = browser.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[1]/td[2]/a')
    myAwrdLink.click()
    byYearLink = browser.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[2]/td[2]/a')
    byYearLink.click()
    yearLink = browser.find_element_by_xpath('/html/body/div[4]/form/table/tbody/tr/td[2]/select/option[2]')
    yearLink.click()
    subLink = browser.find_element_by_xpath('/html/body/div[4]/form/input')
    subLink.click()
    overviewLink = browser.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[3]/a')
    overviewLink.click()
    
def register(browser, crns, username, pswrd):
    print('Registering...')
    browser.get('https://my.utep.edu/newgoldmine')
    browser.implicitly_wait(20)
    user = browser.find_element_by_id('usernameTextbox')
    passwrd = browser.find_element_by_id('passwordTextbox')
    user.send_keys(username)
    passwrd.send_keys(pswrd)
    passwrd.submit()
    browser.implicitly_wait(10)
    regLink = browser.find_element_by_xpath('/html/body/div[4]/table[2]/tbody/tr[2]/td[2]/a')
    regLink.click()
    browser.implicitly_wait(10)
    clsAdd = browser.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[3]/td[2]/a')
    clsAdd.click()
    browser.implicitly_wait(10)
    sub = browser.find_element_by_xpath('/html/body/div[4]/form/input')
    sub.click()
    browser.implicitly_wait(10)
    boxid = 'crn_id1'
    boxnum = 2
    box = browser.find_element_by_id(boxid)
    for i in crns:
        box.send_keys(i)
        boxid=boxid[:-1]+str(boxnum)
        boxnum+=1
        browser.implicitly_wait(10)
        box = browser.find_element_by_id(boxid)
    sub=browser.find_element_by_xpath('/html/body/div[4]/form/input[19]')
    sub.click()
    
def exportTrans(browser, username, pswrd, E=0):
    browser.get('https://my.utep.edu/newgoldmine')
    browser.implicitly_wait(20)
    user = browser.find_element_by_id('usernameTextbox')
    passwrd = browser.find_element_by_id('passwordTextbox')
    user.send_keys(username)
    passwrd.send_keys(pswrd)
    passwrd.submit()
    browser.implicitly_wait(10)
    recLink = browser.find_element_by_xpath('/html/body/div[4]/table[2]/tbody/tr[4]/td[2]/a/img')
    recLink.click()
    browser.implicitly_wait(10)
    transLink = browser.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[4]/td[2]/a')
    transLink.click()
    browser.implicitly_wait(10)
    subLink = browser.find_element_by_xpath('/html/body/div[4]/form/input')
    subLink.click()
    browser.implicitly_wait(10)
    if E==1:
        printToPDF(str(type(browser)))
        browser.quit()

def DegreeEval(browser, username, pswrd):
    browser.get('https://my.utep.edu/newgoldmine')
    browser.implicitly_wait(20)
    user = browser.find_element_by_id('usernameTextbox')
    passwrd = browser.find_element_by_id('passwordTextbox')
    user.send_keys(username)
    passwrd.send_keys(pswrd)
    passwrd.submit()
    browser.implicitly_wait(10)
    recLink = browser.find_element_by_xpath('/html/body/div[4]/table[2]/tbody/tr[4]/td[2]/a/img')
    recLink.click()
    browser.implicitly_wait(10)
    degEvalLink = browser.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[7]/td[2]/a')
    degEvalLink.click()
    browser.implicitly_wait(10)
    subLink = browser.find_element_by_xpath('/html/body/div[4]/form/table/tbody/tr[3]/td[1]/input')
    subLink.click()
    browser.implicitly_wait(10)
    subLink = browser.find_element_by_xpath('/html/body/div[4]/form/table/tbody/tr[2]/td[2]/a')
    subLink.click()
    browser.implicitly_wait(10)
        
        
        
        
# Main ######################################################################################################################################################        
# if __name__ == '__main__':
    # vp_start_gui()
# pswrd, username, browsPic = '','',0


# print("UTEP GoldMiner by Jorge Favela\n")
if os.path.exists('Crd.ini'):
    pswrd, username, browsPic = getCreds()
else:
    vp_start_gui2()
    # print('Would you like to save time by storing your login credentials and browser preferance?\n(1) Yes, securly store my info!\n(2) No, wipe my info when program exits')
    # store = pyip.inputInt(prompt='Enter desired choice (1 or 2): ')
    # print()
    # if store==1:
    #     # os.system('python '+ os.getcwd()+'\\CED.py')
    #     os.system(os.getcwd()+'\\CED.exe')
    #     pswrd, username, browsPic = getCreds()
    # else:
    #     username = pyip.inputStr(prompt='Enter Goldmine Username (Your UTEP Email without "@miners.utep.edu"): ')
    #     pswrd=getpass.getpass()
    #     print('Choose installed browser:\n(1) Chrome\t(2) Firefox')
    #     browsPic= pyip.inputInt()
# end='y'
# while end!='n':
vp_start_gui1()
        # displayMenu()
        # menuOp= pyip.inputInt()  
        
    #     if menuOp==0:
    #         break
    #     elif menuOp==1:
    #         browser= getBrowser(browsPic)
    #         exportTrans(browser, username, pswrd)
    #     elif menuOp==2:
    #         crns=getCRNs()   
    #         browser= getBrowser(browsPic)
    #         register(browser,crns,username,pswrd)
    #     elif menuOp==3:
    #         browser= getBrowser(browsPic)
    #         viewFinAwrded(browser, username, pswrd)
    #     elif menuOp==4:
    #         browser= getBrowser(browsPic)
    #         viewSchedule(browser, username, pswrd, 1)
    #     elif menuOp==5:
    #         browser= getBrowser(browsPic)
    #         exportTrans(browser, username, pswrd, 1)
    #     elif menuOp==6:
    #         browser= getBrowser(browsPic)
    #         DegreeEval(browser, username, pswrd)
    #     elif menuOp==7:
    #         browser= getBrowser(browsPic)
    #         viewSchedule(browser, username, pswrd)
    #     elif menuOp==10:
    #         os.system(os.getcwd()+'\\CED.exe')
    #         pswrd, username, browsPic = getCreds()
    #     else:
    #         print('Please enter the number for your desired option. (0-7 or 10)')   
    #     end=pyip.inputStr(prompt='Back to main menu? (y/n): ')
    #     if menuOp<10 and menuOp>0:
    #         browser.quit()
    #     print('******************************************************************')
    # print('Goodbye, hope it helped! :)')
    
