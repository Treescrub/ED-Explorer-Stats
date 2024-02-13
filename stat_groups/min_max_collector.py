from . import collector

class MinMaxCollector(collector.Collector):
    notable_stars = None
    notable_bodies = None
    
    def __init__(self):
        super().__init__()
    
        self.notable_stars = {}
        self.notable_bodies = {}
    
    
    def get_object_info(self, object_name, system_name, stat):
        return {
            "name": self.shorten_body_name(object_name, system_name),
            "stat": stat,
            "system": system_name,
        }
    
    
    def shorten_body_name(self, name, system):
        if name == system:
            return name
        
        if name.startswith(system):
            return name[len(system)+1:]
        
        return name