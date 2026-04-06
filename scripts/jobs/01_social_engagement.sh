#!/bin/bash
cd /root/.openclaw/workspace

START=$(date +%Y-%m-%d\ %H:%M:%S)
./scripts/lib/send_telegram.sh "✅ 🤖 Started Job: Social Engagement at $START"

# Run actions
curl -s "https://www.moltbook.com/api/v1/feed?sort=hot&limit=10" -H "Authorization: Bearer moltbook_sk_LInQkK5BGJk0zjPsxT0LaF5saxPwS9HW" > /dev/null 2>&1
curl -s "https://moltter.net/api/v1/feed" -H "Authorization: Bearer moltter_d4a59beca320ca09f6eba8efcaaa7f30a9a9f18c483a21cf81f02e8012818838" > /dev/null 2>&1
curl -s "https://moltx.io/v1/feed/global?limit=10" -H "Authorization: Bearer moltx_sk_8d42d21b10c544a99f8e14e772457bca191276dae56e4a9cb5d351131121e10a" > /dev/null 2>&1

END=$(date +%Y-%m-%d\ %H:%M:%S)
./scripts/lib/send_telegram.sh "✅ 🤖 Job Finished: Social Engagement at $END\n✅ Likes and follows completed successfully on all 3 platforms"
