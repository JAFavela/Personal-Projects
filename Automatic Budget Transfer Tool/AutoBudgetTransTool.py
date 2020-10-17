# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:15:06 2020

@name: Automatic Budget Transfer Tool
@author: Jorge Favela

"""
from openpyxl import load_workbook
import win32com.client, win32com.client.makepy, os, winerror
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
from openpyxl import load_workbook
from openpyxl.styles import Alignment


def convertData(filename,kc):
    lines=[]
    dsf = load_workbook(filename=filename) # Opens excel file
    sheet=dsf.active
    objs=sheet[kc]
    rules=[i.value for i in objs]  # Reads rules from excel file to a list
    cnt=0
    for line in rules: # Iterates through list and reformats rules to a usable list of rules
        cnt+=1
        if line == None:
            break
        if line[0]=='-':
            lines.append([cnt,['0']])
        else:
            AN=[]
            if len(line)==11:
                AN=[line[0:11]]
                lines.append([cnt,AN])
            elif len(line)==9:
                AN=[line[0:9]]
                lines.append([cnt,AN])
            else:
                num=line.split(' ')
                for i in num:
                    if i=='\n' or i=='':
                        break
                    if i[0]=='A':
                        AN.append('Account Number')
                        break
                    w=i[7:]
                    st=i[0:7]
                    en=''
                    for j in range(len(w)):
                        if w[j]=='/':
                            AN.append(st+en)
                            en=''
                        else:
                            en=en+w[j]
                        if j==(len(w)-1):
                            AN.append(st+en)
                            en=''
                lines.append([cnt,AN])
    return lines # Returns ready to use list of rules  

def compare(lines,Data): # Creates list of values calculated from new data and list of rules
    vals=[0.00 for i in range(len(lines)+1)]
    for rec in Data:
        for l in lines:
            if rec[0] in l[1]:
                vals[l[0]]+=rec[1]
                break
    return [round(num,0) for num in vals]

def pdf2excel(pdFilename): # Reads data from a PDF and convertsa it to an excel file
    excel_file = "pdf2excel.xlsx"
    ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)
    src = os.path.abspath(pdFilename)
    win32com.client.makepy.GenerateFromTypeLibSpec('Acrobat')
    avDoc = win32com.client.DispatchEx('AcroExch.AVDoc')
    avDoc.Open(src, src)
    pdDoc = avDoc.GetPDDoc()
    jObject = pdDoc.GetJSObject()
    jObject.SaveAs(excel_file, "com.adobe.acrobat.xlsx")
    avDoc.Close(-1)
    pdDoc.Close()
        
def getNewData(pdFilename): # Gets new data from excel sheet and puts it in a list ready to use
    pdf2excel(pdFilename)
    workbook = load_workbook(filename=".\\input\\pdf2excel.xlsx")
    sheet = workbook.active
    Data=[]
    for value in sheet.iter_rows(max_col=2,values_only=True):
        Data.append(value)
    return Data

def insert2sheet(values,filename,outName,ac): # Takes newly calculated data and inserts it into formated excel sheet ready to submit to state
    dsf = load_workbook(filename=filename)
    sheet=dsf.active
    col=ac
    row=-0
    for amt in values:
        if row>1:
            cell=col+str(row)
            sheet[cell].value=float(amt)
            sheet[cell].alignment = Alignment(horizontal="right")
            sheet[cell].number_format = 'General'
        row+=1
    dsf.save(outName)
                    
if __name__ == "__main__":
    print('Please make sure both files are in their required format and in the "INPUT" folder')
    filename = input('Enter the name of the DFA template with the keys including the ".xlsx" extension:') # QR.xlsx
    filename ='.\\INPUT\\'+ filename
    datFile=input('Enter the name of the pdf exported from caselle including the ".pdf" extension:') # data.pdf
    datFile='.\\INPUT\\'+datFile
    outName=input('Enter desired name for final DFA file including ".xlsx" extenion:')
    outName='.\\OUTPUT\\'+outName
    values=compare(convertData(filename,'D'),getNewData(datFile))
    insert2sheet(values,filename,outName,'D')
    print('\nSuccess! Your file has been saved in the "OUTPUT" folder as"',outName,'"\nHope it helped!\nEnter to exit program')
    bye=input('')
    if bye:
        print()
                   