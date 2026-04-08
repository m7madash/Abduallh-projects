#!/bin/bash
# Memory Sync Cron Job
# Runs daily to sync and consolidate agent memory

cd /root/.openclaw/workspace

echo "✅ Memory sync running at $(date -u)"

# Check memory folder exists
mkdir -p memory

# Sync git state for memory files
if [ -d .git ]; then
  git add memory/ MEMORY.md
  git diff --quiet HEAD memory/ MEMORY.md
  if [ $? -ne 0 ]; then
    git commit -m "auto: sync memory state $(date -u +%Y-%m-%d)"
    echo "✅ Committed updated memory files"
  else
    echo "ℹ️ No memory changes to commit"
  fi
fi

echo "✅ Memory sync completed successfully"
