#!/usr/bin/env python
# coding: utf-8

# Created by Noskov Alexey
# version
# 22.09.2019 - 1.0.0 - Релиз
# 22.09.2019 - 1.0.1 - Кодировка исправлена на UTF-8
# 22.09.2019 - 1.1.0 - Добавлена опция NOTEBOOK_ONLY

import json
import io

def make(inputFileName):

    with io.open(inputFileName, mode = "r", encoding = 'utf_8') as inputFile:
        data = json.load(inputFile)

    outputFile = io.open(inputFileName.replace('.ipynb', '.py'), mode = "w", encoding = 'utf_8')

    outputFile.write('#!/usr/bin/env python\n')
    outputFile.write('# coding: utf-8\n')
    outputFile.write('\n')

    for i, val in enumerate(data['cells']):
        if val['cell_type'] == 'code' :
            
            isScriptOnly = False
            isNotebookOnly = False
            
            for k, row in enumerate(val['source']):
                
                if row[:12] == "#SCRIPT_ONLY" or row[:13] == "# SCRIPT_ONLY" :
                    isScriptOnly = True
                    continue
                    
                if row[:14] == "#NOTEBOOK_ONLY" or row[:15] == "# NOTEBOOK_ONLY" :
                    break
                
                if ("SCRIPT_ONLY" in row) or isScriptOnly == True:
                    row = row[1:]
                    
                if ("NOTEBOOK_ONLY" in row):
                    continue

                #print(row)
                if not '\n' == row[-2:] :
                    row = row + '\n'
                outputFile.write(row)

    outputFile.close()



