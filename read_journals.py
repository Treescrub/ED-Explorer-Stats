import json
import os

def read_events(path):
    journal_paths = []

    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        
        if not os.path.isfile(entry_path) or not entry.startswith("Journal.") or not entry.endswith(".log"):
            continue
        
        for event in _read_journal(entry_path):
            yield event

def _read_journal(path):
    with open(path) as journal_file:
        for line in journal_file:
            event = json.loads(line)
            
            yield event