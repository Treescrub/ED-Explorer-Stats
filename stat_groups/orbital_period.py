from . import collector
import datetime
import stellar_info

def new_collector():
    return OrbitalPeriod()


def get_description():
    return "Objects with notable orbital periods"


def setup_parser(parser):
    pass


class OrbitalPeriod(collector.Collector):
    notable_stars = None
    notable_bodies = None

    def __init__(self):
        super().__init__()
        
        self.notable_stars = {}
        self.notable_bodies = {}


    def process_event(self, event):
        if event["event"] != "Scan":
            return
        if "OrbitalPeriod" not in event:
            return
        
        orbital_period = event["OrbitalPeriod"]
        system_name = event["StarSystem"]
        object_name = self.shorten_body_name(event["BodyName"], system_name)
        
        object_info = {
            "name": object_name,
            "period": orbital_period,
            "system": system_name,
        }
        
        if "StarType" in event:
            self.check_body(self.notable_stars, event["StarType"], object_info)
        elif "PlanetClass" in event:
            self.check_body(self.notable_bodies, event["PlanetClass"], object_info)
    
    
    def check_body(self, lookup_dict, type, object_info):
        if type not in lookup_dict:
            lookup_dict[type] = {
                "highest": object_info,
                "lowest": object_info,
            }
        else:
            if lookup_dict[type]["highest"]["period"] < object_info["period"]:
                lookup_dict[type]["highest"] = object_info
            if lookup_dict[type]["lowest"]["period"] > object_info["period"]:
                lookup_dict[type]["lowest"] = object_info
    
    
    def get_output(self):
        self.add_line("Orbital period\n")
        
        self.add_line("Stars:")
        for type in sorted(self.notable_stars):
            self.add_type_info(stellar_info.type_to_name(type), self.notable_stars[type])
            self.add_line()
        
        self.add_line()
        self.add_line("Planets/moons:")
        for type in sorted(self.notable_bodies):
            self.add_type_info(type, self.notable_bodies[type])
            self.add_line()
        
        return self._output
    
    
    def shorten_body_name(self, name, system):
        if name == system:
            return name
        
        if name.startswith(system):
            return name[len(system)+1:]
        
        return name
    
    
    def add_type_info(self, type_name, info):
        self.add_line(type_name)
        
        highest_info = info["highest"]
        lowest_info = info["lowest"]
            
        highest_system = highest_info["system"]
        lowest_system = lowest_info["system"]
        
        highest_object = highest_info["name"]
        lowest_object = lowest_info["name"]
        
        highest_formatted = self.format_period(highest_info["period"])
        lowest_formatted = self.format_period(lowest_info["period"])
        
        self.add_line(f"\tHighest: {highest_formatted} (object {highest_object} in system {highest_system})")
        self.add_line(f"\tLowest: {lowest_formatted} (object {lowest_object} in system {lowest_system})")
    
    
    def format_period(self, period):
        delta = datetime.timedelta(seconds=period)
        
        seconds = delta.seconds % 60
        minutes = delta.seconds // 60 % 60
        hours = delta.seconds // (60 * 60)
        
        days = delta.days % 7
        weeks = delta.days // 7 % 7
        years = delta.days // 365
        
        if years >= 10:
            return f"{years} years"
        
        result = f"{seconds} seconds"
        
        if minutes > 0:
            result = f"{minutes} minutes, " + result
        if hours > 0:
            result = f"{hours} hours, " + result
        if days > 0:
            result = f"{days} days, " + result
        if weeks > 0:
            result = f"{weeks} weeks, " + result
        if years > 0:
            result = f"{years} years, " + result
        
        return result