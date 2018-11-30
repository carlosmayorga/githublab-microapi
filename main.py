from flask import Flask
from flask_restful import Resource, Api, reqparse
from utililies.repository import *
import urllib3
import json

app = Flask(__name__)
api = Api(app)

class Orquestator(Resource):
    def get(self):
        try:
            pullrequest = []
            parser = reqparse.RequestParser()
            parser.add_argument('milestone', type=str)
            parser.add_argument('state', type=str)
            parser.add_argument('group', type=str)
            #You can add more parameters
            args = parser.parse_args()
            pullrequest = self.get_pullrequest(args)
             
            return {'Status':'Ok', 'List':pullrequest}

        except Exception as e:
            return {'Status': 'Error', 'List':pullrequest}, 500, {'Etag': str(e)}

    def get_pullrequest(self, args):
          # Array for response
          pullrequest = []
          page = 0
          c = 0
          url = 'Put here your git lab|hub Url /api/v4/groups/{}/merge_requests'.format(args['group'])
          #You can use .format() to add parameter in middle of Url

          while True:
              page += 1 
              c = 0
              fields={'milestone':args['milestone'],'state':args['state'],'per_page':'100','page':page}
              response = call_api(url,fields)

              if (len(response) > 0):
                  for i in response:
                      item = {
                              'title':response[c]["title"],
                              'author':response[c]["author"]["name"],
                              'url':response[c]["web_url"]
                              #And any element that you want to add to response
                      }
                      pullrequest.append(item)
                      c += 1
              else:
                  break
          return pullrequest


api.add_resource(Orquestator, '/microapi')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')