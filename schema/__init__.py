import logging
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(logging.StreamHandler())

from redis import StrictRedis
from juggernaut import Juggernaut

redis = StrictRedis()
jug = Juggernaut()

from schema.entity import Entity
from schema.aspect import Aspect, action, before, after
from schema.zone import Zone
from schema.event import Event
