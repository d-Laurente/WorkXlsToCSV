#test program to download photos and shove them in a directory
import os
import shutil 
# import barcode
from xlrd import open_workbook
from googleImagesDownloader import *
from barcode.writer import ImageWriter


'''
	This is a comment
'''
def moveImToFolder():
    # Path of the 
    # source: "/mnt/c/Users/derri/Desktop/Coding/work/downloads/"
    # destination: "/mnt/c/Users/derri/Desktop/Coding/work/Covers"
    source = os.getcwd() + "/downloads/"
    destination = os.getcwd() + "/Covers"

    print("Source: " + source)
    print("Destination" + destination)

    if not os.path.exists(destination):
        os.makedirs(destination)

    i = 0

    for f in os.listdir(source):
        i+=1
        imgPath = source + f + "/"
        print(imgPath)
        for ff in os.listdir(imgPath):
            # print(ff)
            # print(os.getcwd())
            if ff.endswith(".jpg"):
                prevName = imgPath + ff
                newName = imgPath + f + ".jpg"
                os.rename(prevName, newName)
                shutil.move(newName, destination)

    # Removes ".../downloads/" directory
    shutil.rmtree(source)
    print("Total number of items: " + str(i))

def moveBarcodesToFolder():
    # source = "/mnt/c/Users/derri/Desktop/Coding/visStudioTest/"
    # destination = "/mnt/c/Users/derri/Desktop/Coding/visStudioTest/Barcode"
    source = os.getcwd() + "/"
    destination = os.getcwd() + "/Barcode"

    print("Source: " + source)
    print("Destination: " + destination)

    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for f in os.listdir(source):
        if f.endswith(".png"):
            shutil.move(source+f, destination)


# main:
def downloadEverything():
    if downloadCovers() is True:
        print("Printing barcodes as there is a file")
        downloadBarcodes()

def downloadCovers():
    # downloads the barcodes
    # you probably should rewrite this
    #loc = ("/mnt/c/Users/derri/Desktop/Coding/work/excel/test.xls")
    loc = os.getcwd() + "/ExcelFolder/testExcel.xls"
    print(loc)

    if not os.path.exists(loc):
        print("1")
        return False
    else:
        wb = open_workbook(loc, "rb")
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0,0)

        newBooksList = []

        for i in range(sheet.nrows):
            if (sheet.cell_value(i,0) != "STOCK CODE"):
                newBooksList.append(sheet.cell_value(i,0))
                print(sheet.cell_value(i,0))
            else:
                #to skip the ISBN name label
                print("1")

        print(newBooksList)

        for book in newBooksList:
            if book == '':
                print ("2")
            else:
                downloadimages(book)
                print()

        moveImToFolder()
        return True

def downloadBarcodes():
    # To start the barcode
    import barcode
    ISBN = barcode.get_barcode_class('isbn13')
    excelFile = ("/mnt/c/Users/derri/Desktop/Coding/visStudioTest/testExcel.xls")
    wb = open_workbook(excelFile, "rb")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)

    for i in range(sheet.nrows):
        if (sheet.cell_value(i,0) != "STOCK CODE" and sheet.cell_value(i,0) != ""):
            # print(sheet.cell_value(i,0))
            # print(type(sheet.cell_value(i,0)))
            # print(type('9781456123789'))
            num = sheet.cell_value(i,0)
            barcode = ISBN(num, writer = ImageWriter())
            # filename = barcode.save("/mnt/c/Users/derri/Desktop/Coding/visStudioTest/Barcode"+sheet.cell_value(i,0))
            filename = barcode.save(sheet.cell_value(i,0))


        else:
            #just skip to the next one
            print("No isbn")

    moveBarcodesToFolder()


