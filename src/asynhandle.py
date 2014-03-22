#!/bin/python

import tornado.httpclient
import tornado.gen
import traceback
import urllib2
import json
import time
 
import mylog

client = tornado.httpclient.AsyncHTTPClient()
class handler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        try:
            s_time = time.time()
            result = yield self.do()
            self.write("%s" % result)
            mylog.LOG.ERROR("end_test:%s" % (time.time()-s_time))
            self.end()
        except Exception,err:
            mylog.LOG.ERROR("error:%s" % (err))
            mylog.LOG.ERROR("traceback:%s" % (traceback.format_exc()))
            self.finish()

    @tornado.gen.coroutine
    def do(self):
        mylog.LOG.ERROR("do it")
        result = yield self.url_query()
        raise tornado.gen.Return("do it ok! %s" % result)
        

    @tornado.gen.coroutine
    def url_query(self):
        request = tornado.httpclient.HTTPRequest(url="http://localhost:8080/basetest/sleep", request_timeout=5)
#        response1, response2 = yield [tornado.gen.Task(client.fetch, request),tornado.gen.Task(client.fetch, request)]
#        mylog.LOG.ERROR("fetch_error_code 1:%s" % (response1.code))
#        mylog.LOG.ERROR("fetch_error_code 2:%s" % (response2.code))
#        mylog.LOG.ERROR("fetch_error_reason 1:%s" % (response1.reason))
#        mylog.LOG.ERROR("fetch_error_reason 2:%s" % (response2.reason))
#        mylog.LOG.ERROR("fetch_test_request_time 1:%s" % (response1.request_time))
#        mylog.LOG.ERROR("fetch_test_request_time 2:%s" % (response2.request_time))
#        timediff1 = response1.body
#        timediff2 = response2.body
#        mylog.LOG.ERROR("fetch_test 1:%s" % (timediff1))
#        mylog.LOG.ERROR("fetch_test 2:%s" % (timediff2))
        response = yield tornado.gen.Task(client.fetch, request)
        if response.code != 200:
            mylog.LOG.ERROR("fetch_error_code :%s" % (response.code))
            mylog.LOG.ERROR("fetch_error_reason :%s" % (response.reason))
            raise tornado.gen.Return("error")
        timediff = response.body
        mylog.LOG.ERROR("fetch_test :%s" % (timediff))
        raise tornado.gen.Return("ok")

    def end(self):
        self.write("ok")
        self.finish()

    def write_error(self, status_code, **kwargs):
        mylog.LOG.ERROR("error :%s" % (kwargs))
        if "exc_info" in kwargs:
            exc_info = kwargs["exc_info"]
            for line in traceback.format_exception(*exc_info):
                mylog.LOG.ERROR("%s" % line)
            self.write("Exception: %s" % kwargs["exc_info"][0].__name__)
        else:
            self.write("Status: %d" % status_code)
        self.finish()



