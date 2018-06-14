from flask_restful import Resource


class Status(Resource):

    def get(self):
        return {'message': 'OK', 'version': "2.6.0"}, 200
