from .View import View

class PygameView(View):
    def __init__(self,surface):
        View.__init__(self)
        self.surface=surface
    