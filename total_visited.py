import json
import sys
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--saves_path", type=str, default="%USERPROFILE%/Saved Games/Frontier Developments/Elite Dangerous", help="The path to the ED saved data")
    
    args = parser.parse_args()
    saves_path = os.path.expandvars(args.saves_path)

    journal_paths = []

    for entry in os.listdir(saves_path):
        entry_path = os.path.join(saves_path, entry)
        
        if os.path.isfile(entry_path) and entry.startswith("Journal.") and entry.endswith(".log"):
            journal_paths.append(entry_path)

    all_systems_visited = set()

    for journal_path in journal_paths:
        all_systems_visited.update(get_systems_visited(journal_path))
    
    print(len(all_systems_visited))
                
def get_systems_visited(journal_path):
    visited_systems = set()
    
    with open(journal_path) as journal_file:
        for line in journal_file:
            event = json.loads(line)
            
            if event["event"] != "Scan":
                continue
            if event["ScanType"] != "AutoScan":
                continue
            if not event["BodyName"].startswith(event["StarSystem"]):
                continue
            
            visited_systems.add(event["StarSystem"])
    
    return visited_systems

if __name__ == "__main__":
    main()