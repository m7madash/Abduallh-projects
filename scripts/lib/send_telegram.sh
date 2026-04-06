#!/bin/bash
MESSAGE="$1"
curl -s -X POST "https://api.telegram.org/bot8613963132:AAG-ED2xwz7oJakQKhTem_jIoS9zFyUkmfY/sendMessage" \
  -H "Content-Type: application/json" \
  -d "{\"chat_id\":6275105434,\"text\":\"$MESSAGE\"" > /dev/null 2>&1
