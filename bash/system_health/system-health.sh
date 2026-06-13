#!/bin/bash

# --- 1. CONFIGURATION & VARIABLES ---

# Define alert threshold percentage (Default: 80%)
THRESHOLD=80
TIME=$(date +"%Y-%m-%d_%H-%M-%S"

# Set destination path from the first argument.
# Defaults to './logs' if no argument is provided.
DEST={$1:-./logs}


# --- 2. METRICS COLLECTION ---

# Get Disk usage for the root (/) partition.
# Strip the '%' sign so Bash can perform integer comparisons later.
DISK=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

# Get CPU and Memory usage, extract specific fields from top/free
CPU=$(top -bn1 | awk '/^%Cpu/ {printf("%.0f", 100 - $8)}')
MEM=$(free | awk '/Mem:/ {printf("%.0f", $3/$2 * 100)}')


# --- 3. PRE-FLIGHT CHECKS ---

# Ensure the destination directory exists before we try to write logs.
# If creation fails (e.g., missing permissions), script exits with an error.
mkdir -p "$DEST" || { echo "Error! Cannot create directory or missing permissions!"; exit 1; }
LOGFILE="$DEST/system-health.log"
BACKUP="$DEST/backup_$TIME.log"


# --- 4. LOGGING & ALERTS ---

# Evaluate the collected metrics against the defined thresholds.
# Generates a health report with warnings for any high resource usage.
# Records the final output to both the console and the log file.
{
echo "===== SYSTEM CHECK ====="
echo "Time: $TIME"
echo "CPU usage: $CPU%"
echo "Disk usage: $DISK%"
echo "Memory usage: $MEM%"
echo ""
echo "===== ALERTS ====="

if [ "$CPU" -gt "$THRESHOLD" ]; then
  echo "WARNING: CPU usage is too high ($CPU%)"
fi

if [ "$DISK" -gt "$THRESHOLD" ]; then
  echo "WARNING: Disk usage is too high ($DISK%)"
fi

if [ "$MEM" -gt "$THRESHOLD" ]; then
  echo "WARNING: Memory usage is too high ($MEM%)"
fi

if [ "$DISK" -le "$THRESHOLD" ] && [ "$MEM" -le "$THRESHOLD" ] && [ "$CPU" -le "$THRESHOLD" ]; then
  echo "System is healthy!"
fi

echo "========================"
} | tee "$LOGFILE"
echo "Check complet! Log saved to: $LOGFILE"


# --- 5. AUTOMATED BACKUP ---

# Create an automated backup of the current state without requiring user input.
cp "$LOGFILE" "$BACKUP"
echo "Automatic backup created: $BACKUP"
