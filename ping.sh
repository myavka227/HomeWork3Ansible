#!/bin/bash
while true; do curl -o /dev/null -s -w "$(date +%s) code:%{http_code} time:%{time_total}\n" https://example.com; sleep 1; done
