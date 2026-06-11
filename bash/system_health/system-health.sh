#!/bin/bash

tmpDISK=$(df / | tail -1 | awk '{print $5}')
DISK=${tmpDISK%?}

CPU=$(top -bn1 | awk '/^%Cpu/ {printf("%.0f", 100 - $8)}')

TIME=$(date)

MEM=$(free | awk '/Mem:/ {printf("%.0f", $3/$2 * 100)}')

echo "Please enter where do you want the .log file saved:"
read DEST
mkdir -p "$DEST"
if [ ! -d "$DEST" ]
then
    echo "Error! Thats not a directory!"
    exit 1
fi
LOGFILE="$DEST/system-health.log"
BACKUP="$DEST/backup_$TIME.log"
echo "===== SYSTEM CHECK =====" | tee -a "$LOGFILE"
echo "Time: $TIME" | tee -a "$LOGFILE"
echo "CPU usage: $CPU%" | tee -a "$LOGFILE"
echo "Disk usage: $DISK%" | tee -a "$LOGFILE"
echo "Memory usage: $MEM%" | tee -a "$LOGFILE"
echo "" | tee -a "$LOGFILE"

echo "===== ALERTS =====" | tee -a "$LOGFILE"
if [ "$CPU" -gt 80 ]; then
  echo "WARNING: CPU usage is too high ($CPU%)" | tee -a "$LOGFILE"
fi

if [ "$DISK" -gt 80 ]; then
  echo "WARNING: Disk usage is too high ($DISK%)" | tee -a "$LOGFILE"
fi

if [ "$MEM" -gt 80 ]; then
  echo "WARNING: Memory usage is too high ($MEM%)" | tee -a "$LOGFILE"
fi

if [ "$DISK" -le 80 ] && [ "$MEM" -le 80 ] && [ "$CPU" -le 80 ]; then
  echo "System is healthy!" | tee -a "$LOGFILE"
fi

echo "========================" | tee -a "$LOGFILE"

touch "$LOGFILE"
echo ".log file saved to $LOGFILE"
read -p "Would you like to save a backup? y/n: " ANSWER
if [[ "$ANSWER" != "y"  && "$ANSWER" != "n" ]]
then 
    echo "Wrong input! Backup not saved!"
    exit 1
else
    cp "$LOGFILE" "$BACKUP"
    echo "Backup created successfully!"
fi
