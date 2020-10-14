# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:15:06 2020

@name: Automatic Budget Transfer Tool
@author: Jorge Favela

"""
from openpyxl import load_workbook
import win32com.client, win32com.client.makepy, os, winerror, pandas as pd, errno, re
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
from openpyxl import load_workbook
from openpyxl.styles import Alignment


def convertData(filename,kc):
    lines=[]
    dsf = load_workbook(filename=filename)
    sheet=dsf.active
    objs=sheet[kc]
    rules=[i.value for i in objs]
    # for i in rules:
    #     print(i)
    cnt=0
    for line in rules:
        cnt+=1
        if line == None:
            break
        # if cnt==0:
        #     break
        # print(line)
        if line[0]=='-':
            lines.append([cnt,['0']])
        else:
            AN=[]
            # print(len(line))
            if len(line)==11:
                AN=[line[0:11]]
                lines.append([cnt,AN])
            elif len(line)==9:
                AN=[line[0:9]]
                lines.append([cnt,AN])
            # elif line=='300E':
            #     AN=['300-30-1062','300-30-1063','300-30-1064','300-30-1065','300-30-1066','300-30-1067','300-30-1070','300-30-1080','300-31-1076','300-31-1077','300-31-1078','300-31-1080','300-31-1081']
            #     lines.append([cnt,AN])
            # elif line=='300R':
            #     AN=['300-40-5110','300-40-5190','300-40-5195','300-44-5110','300-44-5190','300-44-5195','300-47-5120','300-47-5190','300-48-5110','300-49-5120','300-49-5190','300-50-1100','300-50-1140','300-50-1165','300-50-4050','300-50-5130','300-50-5190','300-51-5110','300-53-5110','300-53-5120','300-94-5110','300-97-5120','300-97-5190','300-98-5110','300-98-5120','300-98-5180','300-98-5190','300-98-5195','300-98-5200','300-99-5120','300-99-5190','300-99-5195']
            #     lines.append([cnt,AN])
            else:
                # print('line:',line)
                num=line.split(' ')
                # print('num:',num)
                for i in num:
                    if i=='\n' or i=='':
                        break
                    if i[0]=='A':
                        AN.append('Account Number')
                        break
                    w=i[7:]
                    # print('w',w)
                    st=i[0:7]
                    # print('st',st)
                    en=''
                    for j in range(len(w)):
                        if w[j]=='/':
                            AN.append(st+en)
                            # print('number:',st+en)
                            en=''
                        else:
                            en=en+w[j]
                        if j==(len(w)-1):
                            AN.append(st+en)
                            # print('number:',st+en)
                            en=''
                lines.append([cnt,AN])
    # for i in lines:
    #     print(i)
    return lines


def compare(lines,Data):
    vals=[0.00 for i in range(len(lines)+1)]
    for rec in Data:
        for l in lines:
            if rec[0] in l[1]:
                # print(rec[0])
                # print(rec[1])
                vals[l[0]]+=rec[1]
                break
    return [round(num,0) for num in vals]

def pdf2excel(pdFilename):
    excel_file = "pdf2excel.xlsx"
    ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)
    src = os.path.abspath(pdFilename)
    win32com.client.makepy.GenerateFromTypeLibSpec('Acrobat')
    adobe = win32com.client.DispatchEx('AcroExch.App')
    avDoc = win32com.client.DispatchEx('AcroExch.AVDoc')
    avDoc.Open(src, src)
    pdDoc = avDoc.GetPDDoc()
    jObject = pdDoc.GetJSObject()
    jObject.SaveAs(excel_file, "com.adobe.acrobat.xlsx")
    avDoc.Close(-1)
    pdDoc.Close()
        
def getNewData(pdFilename):
    pdf2excel(pdFilename)
    workbook = load_workbook(filename=".\\input\\pdf2excel.xlsx")
    sheet = workbook.active
    Data=[]
    for value in sheet.iter_rows(max_col=2,values_only=True):
        Data.append(value)
    # for i in Data:
    #     print(i)
    return Data

def insert2sheet(values,filename,outName,ac):
    #Target sheet: "Q3 DFA Submission"
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
    # kc=input('Enter column in .xlsx file that key values are located (Capital Letter):') # K
    # ac=input('Enter column in .xlsx file that The amounts are to be located (Capital Letter):') # D
    datFile=input('Enter the name of the pdf exported from caselle including the ".pdf" extension:') # data.pdf
    datFile='.\\INPUT\\'+datFile
    outName=input('Enter desired name for final DFA file including ".xlsx" extenion:')
    outName='.\\OUTPUT\\'+outName
    values=compare(convertData(filename,'D'),getNewData(datFile))
    # for i in values:
    #     print(i)
    insert2sheet(values,filename,outName,'D')
    print('\nSuccess! Your file has been saved in the "OUTPUT" folder as"',outName,'"\nHope it helped!\nEnter to exit program')
    bye=input('')
    if bye:
        print()
                   