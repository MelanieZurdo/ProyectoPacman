class Printable:
    view=None

    def set_view(self, view):
        self.view = view
        view.set_printable(self)

    def get_view(self):
        return self.view
