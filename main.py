#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        motors = [{"name":"Small Motor", "url":"smallMotor"},{},{}]
        luminence = [{"name":"Lights", "url":"lights"}, {"name":"White Space", "url":"whiteSpace"} ]
		
        this = {
		    "directed": False, 
		    "graph": [[
		            "name", 
		            "myGraph"]], 
		    "nodes": [
		        {
		            "gate": "this", 
		            "id": 1
		        }
		    ], 
		    "links": [
		        # {
		        #     "source": 3, 
		        #     "target": 2
		        # }, 
		        # {
		        #     "source": 0, 
		        #     "target": 3
		        # }, 
		        # {
		        #     "source": 1, 
		        #     "target": 3
		        # }
		    ], 
		    "multigraph": False
		}
        
        self.response.out.write(template.render(path,{ "this":this, "motors":motors }))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
