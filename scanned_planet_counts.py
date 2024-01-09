import argparse
import os
import read_journals

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--saves_path", type=str, default="%USERPROFILE%/Saved Games/Frontier Developments/Elite Dangerous", help="The path to the ED saved data")
    
    args = parser.parse_args()
    saves_path = os.path.expandvars(args.saves_path)

    planets_scanned = set()
    planet_classes_scanned = {}
    total = 0

    for event in read_journals.read_events(saves_path):
        if event["event"] != "Scan":
            continue
        if "PlanetClass" not in event:
            continue
        if event["BodyName"] in planets_scanned:
            continue
        
        planets_scanned.add(event["BodyName"])
        
        total += 1
        planet_class = event["PlanetClass"]
        
        if planet_class not in planet_classes_scanned:
            planet_classes_scanned[planet_class] = 0
        
        planet_classes_scanned[planet_class] += 1
    
    print("Total: " + str(total) + "\n")
    
    for planet_class in planet_classes_scanned:
        print(planet_class + ": " + str(planet_classes_scanned[planet_class]))

if __name__ == "__main__":
    main()