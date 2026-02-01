import sys
import os
import re
from datetime import datetime

README_FILE = 'README.md'

def update_leaderboard(score, user):
    if not os.path.exists(README_FILE):
        with open(README_FILE, 'w') as f:
            f.write("# Line Follower Challenge\n\n## Leaderboard\n| User | Time | Date |\n|---|---|---|\n")
    
    with open(README_FILE, 'r') as f:
        content = f.read()
        
    # Check if Leaderboard section exists
    if "## Leaderboard" not in content:
        content += "\n\n## Leaderboard\n| User | Time | Date |\n|---|---|---|\n"
        
    # Parse existing leaderboard
    # Find list of entries
    # We want to keep unique users, only their best score? Or all scores?
    # Let's keep best score per user for simplicity and cleanliness.
    
    # Simple regex to find the table rows
    # Assuming standard markdown table format
    # | User | Time | Date |
    
    lines = content.splitlines()
    leaderboard_start = -1
    leaderboard_end = -1
    
    for i, line in enumerate(lines):
        if "## Leaderboard" in line:
            leaderboard_start = i
            # Skip header and separator
            break
            
    if leaderboard_start == -1:
        # Should not happen given logic above, but safety
        return

    # Extract entries
    entries = []
    # format: {'user': str, 'time': float, 'date': str}
    
    # Rows start after header (start + 2 usually)
    table_start = leaderboard_start + 3
    
    # Read existing
    # We might have content after table, so stop at next header or empty lines if strict
    # For now assume table is at end or continuous
    
    for i in range(table_start, len(lines)):
        line = lines[i].strip()
        if not line.startswith('|'): 
            continue
        parts = [p.strip() for p in line.split('|') if p.strip()]
        if len(parts) >= 3:
            u, t, d = parts[0], parts[1], parts[2]
            try:
                t_val = float(t.replace('s', ''))
                entries.append({'user': u, 'time': t_val, 'date': d, 'original_line': line})
            except ValueError:
                pass
                
    # Update or Add
    current_time = float(score)
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    updated = False
    for entry in entries:
        if entry['user'] == user:
            if current_time < entry['time']:
                entry['time'] = current_time
                entry['date'] = date_str
                updated = True
            else:
                # New score is worse, do nothing? Or maybe user wants to see attempt?
                # Challenge usually demands Personal Best.
                print(f"New score {current_time} is not better than best {entry['time']}. No update.")
                return
            break
            
    if not updated and not any(e['user'] == user for e in entries):
        entries.append({'user': user, 'time': current_time, 'date': date_str})
        updated = True

    if not updated:
        return

    # Sort entries by time (asc)
    entries.sort(key=lambda x: x['time'])
    
    # Reconstruct Table
    new_table_lines = []
    for e in entries:
        new_table_lines.append(f"| {e['user']} | {e['time']:.4f}s | {e['date']} |")
        
    # Reconstruct File Content
    # We replace from table_start to the end of the table
    # Finding end of table is tricky if there is content after.
    # We will just replace all consecutive table lines starting from table_start
    
    # But wait, lines list is static.
    # Let's find where the table technically ends (next empty line or non-table line)
    table_end = table_start
    while table_end < len(lines) and lines[table_end].strip().startswith('|'):
        table_end += 1
        
    # Rebuild
    final_lines = lines[:table_start] + new_table_lines + lines[table_end:]
    
    with open(README_FILE, 'w') as f:
        f.write("\n".join(final_lines))
        
    print(f"Leaderboard updated for {user} with time {current_time}s")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python update_leaderboard.py <score> <user>")
        sys.exit(1)
    
    try:
        score = float(sys.argv[1])
        user = sys.argv[2]
        update_leaderboard(score, user)
    except ValueError:
        print("Invalid score format")
        sys.exit(1)
