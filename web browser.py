#!/usr/bin/env python
import gi.repository
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, WebKit, GObject


class MyWindowWebKit:
    default_site = "http://www.google.com"


    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_resizable(True)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        self.web_view = WebKit.WebView()
        self.web_view.open(self.default_site)

        scroll_window = Gtk.ScrolledWindow(None, None)
        scroll_window.add(self.web_view)

        self.window.add(scroll_window)
        self.window.show_all()

    def main(self):
        GObject.threads_init()
        Gtk.main()


mn = MyWindowWebKit()
mn.main()
