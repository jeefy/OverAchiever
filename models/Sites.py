from storm.locals import *
import hashlib
import random
import string
from config.config import config

class Site(object):
    __storm_table__ = config['table_prefix'] + 'Sites'
    id             = Int(primary = True)
    display_name   = Unicode()
    description    = Unicode()
    avatar         = Unicode()
    date_created   = Date()
    email          = Unicode()
    username       = Unicode()
    password       = Unicode()
    activation     = Unicode()
    acccount_state = Int()
    
    def __init__(self, store):
        #sup
        self.store = store
    
    def create(self, username, password):
        m = hashlib.md5()
        m.update(password + config['site_salt'])
        
        self.username = username
        self.password = m.hexdigest()
        
        self.store.add(self)
        self.store.flush()
        return True
        
    def update(self, display_name, description, avatar):
        self.display_name = display_name
        self.description  = description
        self.avatar       = avatar
        
        self.store.commit()
        return True
    
    def delete(self):
        self.store.remove(self)
        return True
    
    def change_password(self, old_password, new_password):
        m = hashlib.md5()
        old = m.update(old_password + config['site_salt']).hexdigest()
        if old is not self.password:
            return False
        
        self.password = m.update(new_password + config['site_salt']).hexdigest()
        self.store.commit()
        return True
        
    def randomize_password(self):
        m = hashlib.md5()
        new_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(12))
        self.password = m.update(new_password + config['site_salt']).hexdigest()
        self.email('Lost Password Recovery', 'Temporary password is: ' + new_password)
        self.store.commit()
        return True
        
    def forgotten_username(self, email):
        #sup
        return False
        
    def email(self, subject, message):
        #sup
        return False
        
    def activate(self, activation_code):
        #sup
        return False
        
    def username_exists(self, username):
        #sup
        return False