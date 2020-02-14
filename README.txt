Before typing, you must make sure the environment is set up correctly:
- Pillow is installed along with barcode to make sure the barcode are made correctly
- Xlrd so the script can read excel documents
- whatever it is to export to csv files that you need
- Excel ISBN numbers are enterred in correctly (ensuring you type ' before 
  so that it doesn't store the numbers as a decimal or in scientific notation)

It will be too hard to get every obscure book. For now the best way to handle those:
- Make an output .txt file that specifies which books that could not be seen, followed
  by the title just for more ease of use
- If there are no hard books, then the file should be empty
 
