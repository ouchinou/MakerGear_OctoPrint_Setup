#!/usr/bin/env python
"""Convert tabs to spaces in Python files."""
import sys
from pathlib import Path

def convert_tabs_to_spaces(file_path, tab_size=8):
    """Convert tabs to spaces in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace tabs with spaces
        converted = content.expandtabs(tab_size)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(converted)
        
        print(f"✓ Converted: {file_path}")
        return True
    except Exception as e:
        print(f"✗ Error converting {file_path}: {e}")
        return False

if __name__ == "__main__":
    files = [
        "octoprint_mgsetup/__init__.py",
        "octoprint_mgsetup/static/maintenance/scripts/hosts.py",
        "octoprint_mgsetup/static/maintenance/scripts/resetWatch.py",
        "octoprint_mgsetup/static/maintenance/scripts/resetWatchTest.py",
        "octoprint_mgsetup/static/maintenance/scripts/upload.py",
        "setup.py",
        "main.py",
    ]
    
    success_count = 0
    for file in files:
        file_path = Path(file)
        if file_path.exists():
            if convert_tabs_to_spaces(file_path):
                success_count += 1
        else:
            print(f"✗ File not found: {file}")
    
    print(f"\n{success_count}/{len(files)} files converted successfully")
