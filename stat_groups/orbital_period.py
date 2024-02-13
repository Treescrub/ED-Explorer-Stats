from . import min_max_collector
import datetime
import stellar_info

def new_collector():
    return OrbitalPeriod()


def get_description():
    return "Objects with notable orbital periods"


def setup_parser(parser):
    pass


class OrbitalPeriod(min_max_collector.MinMaxCollector):
    def __init__(self):
        super().__init__()


    def process_event(self, event):
        if event["event"] != "Scan":
            return
        if "OrbitalPeriod" not in event:
            return
    
        object_info = self.get_object_info(event["BodyName"], event["StarSystem"], event["OrbitalPeriod"])
        
        if "StarType" in event:
            self.check_body(self.notable_stars, event["StarType"], object_info)
        elif "PlanetClass" in event:
            self.check_body(self.notable_bodies, event["PlanetClass"], object_info)
    
    
    def get_output(self):
        self.add_line("Orbital period\n")
        
        self.add_line("Stars:")
        for type in stellar_info.sorted_types():
            if type not in self.notable_stars:
                continue
            
            self.add_type_info(stellar_info.type_to_name(type), self.notable_stars[type])
            self.add_line()
        
        self.add_line()
        self.add_line("Planets/moons:")
        for type in sorted(self.notable_bodies):
            self.add_type_info(type, self.notable_bodies[type])
            self.add_line()
        
        return self._output
    
    
    def get_formatted_stat(self, stat):
        delta = datetime.timedelta(seconds=stat)
        
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