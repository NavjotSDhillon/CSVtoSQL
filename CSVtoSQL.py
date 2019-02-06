import csv

fileName = input("Enter CSV file name: ")
databaseName = input("Enter database name: ")
outputFile = open("output.sql","w+")
noQuoteColumn = input("Enter the columns surrounded with no quotation separated by comma(,): ").split(",")

with open(fileName) as csvFile:
    dataCsv = csv.reader(csvFile, delimiter=',')
    for row in dataCsv:
        insertRow = "INSERT INTO " + str(databaseName) + " VALUES ("
        currentValNum = 0
        for value in row:
            ifNoQuotes = False
            for num in noQuoteColumn:
                if(int(num) == currentValNum+1):
                    ifNoQuotes = True
                    break

            if ifNoQuotes:
                if value == '':
                    insertRow += "0"
                else:
                    insertRow += value
            else:
                insertRow += "'" + value + "'"
            
            if currentValNum < len(row)-1: insertRow += ", "
            currentValNum += 1
        insertRow += ");"
        outputFile.write(insertRow + "\n")
outputFile.close()
print("SQL SCRIPT CREATED")
