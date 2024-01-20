from . import collector

def new_collector():
    return MostBodies()


def get_description():
    return "System with the most stellar objects"


def setup_parser(parser):
    pass


class MostBodies(collector.Collector):
    best_system_name = None
    best_body_count = None

    def __init__(self):
        self.best_body_count = 0

    def process_event(self, event):
        if event["event"] != "FSSDiscoveryScan": # Relying entirely on honking events can miss manual discovery
            return
        
        count = event["BodyCount"]
        system = event["SystemName"]
        
        if count > self.best_body_count:
            self.best_system_name = system
            self.best_body_count = count
    
    def get_output(self):
        output = f"Most bodies: {self.best_body_count} at system {self.best_system_name}"
        
        return output