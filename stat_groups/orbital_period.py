from . import collector
import datetime

def new_collector():
    return OrbitalPeriod()


def get_description():
    return "Objects with notable orbital periods"


def setup_parser(parser):
    pass


class OrbitalPeriod(collector.Collector):
    highest_object_name = None
    highest_system_name = None
    highest_orbital_period = None
    lowest_object_name = None
    lowest_system_name = None
    lowest_orbital_period = None

    def __init__(self):
        super().__init__()
        
        self.highest_orbital_period = 0
        self.lowest_orbital_period = float("inf")


    def process_event(self, event):
        if event["event"] != "Scan":
            return
        if "OrbitalPeriod" not in event:
            return
        
        orbital_period = event["OrbitalPeriod"]
        object_name = event["BodyName"]
        system_name = event["StarSystem"]
        
        if orbital_period > self.highest_orbital_period:
            self.highest_object_name = object_name
            self.highest_system_name = system_name
            self.highest_orbital_period = orbital_period
        if orbital_period < self.lowest_orbital_period:
            self.lowest_object_name = object_name
            self.lowest_system_name = system_name
            self.lowest_orbital_period = orbital_period
    
    
    def get_output(self):
        highest_formatted = self.format_period(self.highest_orbital_period)
        lowest_formatted = self.format_period(self.lowest_orbital_period)
    
        self.add_line("Orbital period")
        self.add_line(f"\tHighest: {highest_formatted} with object {self.highest_object_name} in system {self.highest_system_name}")
        self.add_line(f"\tLowest: {lowest_formatted} with object {self.lowest_object_name} in system {self.lowest_system_name}")
        
        return self._output
    
    
    def format_period(self, period):
        delta = datetime.timedelta(seconds=period)
        
        seconds = delta.seconds % 60
        minutes = delta.seconds // 60 % 60
        hours = delta.seconds // (60 * 60)
        
        days = delta.days % 7
        weeks = delta.days // 7 % 7
        years = delta.days // 365
        
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