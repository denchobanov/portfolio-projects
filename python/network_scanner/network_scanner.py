import socket, subprocess, time, os, json, sys
from datetime import datetime

# Generate timestamp for reports
timestamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Load scanner configuration
try:
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print('config.json not found!')
    exit()
except json.JSONDecodeError:
    print('Invalid JSON format in config.json!')
    exit() 

# Check if target host is reachable
def ping_host(ip):
    checkOnline = subprocess.run(['ping', '-c', str(config['ping_count']), ip],capture_output=True)
    if checkOnline.returncode != 0:
       return False
    return True

# Scan configured ports and store their status
def scan_ports(ip, ports):
    scan_results = {}

    # Attempt to connect to the current port
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(config['timeout'])
        connection_status = sock.connect_ex((ip,port))
        if connection_status == 0:
            scan_results[port] = 'OPEN'
        else: 
            scan_results[port] = 'CLOSED'
        sock.close()
    return scan_results

# Count open and closed ports
def count_ports(results):
    closed_ports = 0
    open_ports = 0
    
    for status in results.values():
        if status == "OPEN":
            open_ports+=1
        else: 
            closed_ports+=1
    
    return open_ports, closed_ports

# Display scan results in the terminal
def print_results(results, duration):
    open_ports, closed_ports = count_ports(results)

    print('\n===== RESULTS =====\n')
    for port, status in results.items():
        print(f'PORT {port}: {status}')
    print('\n===== SUMMARY =====\n')
    print(f'Open ports: {open_ports}')
    print(f'Closed ports: {closed_ports}')
    print(f'Scan Duration: {duration:.2f} seconds\n')
    

# Save scanned results to a timestamped report
def save_report(ip, results, duration):

    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    report_path = os.path.join('reports',f'network_scan_{timestamp}.txt')
    
    open_ports, closed_ports = count_ports(results)
    
    # Write scan results to the report
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

# Validate arguments 
if len (sys.argv) != 2:
    print('Usage: python3 network_scanner.py <ip>')
    exit()

ip = sys.argv[1]

# Measure scan duration
start_time = time.time()
if not ping_host(ip):
    print('Host unreachable!')
    exit()

# Load ports from the configuration file
ports = config['ports']
scan_results = scan_ports(ip, ports)
end_time = time.time()
duration = end_time - start_time
print_results(scan_results, duration)
save_report(ip, scan_results, duration)
