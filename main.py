#!/usr/local/bin/python
#coding:utf8
import tornado.ioloop
import tornado.web

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        print("get request")
        self.write({"str": "hello tornado"})

    def post(self):
        body = self.request.body
        print(body)
        self.write({"echo:": body})


def make_app():
    return tornado.web.Application([
        (r"/", TestHandler),
        (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': './static/favicon.ico'}),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': './static',}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(3003)
    tornado.ioloop.IOLoop.current().start()
