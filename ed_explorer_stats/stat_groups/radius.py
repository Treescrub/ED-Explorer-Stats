import datetime
from . import min_max_collector
from .. import stellar_info

def new_collector():
    return Radius()


def get_description():
    return "Objects with notable radius"


def setup_parser(parser):
    pass


class Radius(min_max_collector.MinMaxCollector):
    def __init__(self):
        super().__init__()


    def process_event(self, event):
        if event["event"] != "Scan":
            return
        if "Radius" not in event:
            return
        
        object_info = self.get_object_info(event["BodyName"], event["StarSystem"], event["Radius"])
        
        if "StarType" in event:
            self.check_body(self.notable_stars, event["StarType"], object_info)
        elif "PlanetClass" in event:
            self.check_body(self.notable_bodies, event["PlanetClass"], object_info)
    
    
    def get_output(self):
        self.add_line("Object radius\n")
        
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
        return f"{round(stat / 1000, 1)}km"