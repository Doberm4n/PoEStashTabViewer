# -*- coding: utf-8 -*-
import os
import csv
from PyQt4 import QtGui

#csv comma delimited with headers, UTF-8
def exportToCsv(form):
    fileName = getCsvFileName()
    if fileName:
            with open(unicode(fileName), 'wb') as stream:
                csvWriter = csv.writer(stream)
                rowdata = []
                #column headers
                for columns in range(form.tableWidget.columnCount()):
                    columnHeaderText = unicode(form.tableWidget.horizontalHeaderItem(columns).text())
                    rowdata.append(columnHeaderText.encode('utf-8'))
                csvWriter.writerow(rowdata)

                #rows
                for rows in range(form.tableWidget.rowCount()):
                    rowdata = []
                    for columns in range(form.tableWidget.columnCount()):
                        item = form.tableWidget.item(rows, columns)
                        if item:
                            rowdata.append(unicode(item.text()).encode('utf-8'))
                        else:
                            rowdata.append('')
                    csvWriter.writerow(rowdata)

def getCsvFileName():
    newName = QtGui.QFileDialog.getSaveFileName(None, 'Export to .csv', directory=os.getcwd(), filter='*.csv')
    return newName
