# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:05:34 2020

@author: naveen
"""


import pandas as pd
import os

Golden_directory=r'D:\Users\naveen\work\golden'
temp_directory=r'D:\Users\naveen\work\temp'


def checkfile(Golden_directory,temp_directory):
    for filename in os.listdir(Golden_directory):
        for tempFilename in os.listdir(temp_directory):
             if tempFilename==filename:
                 performDQ(Golden_directory+'\\'+filename,temp_directory+"\\"+tempFilename)
                 
def performDQ(filename,tempFilename):
    if(filename.endswith('.xls') or filename.endswith('.xlsm')  or filename.endswith('.xlsx')):
        print('here')
        all_dfs_golden = pd.read_excel(filename, sheet_name=None)
        all_dfs_temp = pd.read_excel(tempFilename, sheet_name=None)
        if(checkSheetNames(all_dfs_golden,all_dfs_temp)): 
            df_golden = pd.concat(all_dfs_golden, ignore_index=True)
            df_temp= pd.concat(all_dfs_temp, ignore_index=True)
            if(df_golden.equals(df_temp)):
                 print("Both File identical: "+filename,tempFilename)
            else:
                 print("files have diffrent contains: "+filename,tempFilename)
            
        else:
            print("files have diffrent caontains: "+filename,tempFilename)
    elif(filename.endswith('.csv') or filename.endswith('.txt')):
         CheckCsvFile(filename,tempFilename)
    else:
        print('unwanted File'+filename)
         
         
        
        
        
def checkSheetNames(sheetsGolden,SheetsTemp):
    if(list(sheetsGolden.keys()).sort()== list(SheetsTemp.keys()).sort()):
        return True
    else:
        return False
def CheckCsvFile(filename,tempFilename):
    with open('filename', 'r') as t1, open('tempFilename', 'r') as t2:
        
        fileone = t1.readlines()
        filetwo = t2.readlines()
        for line in filetwo:
            if line not in fileone:
                print("files have diffrent contains: "+filename,tempFilename)
                
def main():
     checkfile(Golden_directory,temp_directory)
           
                
if __name__ == "__main__":
    main()
        
        
        
        

    
                 
            













