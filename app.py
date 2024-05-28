from window import *

class App(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.example.TestApp", **kwargs)
        GLib.set_application_name('Gtk Test')
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        if not self.window:
            self.window = Window(application=self, title='Main Window')
        self.window.present()
