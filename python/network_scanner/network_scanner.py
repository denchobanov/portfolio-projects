import socket, subprocess, time, os
from datetime import datetime

timestamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

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

def count_ports(results):
    closed_ports = 0
    open_ports = 0
    
    for status in results.values():
        if status == "OPEN":
            open_ports+=1
        else: 
            closed_ports+=1
    
    return open_ports, closed_ports

def print_results(results, duration):
    open_ports, closed_ports = count_ports(results)

    print('\n===== RESULTS =====\n')
    for port, status in results.items():
        print(f'PORT {port}: {status}')
    print('\n===== SUMMARY =====\n')
    print(f'Open ports: {open_ports}')
    print(f'Closed ports: {closed_ports}')
    print(f'\n Scan Duration: {duration:.2f} seconds')
    

def save_report(ip, results, duration):
    os.makedirs('reports', exist_ok=True)
    report_path = os.path.join('reports',f'network_scan_{timestamp}.txt')
    
    open_ports, closed_ports = count_ports(results)

    with open(report_path,'w') as report:
        report.write('===== NETWORK SCAN REPORT =====\n\n')
        report.write(f'Generated: {timestamp}\n')
        report.write(f'Target host: {ip}\n')
        report.write('\n===== RESULTS =====\n\n')
        for port, status in results.items():
            report.write(f'PORT {port}: {status}\n')
        report.write('\n\n===== SUMMARY =====\n\n')
        report.write(f'Open ports: {open_ports}\n')
        report.write(f'Closed ports: {closed_ports}\n\n')
        report.write(f'Scan Duration: {duration:.2f} seconds\n')
    
    print(f'Report saved to: {os.path.dirname(report_path)}/')

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
save_report(ip, scan_results, duration)
