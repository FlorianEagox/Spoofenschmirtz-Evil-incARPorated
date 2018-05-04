import gi.repository

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, WebKit, GObject


class WebRenderer(Gtk.Window):
    def __init__(self, ui):
        Gtk.Window.__init__(self)
        self.set_decorated(False)
        self.connect("delete-event", Gtk.main_quit)
        self.move(ui.webFrameHolder.winfo_rootx(), ui.webFrameHolder.winfo_rooty())
        self.web_view = WebKit.WebView()
        self.web_view.open("file://~/outPut.html")
        scroll_window = Gtk.ScrolledWindow(None, None)
        scroll_window.add(self.web_view)

        self.add(scroll_window)
        self.resize(ui.webFrameHolder.winfo_width(), ui.webFrameHolder.winfo_height())
        self.show_all()

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        Gtk.main_quit()
