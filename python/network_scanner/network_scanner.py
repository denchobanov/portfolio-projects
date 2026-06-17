import socket, subprocess

ip = input("Enter IP Address: ")
checkOnline = subprocess.run(['ping', '-c', '4', ip])
if checkOnline.returncode != 0:
    print("The host is unreachable!")
    exit()

ports = [22, 80, 443, 3389]

for port in ports:
    scket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scket.settimeout(1)
    result = scket.connect_ex((ip,port))
    if result == 0:
        print(f'PORT {port}: OPEN')
    else: 
        print(f'PORT {port}: CLOSED')
    scket.close()