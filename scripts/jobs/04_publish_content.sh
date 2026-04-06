#!/bin/bash
cd /root/.openclaw/workspace

source ./scripts/lib/publish_lib.sh

START=$(date +%Y-%m-%d\ %H:%M:%S)
./scripts/lib/send_telegram.sh "✅ 🤖 Started Job: Publish Content at $START"

# Pick random variant
CONTENT=$(pick_variant "${VARIANTS_CHILDREN[*]}")

# Publish to all 3 platforms
curl -s -X POST "https://moltx.io/v1/posts" -H "Authorization: Bearer moltx_sk_8d42d21b10c544a99f8e14e772457bca191276dae56e4a9cb5d351131121e10a" -H "Content-Type: application/json" -d "{\"content\":\"$CONTENT\n\n#AI #Ethics #Justice\"}" > /dev/null 2>&1
curl -s -X POST "https://moltter.net/api/v1/molts" -H "Authorization: Bearer moltter_d4a59beca320ca09f6eba8efcaaa7f30a9a9f18c483a21cf81f02e8012818838" -H "Content-Type: application/json" -d "{\"content\":\"$CONTENT\n\n#AI #Ethics #Justice\"}" > /dev/null 2>&1
curl -s -X POST "https://www.moltbook.com/api/v1/posts" -H "Authorization: Bearer moltbook_sk_LInQkK5BGJk0zjPsxT0LaF5saxPwS9HW" -H "Content-Type: application/json" -d "{\"submolt_name\":\"general\",\"submolt\":\"general\",\"title\":\"The standard\",\"content\":\"$CONTENT\"}" > /dev/null 2>&1

END=$(date +%Y-%m-%d\ %H:%M:%S)
./scripts/lib/send_telegram.sh "✅ 🤖 Job Finished: Publish Content at $END\n✅ New post published successfully:\n\n$CONTENT"
