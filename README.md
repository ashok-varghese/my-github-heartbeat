# 💓 GitHub Profile Heartbeat

This project is an automated utility designed to maintain an active contribution graph and monitor GitHub Actions uptime.

## 🛠️ How It Works
- **GitHub Actions**: Triggers every hour via a `cron` schedule.
- **Python Logic**: A script in `/scripts` generates a fresh timestamp.
- **Automation**: The `github-actions[bot]` commits the change to `heartbeat.txt`.

## 📂 Structure
- `.github/workflows/`: Contains the YAML automation logic.
- `scripts/`: Python source for updating logs.
- `heartbeat.txt`: The target file for automated commits.
