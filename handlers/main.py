#!/usr/bin/env python
#
# Copyright 2015 John Simons

import webapp2
import template_loader
import logging, datetime, json
from models.coach_availability import CoachAvailability
from models.appointment import Appointment


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Date management
        date = self.request.get('date')
        if date:
            date = datetime.date(*[int(x) for x in date.split('/')])
        else:
            date = datetime.date.today()
        prev = date - datetime.timedelta(days = 1)
        next = date + datetime.timedelta(days = 1)

        q = CoachAvailability.all()
        q.filter("date = ", date)
        availability = [r.toJson() for r in q.run()]

        q = Appointment.all()
        q.filter("date = ", date)
        appointments = [r.toJson() for r in q.run()]

        template_values = {
            'coach_availability': availability,
            'coach_appointments': appointments,
            'date_formatted': date.strftime('%B %d, %Y'),
            'date': date.strftime('%Y/%m/%d'),
            'prev': prev.strftime('%Y/%m/%d'),
            'next': next.strftime('%Y/%m/%d'),
            'client_name': 'John Simons',
            'client_id': 1
        }
        template = template_loader.getTemplate('index.html')
        self.response.write(template.render(template_values))
