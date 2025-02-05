import importlib.metadata
import logging

from ._logging import configure_logger

__version__ = importlib.metadata.version(__package__)

log = logging.getLogger(__package__)
configure_logger(log)
