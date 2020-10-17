# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:31:24 2020
Last modified on Sat May  2 21:23:27 2020
@title: GPA Calculator
@author: Jorge A Favela
Purpose of program: To sereve as a tool to calculate the estimated GPA one might have
based on current gpa and current semesters projected grades
"""
import math

L=['A','B','C','D','F']
P=[4,3,2,1,0]

def lc2p(letter, cred): # Points calculated from etter grade and credit value 
    for i in range(len(L)):
        if L[i]==letter:
            return cred * P[i]
    
def truncate(f,n):
    return math.floor(f * 10 ** n) / 10 ** n

if __name__ == "__main__":
    print('GPA Estimater:\n***Information from your most current transcript is required for accurate results***')
    cur_gpa=float(input('Please enter your current gpa (It is important that this be exactly what it says on your transcript): '))
    cred_hrs=float(input('Enter total "GPA Hours" according to transcript: '))
    gpa_pts= float(math.ceil((cur_gpa * cred_hrs)))
    print('\n***********************************************************************************')
    print('Next, for each course currently being taken, enter the letter grade you expect to earn followed by the number of ',end='')
    print('credits the class is worth. It is important that you enter every class that will be factored into your gpa at the end of this semester.\n\nEnter "done 0" when all classes have been entered')
    print('\n***********************************************************************************')
    gdCred=[]
    g=''
    c=0
    cnt=1
    while g != 'done':
        print('\nGrades and credits entered')
        print('\n#        Grade     Credits')
        for i in range(len(gdCred)):
            print(*gdCred[i], sep='         ')
        s= input('\nEnter the letter grade and credit value of course sepatated by a space (Ex. A 4): ')
        sl=s.split(sep=' ')
        g=sl[0]
        c=int(sl[1])
        if g.upper()=='DONE':
            break
        if g.upper() not in L:
            print('The letter grade must be either an A B C D or F\nTry again')
        else:
            if c not in P:
                print('The credit value must be either a 4 3 2 or 1\nTry again')
            else:
                gdCred.append([cnt,g.upper(),c])
                cnt+=1
    newgpa_pts=gpa_pts
    newcred_hrs=cred_hrs
    op='Y'
    while op == 'Y':
        for i in gdCred:
            newgpa_pts+= lc2p(i[1],i[2])
            newcred_hrs+=i[2]
        proj_gpa = truncate(newgpa_pts/newcred_hrs,2)
        print('\nEstimated GPA after earning the above grades for the current semester:  ',proj_gpa)
        print('\n***********************************************************************************')
        op=(input('Would you like to change one or more of the grades given and run again? (y/n): ')).upper()
        if op == 'Y':
            num=-1
            while num!=0:
                num=int(input('Enter the # of the grade youd like to change or "0" when finished: '))
                if num >len(gdCred):
                    print('\nThere is no number',num,'in the list. Please choose a number from the list of grades')
                else:
                    if num!=0:
                        newGd=''
                        while newGd.upper() not in L:
                            newGd= input('Enter the letter grade to replace it with:  ')
                            if newGd.upper() not in L:
                                print('The letter grade must be either an A B C D or F\nTry again')
                        (gdCred[num-1])[1]=newGd.upper()
                print('\nGrades and credits entered')
                print('\n#        Grade     Credits')
                for i in range(len(gdCred)):
                    print(*gdCred[i], sep='         ')
            newgpa_pts=gpa_pts
            newcred_hrs=cred_hrs
            print('\n***********************************************************************************')
        else:
            print('\n***********************************************************************************')
            print('\nI hope it helped! Good luck!\nProgram Author: Jorge Favela\n\nHit ENTER to exit') 
            x=input('')
            if x=='':
                break
                
    