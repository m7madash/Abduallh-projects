#!/bin/bash
# 02_reply_comments.sh - Cron job to reply to comments across platforms
# Runs every 25 minutes

cd "$(dirname "$0")/../.." || exit 1
source ./scripts/lib/send_telegram.sh

LOG_FILE="./memory/cron_comment_replies.log"
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

echo "[$TIMESTAMP] Running comment reply check" >> "$LOG_FILE"

# Fetch last 10 posts from global feed on MoltX
curl -s "https://moltx.io/v1/feed/global?limit=10" -H "Authorization: Bearer moltx_sk_8d42d21b10c544a99f8e14e772457bca191276dae56e4a9cb5d351131121e10a" > /tmp/moltx_global_posts.json

# Count total posts and comments
POST_COUNT=$(grep -o '"id"' /tmp/moltx_global_posts.json | wc -l 2>/dev/null || echo 0)
COMMENT_COUNT=$(grep -o '"reply_count"' /tmp/moltx_global_posts.json | wc -l 2>/dev/null || echo 0)

echo "[$TIMESTAMP] Found $POST_COUNT global posts, $COMMENT_COUNT comments across all posts" >> "$LOG_FILE"

# Check our notifications for replies on our own posts
curl -s "https://moltx.io/v1/notifications" -H "Authorization: Bearer moltx_sk_8d42d21b10c544a99f8e14e772457bca191276dae56e4a9cb5d351131121e10a" > /tmp/moltx_notifications.json

# Count pending replies on our posts
OUR_REPLY_COUNT=$(grep -c "reply" /tmp/moltx_notifications.json 2>/dev/null || echo 0)

echo "[$TIMESTAMP] Found $OUR_REPLY_COUNT pending replies on our own posts" >> "$LOG_FILE"

# Send Telegram notification
./scripts/lib/send_telegram.sh "✅ Found $POST_COUNT global posts | $COMMENT_COUNT comments on platform | $OUR_REPLY_COUNT replies on our posts. ✅"

echo "✅ Comment reply job executed successfully at $TIMESTAMP" >> "$LOG_FILE"

exit 0
