#!/bin/bash

# Modify this
PROJECT_DIR="/Users/owen/Desktop/FreeGame-Scraper"
VENV_PATH="$PROJECT_DIR/myvenv/bin/activate"
PY_SCRIPT="$PROJECT_DIR/fetch_v3.py"

# macOS：使用 AppleScript 開 Terminal
if [[ "$OSTYPE" == "darwin"* ]]; then
    osascript <<EOF
tell application "Terminal"
    activate
    do script "source \"$VENV_PATH\"; python \"$PY_SCRIPT\"; deactivate; exit"
end tell
EOF

# Linux：GNOME 預設 terminal
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    gnome-terminal -- bash -c "cd \"$PROJECT_DIR\"; source \"$VENV_PATH\"; python \"$PY_SCRIPT\"; exec bash"

# 可擴充其他環境
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi
