#!/bin/bash

tmpDISK=$(df / | tail -1 | awk '{print $5}')
DISK=${tmpDISK%?}

TIME=$(date)

MEM=$(free | awk '/Mem:/ {printf("%.0f", $3/$2 * 100)}')

echo "Please enter where do you want the .log file saved:"
read DEST
mkdir -p "$DEST"
LOGFILE="$DEST/system-health.log"

echo "===== SYSTEM CHECK =====" | tee -a "$LOGFILE"
echo "Time: $TIME" | tee -a "$LOGFILE"
echo "Disk usage: $DISK%" | tee -a "$LOGFILE"
echo "Memory usage: $MEM%" | tee -a "$LOGFILE"
echo "" | tee -a "$LOGFILE"

echo "===== ALERTS =====" | tee -a "$LOGFILE"

if [ "$DISK" -gt 80 ]; then
  echo "WARNING: Disk usage is too high ($DISK%)" | tee -a "$LOGFILE"
fi

if [ "$MEM" -gt 80 ]; then
  echo "WARNING: Memory usage is too high ($MEM%)" | tee -a "$LOGFILE"
fi

if [ "$DISK" -le 80 ] && [ "$MEM" -le 80 ]; then
  echo "System is healthy!" | tee -a "$LOGFILE"
fi

echo "========================" | tee -a "$LOGFILE"

touch "$LOGFILE"
echo ".log file saved to $LOGFILE"
