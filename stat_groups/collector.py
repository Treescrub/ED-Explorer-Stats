from colors import ColorGroup

class Collector:
    _output = None
    
    
    def __init__(self):
        self._output = ""
    

    def process_event(self, event):
        pass
    
    
    def add_line(self, text: str = ""):
        self._output += f"{text}\n{ColorGroup.RESET}"
    
    
    def get_output(self):
        pass