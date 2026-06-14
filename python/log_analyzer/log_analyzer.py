import os
from datetime import datetime
# Setup
timestamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

path = input("Enter log file path: ")
reportPath = os.path.join('reports',f'analysis_report_{timestamp}.txt')

# Counters
errCnt = 0
wrnCnt = 0
infoCnt = 0
totalEntries = 0
failedLoginCnt = 0

# Store recurring errors and failed logins
errDict = {}
failedLoginDict = {}

# Determine the most common error
maxValue = 0
topError = 'None'

# Log analysis
try:
    with open(path,'r') as logFile:
        for line in logFile:

            # Count and categorize errors
            if 'error' in line.lower():

                # Extract error message after 'ERROR'
                parts=line.split(':',1)
                errMessage=parts[1].strip()

                # Track recurring errors
                if errMessage not in errDict:
                    errDict[errMessage] = 1
                else:
                    errDict[errMessage]+=1
                errCnt+=1

            # Count warning entries
            if 'warning' in line.lower():
                wrnCnt+=1
            
            # Count informational entries
            if 'info' in line.lower():
                infoCnt+=1

            # Count failed login attempts
            if 'failed login' in line.lower():

                # Extract username after 'FAILED LOGIN'
                parts=line.split(':',1)
                loginUsername=parts[1].strip()

                # Track recurring failed login attempts
                if loginUsername not in failedLoginDict:
                    failedLoginDict[loginUsername] = 1
                else:
                    failedLoginDict[loginUsername] += 1
                failedLoginCnt+=1
                
            totalEntries+=1

        # Check if the log file is empty
        if totalEntries == 0:
            print('Log file is empty!')

    # Report generation
    with open(reportPath,'w') as reportFile:
        reportFile.write(f'===== LOG ANALYSIS REPORT =====\n\n\n')
        reportFile.write(f'Generated: {timestamp}\n')
        reportFile.write(f'Analyzed File: {os.path.basename(path)}\n\n')
        reportFile.write(f'Errors: {errCnt}\n\n')
        reportFile.write(f'Warnings: {wrnCnt}\n\n')
        reportFile.write(f'Info: {infoCnt}\n\n')
        reportFile.write(f'Total entries: {totalEntries}\n\n')
        reportFile.write(f'===== MOST COMMON ERRORS =====\n\n\n')
       
        for key,value in errDict.items():
            reportFile.write(f'{key}: {value}\n\n')
            
            # Find the most frequently occurring error
            if value>maxValue:
                maxValue=value
                topError=key
        
        # Check if theres any errors in the logs
        if errCnt > 0:
           reportFile.write(f'\nTop Issue: {topError} (Occurrences: {maxValue})\n\n')
        else:
            reportFile.write('\nTop Issue: No errors detected\n\n')
        
        reportFile.write('===== SECURITY SUMMARY =====\n\n\n')
        reportFile.write(f'Failed login attempts: {failedLoginCnt}\n\n')
        reportFile.write('Affected accounts:\n\n')
        for key,value in failedLoginDict.items():
            reportFile.write(f'{key}: {value}\n\n')
        reportFile.write('===== SUMMARY =====\n\n')
        reportFile.write(f'Errors: {errCnt}\n')
        reportFile.write(f'Warnings: {wrnCnt}\n')
        reportFile.write(f'Info: {infoCnt}\n')
        reportFile.write(f'Failed Logins: {failedLoginCnt}\n')
        
    print(f'Report saved to {reportPath}')

# Handle invalid file paths
except FileNotFoundError:
    print('Invalid path! Make sure you write the correct path!')