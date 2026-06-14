import os
from datetime import datetime
timestamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
path = input("Enter log file path: ")
reportPath = os.path.join(os.path.dirname(path),f'analysis_report_{timestamp}.txt')
errCnt = 0
wrnCnt = 0
infoCnt = 0
totalEntries =0

try:
    with open(path,'r') as logFile:
        for line in logFile:
            if 'error' in line.lower():
                errCnt+=1
            if 'warning' in line.lower():
                wrnCnt+=1
            if 'info' in line.lower():
                infoCnt+=1
            totalEntries+=1
    with open(reportPath,'w') as reportFile:
        reportFile.write(f'===== LOG ANALYSIS REPORT =====\n\n\n')
        reportFile.write(f'Errors: {errCnt}\n\n')
        reportFile.write(f'Warnings: {wrnCnt}\n\n')
        reportFile.write(f'Info: {infoCnt}\n\n')
        reportFile.write(f'Total entries: {totalEntries}\n\n')
    print(f'Report saved to {reportPath}')
except FileNotFoundError:
    print('Invalid path! Make sure you write the correct path!')