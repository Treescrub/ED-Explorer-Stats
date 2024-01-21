from . import collector

def new_collector():
    return VisitedSystems()


def get_description():
    return "Total systems visited"


def setup_parser(parser):
    pass


class VisitedSystems(collector.Collector):
    visited_systems = None

    def __init__(self):
        self.visited_systems = set()


    def process_event(self, event):
        if event["event"] != "Scan" and event["event"] != "Location" and event["event"] != "FSDJump":
            return
            
        self.visited_systems.add(event["StarSystem"])
    
    
    def get_output(self):
        output = "Visited systems\n"
        output += "\tTotal visited systems: " + str(len(self.visited_systems))
        
        return output