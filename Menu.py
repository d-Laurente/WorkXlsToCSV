#Author: Derrick Laurente
'''
Alpha Build 0.1
This is a program that acts as an interface for the different parts of the import process
'''

import os
import shutil
from ImagesDownloader import *

def actionSelect(cmd):
    if cmd == '0':
        print("Cleaning the work environment")       
        cleanWorkEnvironment()
    elif cmd == '1':
        print("Downloading images and barcodes")
        downloadEverything()
    elif cmd == '2':
        print("Generate a file for Cubecart")
    elif cmd == '3':
        downloadBarcodes()
    else:
        print("Invalid option. Please select a proper option")

def printLines():
    for i in range(5):
        print()

def clearScreen():
    os.system("clear") # for linux but for windows try os.system("cls")

def cleanWorkEnvironment():
    # path = os.getcwd()
    # print("Clearing the " + path)
    # shutil.rmtree(path + "/Covers")
    # shutil.rmtree(path + "/Barcode")
    # print("Environment is now clean")
    path = os.getcwd()
    try:
        shutil.rmtree(path + "/Covers")
        shutil.rmtree(path + "/Barcode")
    except:
        print("There are no folders to clean")
    else:
        print("Environment is clean")

# main program starting here
clearScreen()
print("Alpha build 0.1")
print("This is a program to import books to Cubecart")
print("Any assistance needed, call Derrick")
printLines()


while True:
    print("To prepare the work environment '0'")
    print("To download covers and barcodes images press '1'")
    print("To export to Cubecart press '2'")
    print("To test barcode press 3 TEST PURPOSES ONLY")
    print("To quit the program type \"quit\"")
    value = input("Please enter a command: ")
    if value == "quit":
        break
    else:
        actionSelect(value)
        printLines()
