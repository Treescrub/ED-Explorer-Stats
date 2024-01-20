import argparse
import os
import read_journals

import stat_groups
from stat_groups import *

PROGRAM_NAME = "ED Exploration Stats"
VERSION = "0.1.0"

def main():
    parser = build_arg_parser()
    
    args = parser.parse_args()
    
    if not args.stat_group:
        run_main()
    else:
        stat_group_name = args.stat_group
        if stat_group_name not in stat_groups.get_stat_group_modules():
            invalid_stat_group(stat_group_name)
        else:
            run_stat_group(args)


def run_stat_group(args):
    module = stat_groups.__dict__[args.stat_group]
    collector = module.new_collector()
    
    saves_path = os.path.expandvars(args.saves_path)
    
    for event in read_journals.read_events(saves_path):
        collector.process_event(event)
    
    print(collector.get_output())

def invalid_stat_group(name):
    print(f"Invalid stat group '{name}', probably missing in package init file")


def run_main():
    print_stat_groups()


def print_stat_groups():
    for name in stat_groups.get_stat_group_modules(): 
        print(name + " - " + stat_groups.__dict__[name].get_description())


def build_arg_parser():
    parser = argparse.ArgumentParser(prog=PROGRAM_NAME)
    parser.add_argument("--saves_path", type=str, default="%USERPROFILE%/Saved Games/Frontier Developments/Elite Dangerous", help="path to the ED saved data")
    parser.add_argument("--version", action="version", version=f"{PROGRAM_NAME} v{VERSION}")
    
    subparsers = parser.add_subparsers(dest="stat_group")
    
    scanned_bodies_parser = subparsers.add_parser("scanned_bodies")
    visited_systems_parser = subparsers.add_parser("visited_systems")
    
    return parser

    
if __name__ == "__main__":
    main()