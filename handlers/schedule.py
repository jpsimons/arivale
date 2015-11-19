#!/usr/bin/env python
#
# Copyright 2015 John Simons

import webapp2
import template_loader
import logging, datetime, json
from models.coach_availability import CoachAvailability
from models.appointment import Appointment


class ScheduleHandler(webapp2.RequestHandler):
    def post(self):
        # Parse date
        date = self.request.get('date')
        dateParts = date.split('/')
        year = int(dateParts[0])
        month = int(dateParts[1])
        day = int(dateParts[2])
        date = datetime.date(year, month, day)

        # Parse time
        hour = int(self.request.get('hour'))
        minute = int(self.request.get('minute'))
        ampm = self.request.get('ampm')
        if ampm == 'pm':
            hour += 12
        time = datetime.time(hour, minute, 0)

        # Insert to database
        appt = Appointment(date = date, start_time = time, duration_minutes = 60, client_id = 1)
        appt.put()

        self.response.write('OK')
