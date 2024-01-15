from . import collector

def new_collector():
    return VisitedSystems()


class VisitedSystems(collector.Collector):
    visited_systems = None

    def __init__(self):
        visited_systems = set()

    def process_event(self, event):
        if event["event"] != "Scan" and event["event"] != "Location" and event["event"] != "FSDJump":
            return
            
        visited_systems.add(event["StarSystem"])
    
    def get_output(self):
        return "Total visited systems: " + str(len(visited_system))