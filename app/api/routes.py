from .resources.status import Status


def init_routes(api):
    """routes"""
    api.add_resource(Status, '/status')