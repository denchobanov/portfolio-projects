import socket, subprocess

def ping_host(ip):
    checkOnline = subprocess.run(['ping', '-c', '4', ip])
    if checkOnline.returncode != 0:
       return False
    return True

def scan_ports(ip, ports):
    scan_results = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        connection_status = sock.connect_ex((ip,port))
        if connection_status == 0:
            scan_results[port] = 'OPEN'
        else: 
            scan_results[port] = 'CLOSED'
        sock.close()
    return scan_results

def print_results(results):
    print("\n===== SCAN RESULTS =====\n")
    for port, status in results.items():
        print(f'PORT {port}: {status}')

ip = input('Enter an ip: ')
if not ping_host(ip):
    print('Host unreachable!')
    exit()
ports = [22, 80, 443, 3389]
scan_results = scan_ports(ip, ports)
print_results(scan_results)
