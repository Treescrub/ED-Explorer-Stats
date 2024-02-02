from . import collector
import stellar_info


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


    def get_star_type_name(self, type):
        if type[0] == "D":
            return f"White dwarf ({type})"
        
        if type in self._star_type_names:
            return self._star_type_names[type]
        else:
            return type

    
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
    
    
    def get_stellar_remnant_names(self):
        names = {}
    
        for type in stellar_info.stellar_remnant_types():
            names[stellar_info.type_to_name(type)] = type
        
        return names
    
    
    def get_output(self):
        output = "Scanned bodies\n\n"
        output += f"Total: {self.total}\n\n\n"
        
        output += "Stellar remnants:\n\n"
        stellar_remnant_names = self.get_stellar_remnant_names()
        for name in sorted(stellar_remnant_names):
            type = stellar_remnant_names[name]
            count = self.star_types_scanned.get(type, 0)
            output += f"\t{name}: {count}\n"
            
            if type in self.star_types_scanned:
                del self.star_types_scanned[type]
        
        output += "\nMain sequence stars:\n\n"
        for type in ["O", "B", "A", "F", "G", "K", "M"]:
            output += f"\t{type} star: {self.star_types_scanned.get(type, 0)}\n"
            
            if type in self.star_types_scanned:
                del self.star_types_scanned[type]
        
        output += "\nDwarf stars:\n\n"
        for type in ["Y", "T", "L"]:
            output += f"\t{type} brown dwarf: {self.star_types_scanned.get(type, 0)}\n"
            
            if type in self.star_types_scanned:
                del self.star_types_scanned[type]
        
        output += "\nOther:\n\n"
        for type in sorted(self.star_types_scanned):
            name = stellar_info.type_to_name(type)
            output += f"\t{name}: {self.star_types_scanned[type]}\n"
        
        output += "\nPlanets:\n"
        for planet_class in sorted(self.planet_classes_scanned):
            output += f"\t{planet_class}: {self.planet_classes_scanned[planet_class]}\n"
        
        return output