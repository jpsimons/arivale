#!/usr/bin/env python
#
# Copyright 2015 John Simons

import webapp2
from models.coach_availability import CoachAvailability
from models.appointment import Appointment
from google.appengine.ext import db
import logging, datetime, random

# Id of an arbitary client who isn't you.
SOMEONE_ELSE = 5

class MockHandler(webapp2.RequestHandler):
    """
    Fills the datastore with fake data.
    """
    def get(self):
        # Clear data
        db.delete(CoachAvailability.all())
        db.delete(Appointment.all())

        # Create availability for the next couple months
        morning = datetime.time(9, 0, 0)
        afternoon = datetime.time(13, 0, 0)
        today = datetime.date.today()

        for x in range(0, 60):
            date = today + datetime.timedelta(days = x)
            # Morning availability
            if random.random() > 0.2:
                slot = CoachAvailability(date = date,
                                         start_time = morning,
                                         duration_minutes = 180)
                slot.put()
                for hour in range(9, 12):
                    if random.random() > 0.5:
                        appt = Appointment(date = date,
                                           start_time = datetime.time(hour, 0, 0),
                                           duration_minutes = 60,
                                           client_id = SOMEONE_ELSE)
                        appt.put()
            # Afternoon availability
            if random.random() > 0.2:
                duration_minutes = 90 + int(random.random() * 10) * 30
                slot = CoachAvailability(date = date,
                                         start_time = afternoon,
                                         duration_minutes = duration_minutes)
                slot.put()
                for hour in range(13, 13 + duration_minutes / 60):
                    if (random.random() > 0.5):
                        appt = Appointment(date = date,
                                           start_time = datetime.time(hour, 0, 0),
                                           duration_minutes = 60,
                                           client_id = SOMEONE_ELSE)
                        appt.put()
        self.response.write('Done')
