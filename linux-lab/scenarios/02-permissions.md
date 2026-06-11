# Scenario 2: File Permissions

## Objective
Understand and modify Linux file permissions to control user access to files.

## Steps performed
- Created a test file on the server
- Checked default file permissions using `ls -l`
- Attempted access as a different user
- Modified permissions using `chmod`
- Verified access was restored

## Commands used
- touch testfile.txt
- ls -l
- chmod 644 testfile.txt
- chmod 600 testfile.txt
- su - testuser
- cat testfile.txt

## Result
File access was tested under different permission settings. Permissions were adjusted to control and restore user access successfully.
