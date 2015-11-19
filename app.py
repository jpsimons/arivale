#!/usr/bin/env python
#
# Copyright 2015 John Simons

import webapp2
import handlers.main
import handlers.mock
import handlers.schedule

app = webapp2.WSGIApplication([
    ('/', handlers.main.MainHandler),
    ('/mock', handlers.mock.MockHandler),
    ('/schedule', handlers.schedule.ScheduleHandler)
], debug=True)
