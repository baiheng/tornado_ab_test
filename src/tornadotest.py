#!/usr/bin/python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import sys
 
import asynhandle
import mylog


class myapplication(tornado.web.Application):
    def log_request(self, handler):
        request_time = 1000.0 * handler.request.request_time()
        mylog.LOG.ERROR("%d %s %.2fms" % (handler.get_status(),
                handler._request_summary(), request_time))

 
if __name__ == "__main__":
    define("port", default=8000, help="run on the given port", type=int)
#    define("logging", default="info",
#       help=("Set the Python log level. If 'none', tornado won't touch the logging configuration."),
#       metavar="debug|info|warning|error|none") 
    tornado.options.parse_config_file("/usr/local/x/tornadotest/conf/tornadotest_options.conf")
    app = myapplication(handlers=[(r"/tornadotest/", asynhandle.handler)], 
            debug=True, log_funciton=asynhandle.handler)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(sys.argv[1])
    tornado.ioloop.IOLoop.instance().start()



