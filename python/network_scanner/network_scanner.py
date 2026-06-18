import socket, subprocess,time

def ping_host(ip):
    checkOnline = subprocess.run(['ping', '-c', '4', ip],capture_output=True)
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

def print_results(results, duration):
    closed_Ports = 0
    open_Ports = 0
    for status in results.values():
        if status == "OPEN":
            open_Ports+=1
        else: 
            closed_Ports+=1
    print("\n===== SCAN RESULTS =====\n")
    for port, status in results.items():
        print(f'PORT {port}: {status}')
    print('\n===== SUMMARY =====\n')
    print(f'Open ports: {open_Ports}')
    print(f'Closed ports: {closed_Ports}')
    print(f'\n Scan Duration: {duration:.2f} seconds')

ip = input('Enter an ip: ')
start_time = time.time()
if not ping_host(ip):
    print('Host unreachable!')
    exit()
ports = [22, 80, 443, 3389]
scan_results = scan_ports(ip, ports)
end_time = time.time()
duration = end_time - start_time
print_results(scan_results, duration)
