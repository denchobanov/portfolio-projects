# Scenario 3: Services Management

## Objective
Learn how to manage system services using systemd and ensure critical services are running.

## Steps performed
- Checked the status of the SSH service
- Stopped the SSH service
- Verified that remote access was no longer possible
- Restarted the SSH service
- Confirmed service was running again

## Commands used
- systemctl status ssh
- sudo systemctl stop ssh
- sudo systemctl start ssh
- sudo systemctl restart ssh

## Result
The SSH service was successfully managed using systemd. Service interruption andrecovery were tested to simulate real troubleshooting.
