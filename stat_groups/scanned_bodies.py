from . import collector


def new_collector():
    return ScannedBodies()


def get_description():
    return "Counts of all scanned stellar bodies"


def setup_parser(parser):
    pass


class ScannedBodies(collector.Collector):
    bodies_scanned = None
    planet_classes_scanned = None
    star_types_scanned = None
    total = 0
    
    def __init__(self):
        self.bodies_scanned = set()
        self.planet_classes_scanned = {}
        self.star_types_scanned = {}

    
    def process_event(self, event):
        if event["event"] != "Scan":
            return
        if "PlanetClass" not in event and "StarType" not in event:
            return
        if event["BodyName"] in self.bodies_scanned:
            return
        
        self.bodies_scanned.add(event["BodyName"])
        self.total += 1
        
        if "PlanetClass" in event:
            planet_class = event["PlanetClass"]
            
            if planet_class not in self.planet_classes_scanned:
                self.planet_classes_scanned[planet_class] = 0
            
            self.planet_classes_scanned[planet_class] += 1
        elif "StarType" in event:
            star_type = event["StarType"]
            
            if star_type not in self.star_types_scanned:
                self.star_types_scanned[star_type] = 0
            
            self.star_types_scanned[star_type] += 1
    
    
    def get_output(self):
        output = "Scanned bodies\n"
        output += "\tTotal: " + str(self.total) + "\n"
    
        output += "\n\tStars:\n"
        for star_type in sorted(self.star_types_scanned):
            output += "\t" + star_type + ": " + str(self.star_types_scanned[star_type]) + "\n"
            
        output += "\n\tPlanets:\n"
        for planet_class in sorted(self.planet_classes_scanned):
            output += "\t" + planet_class + ": " + str(self.planet_classes_scanned[planet_class]) + "\n"
        
        return output