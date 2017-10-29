#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import tornado.escape
import sys

class LogHandler(tornado.web.RequestHandler):
    def post(self, device_id):
        data = tornado.escape.json_decode(self.request.body)
        sys.stderr.write("Received headers: %s\n"%str(self.request.headers))
        sys.stderr.write("Received payload: %s\n"%str(data))
        self.finish({'status': 'ok'})

def make_app():
    return tornado.web.Application([
        (r"/temperature/([^/]+)", LogHandler)])

if __name__=='__main__':
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
