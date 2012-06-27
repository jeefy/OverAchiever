from storm.locals import *
from Sites import Site
from config.config import config

class Achievement(object):
    __storm_table__ = config['table_prefix'] + 'Achievements'
    id          = Int(primary = True)
    name        = Unicode()
    description = Unicode()
    site_id     = Int()
    site        = Reference(site_id, Site.id)
    