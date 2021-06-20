import cherrypy
import hashlib
import sys
import os

class LoginCheck(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <div>This page is used to check the password for the status page. </div>
          </body>
        </html>"""


    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def loginCheck(self, **params):
        hash_value = ''
        params = cherrypy.request.params   
        for value in params.values():
            hash_value = hashlib.sha1(value.encode()).hexdigest()
        if hash_value == '2a9c1ff8c145af3600241455dcebbef9f8567917' :
            return "Correct"
        else:
            return "Incorrect Password"

################################ Sys parameters ###############################
serviceURL = sys.argv[1]
servicePort = int(sys.argv[2])

if __name__ == '__main__':
    config = {'server.socket_host': serviceURL}
    cherrypy.config.update(config)

    # Update the configuration to your host
    cherrypy.config.update({'server.socket_port': servicePort})
    
    # cherrypy.config.update({'server.socket_host': 'dickens.seas.upenn.edu', 'server.socket_port': 4049})
    '''
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
       '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../frontend/js'
        },
       '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../frontend/css'
        },
    }
'''


    cherrypy.quickstart(LoginCheck())