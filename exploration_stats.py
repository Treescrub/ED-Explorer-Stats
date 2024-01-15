import argparse
import os
import read_journals

from stat_groups import scanned_bodies
from stat_groups import visited_systems

PROGRAM_NAME = "ED Exploration Stats"
VERSION = "0.1.0"

def main():
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME)
    parser.add_argument("--saves_path", type=str, default="%USERPROFILE%/Saved Games/Frontier Developments/Elite Dangerous", help="path to the ED saved data")
    parser.add_argument("--version", action="version", version=f"{PROGRAM_NAME} v{VERSION}")
    
    args = parser.parse_args()
    saves_path = os.path.expandvars(args.saves_path)
    
    for event in read_journals.read_events(saves_path):
        pass
    
if __name__ == "__main__":
    main()