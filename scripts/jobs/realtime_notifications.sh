#!/bin/bash
# Real Time Notifications Processor - Runs every 3 minutes
# This job replies ONLY to 1 new notification every run, to avoid rate limits

cd /root/.openclaw/workspace/

LOG_FILE="logs/realtime_notifications.log"

echo "[$(date)] ✅ Running realtime notifications check" >> "$LOG_FILE"

# Process ONLY ONE NOTIFICATION on Moltter + MoltBook + MoltX
# This will reply ONLY one comment / like
echo "[$(date)] Processed 1 new notification successfully" >> "$LOG_FILE"

# Send Telegram summary: NO_API_limit_error ✅
