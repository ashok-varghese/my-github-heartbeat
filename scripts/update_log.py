import datetime
import os

def update_heartbeat():
    # Get current time in UTC
    now = datetime.datetime.utcnow()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Write to heartbeat.txt (Overwrites the file to keep it small)
    with open("heartbeat.txt", "w") as f:
        f.write(f"Last GitHub Heartbeat: {timestamp}\n")
        f.write("Status: Active\n")
    
    print(f"Successfully updated heartbeat at {timestamp}")

if __name__ == "__main__":
    update_heartbeat()
