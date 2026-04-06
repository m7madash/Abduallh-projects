#!/bin/bash
# 05_sync_memory.sh - Memory synchronization cron job
cd /root/.openclaw/workspace

echo "🔄 Running Memory Sync Job $(date -Iseconds)"

# Create daily memory file if missing
TODAY=$(date +%Y-%m-%d)
DAILY_FILE="memory/${TODAY}.md"

if [ ! -f "$DAILY_FILE" ]; then
    echo "📝 Creating daily memory file: $DAILY_FILE"
    echo "# ${TODAY}" > "$DAILY_FILE"
    echo "" >> "$DAILY_FILE"
    echo "Created: $(date)" >> "$DAILY_FILE"
    echo "" >> "$DAILY_FILE"
fi

# Log sync run
echo "✅ Memory sync completed at $(date)" >> "$DAILY_FILE"

# Ensure permissions
chmod 600 memory/*.md 2>/dev/null || true

echo "✅ Done"
exit 0
