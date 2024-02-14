from enum import Enum

class ForegroundColor(Enum):
    RED = "\x1B[31m"
    GREEN = "\x1B[32m"
    BLUE = "\x1B[34m"
    MAGENTA = "\x1B[35m"
    CYAN = "\x1B[36m"


class BackgroundColor(Enum):
    RED = "\x1B[41m"
    GREEN = "\x1B[42m"
    BLUE = "\x1B[44m"
    MAGENTA = "\x1B[45m"
    CYAN = "\x1B[46m"


class ColorGroup(Enum):
    def __str__(self):
        return str(self.value)

    DEFAULT = "\x1B[39;49m"
    RESET = "\x1B[0m"
    TITLE = "\x1B[1;31m" # red
    SECTION_TITLE = "\x1B[32m" # green
    TYPE = "\x1B[36m" # cyan
    STAT = "\x1B[33m" # yellow