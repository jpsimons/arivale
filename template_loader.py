import jinja2
import os, datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def hour_formatted(hour):
    return datetime.time(hour, 0, 0).strftime('%I:%M %p').strip('0')

JINJA_ENVIRONMENT.filters['hour_formatted'] = hour_formatted

def getTemplate(name):
    return JINJA_ENVIRONMENT.get_template('templates/' + name)
