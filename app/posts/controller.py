from flask.views import MethodView

class PostGeneral(MethodView):
    def post(self, **kwargs):
        pass

    def get(self, **kwargs):
        pass

class PostSpecific(MethodView):

    def get(self, **kwargs):
        pass

    def patch(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass