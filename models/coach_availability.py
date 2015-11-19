from google.appengine.ext import db

class CoachAvailability(db.Model):
    date = db.DateProperty(required=True)
    start_time = db.TimeProperty(required=True)
    duration_minutes = db.IntegerProperty(required=True)

    def toJson(self):
        return {
            'start_hour': self.start_time.hour,
            'start_minute': self.start_time.minute,
            'duration_minutes': int(self.duration_minutes)
        }
