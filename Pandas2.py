# script creat xlsx file and write data in that file

import os
import fnmatch
from sys import *
import xlsxwriter

def ExcelCreate(name):
    workbook = xlsxwriter.Workbook(name)

    worksheet = workbook.add_worksheet()

    worksheet.write('A1','Name')
    worksheet.write('B1','Collage')

    worksheet.write('C1','Mail Id')

    worksheet.write('D1','Mobile')
    worksheet.write('Mobile','731978327494')

    workbook.close()



def main():
    print("Application Name" +argv[0])

    if(len(argv)!= 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h" or argv[1] =="-H"):

        print("script creat xlsx file and write data in that file")
        exit()

    if(argv[1]=="-u" or argv[1] =="-U"):
        print("Usage : ApplicationName Name_Of_FIle")
        exit()
    
    try:
        ExcelCreate(argv[1])
    except Exception:
        print("Error : Invalid Arguments")
    
    

if __name__ =="__main__":
    main()