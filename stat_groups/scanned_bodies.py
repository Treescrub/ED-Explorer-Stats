from . import collector

def new_collector():
    return ScannedBodies()


class ScannedBodies(collector.Collector):
    bodies_scanned = None
    body_classes_scanned = None
    total = 0
    
    def __init__(self):
        bodies_scanned = set()
        body_classes_scanned = {}

    
    def process_event(self, event):
        if event["event"] != "Scan":
            return
        if "PlanetClass" not in event and "StarType" not in event:
            return
        if event["BodyName"] in bodies_scanned:
            return
        
        bodies_scanned.add(event["BodyName"])
        total += 1
        
        body_class = None
        
        if "PlanetClass" in event:
            body_class = event["PlanetClass"]
        elif "StarType" in event:
            body_class = event["StarType"]
        
        if body_class not in body_classes_scanned:
            body_classes_scanned[body_class] = 0
        
        body_classes_scanned[body_class] += 1
    
    
    def get_output(self):
        output = "Total: " + str(total) + "\n"
    
        for body_class in body_classes_scanned:
            output += body_class + ": " + str(body_classes_scanned[body_class])
        
        return output