VERSION = (24, 2, 10, "")

__version_info__ = VERSION
__version__ = ".".join(map(str, VERSION[:3])) + (f"-{VERSION[3]}" if VERSION[3] else "")
