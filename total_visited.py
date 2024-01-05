import argparse
import os
import read_journals

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--saves_path", type=str, default="%USERPROFILE%/Saved Games/Frontier Developments/Elite Dangerous", help="The path to the ED saved data")
    
    args = parser.parse_args()
    saves_path = os.path.expandvars(args.saves_path)

    visited_systems = set()

    for event in read_journals.read_events(saves_path):
        if event["event"] != "Scan":
            continue
        if event["ScanType"] != "AutoScan":
            continue
        if not event["BodyName"].startswith(event["StarSystem"]):
            continue
            
        visited_systems.add(event["StarSystem"])
    
    print(len(visited_systems))

if __name__ == "__main__":
    main()