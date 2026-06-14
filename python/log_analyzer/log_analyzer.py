import os
from datetime import datetime
timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
path = input("Enter log file path: ")
reportPath = os.path.join(os.path.dirname(path),'analysis_report.txt')
errCnt = 0
wrnCnt = 0
infoCnt = 0

try:
    with open(path,'r') as logFile:
        for line in logFile:
            if 'error' in line.lower():
                errCnt+=1
            elif 'warning' in line.lower():
                wrnCnt+=1
            elif 'info' in line.lower():
                infoCnt+=1
    with open(reportPath,'a') as reportFile:
        reportFile.write(f'===== LOG ANALYSIS REPORT ({timestamp}) =====\n\n\n')
        reportFile.write(f'Errors: {errCnt}\n\n')
        reportFile.write(f'Warnings: {wrnCnt}\n\n')
        reportFile.write(f'Info: {infoCnt}\n\n')
        
except FileNotFoundError:
    print('Invalid path! Make sure you write the correct path!')