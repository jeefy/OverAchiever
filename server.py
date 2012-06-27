import tornado.ioloop
import tornado.web

from storm.locals import *
from storm.store import Store
from storm.database import create_database

from models.Achievements import Achievement
from models.Sites import Site
from config.config import config

database = create_database(config['databaseURI'])
store = Store(database)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Big things have small beginnings(TM)")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()