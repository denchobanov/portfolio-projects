# Scenario 5: IT Ticket Simulation

## Objective
Simulate real-world IT support scenarios by combining Linux user management, permissions, services, and networking.

---

## Ticket 1: User cannot access file

### Issue
A user reports they cannot read a file on the server.

### Investigation
- Checked file permissions using `ls -l`
- Verified user identity using `id`

### Fix
- Adjusted file permissions using `chmod`

### Result
User regained access to the file successfully.

---

## Ticket 2: Server not reachable

### Issue
Server is unreachable over SSH.

### Investigation
- Checked network connectivity using `ping`
- Verified IP address using `ip a`
- Checked SSH service status using `systemctl`

### Fix
- Restarted SSH service if required

### Result
SSH connectivity was restored.

---

## Ticket 3: Service not responding

### Issue
SSH service is not responding.

### Investigation
- Checked service status using `systemctl status ssh`
- Verified socket status if applicable

### Fix
- Restarted SSH service and socket

### Result
Service was restored and remote access worked again.
