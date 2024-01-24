from . import collector
import datetime

def new_collector():
    return Radius()


def get_description():
    return "Objects with notable orbital periods"


def setup_parser(parser):
    pass


class Radius(collector.Collector):
    highest_object_name = None
    highest_system_name = None
    highest_radius = None
    lowest_object_name = None
    lowest_system_name = None
    lowest_radius = None

    def __init__(self):
        self.highest_radius = 0
        self.lowest_radius = float("inf")


    def process_event(self, event):
        if event["event"] != "Scan":
            return
        if "Radius" not in event:
            return
        
        radius = event["Radius"]
        object_name = event["BodyName"]
        system_name = event["StarSystem"]
        
        if radius > self.highest_radius:
            self.highest_object_name = object_name
            self.highest_system_name = system_name
            self.highest_radius = radius
        if radius < self.lowest_radius:
            self.lowest_object_name = object_name
            self.lowest_system_name = system_name
            self.lowest_radius = radius
    
    
    def get_output(self):
        output = "Object radius\n"
        output += f"\tHighest: {self.highest_radius}m with object {self.highest_object_name} in system {self.highest_system_name}\n"
        output += f"\tLowest: {self.lowest_radius}m with object {self.lowest_object_name} in system {self.lowest_system_name}"
        
        return output