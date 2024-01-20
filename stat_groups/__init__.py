__all__ = [
    "scanned_bodies",
    "visited_systems",
    "most_bodies",
]

def get_module_names():
    return __all__


def get_module(name):
    return globals()[name]