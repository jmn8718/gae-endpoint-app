import os

from google.appengine.api import users

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class DashboardPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()        
        if user is not None:
            template = JINJA_ENVIRONMENT.get_template('templates/pages/dashboard.html')
            self.response.write(template.render({'user':user}))
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/dashboard', DashboardPage),
], debug=True)


