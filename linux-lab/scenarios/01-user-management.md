# Scenario 1: User Management

## Objective
Create and manage a new user on the Linux server.

## Steps performed
- Connected to the server using SSH
- Created a new user using the `adduser` command
- Verified the user was created using `id`
- Checked that a home directory was created in `/home`
- Switched to the new user using `su`

## Commands used
- adduser testuser
- id testuser
- ls /home
- su - testuser

## Result
A new user was successfully created and verified on the system. The user accountand home directory were confirmed to be working.
