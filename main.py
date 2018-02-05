#!/usr/bin/env python

# import
import jedi
import gi

# PyGObject
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

#==============================================================================#

# class
class Dummy():
    # constructor
    def __init__(self, **args):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('/home/frederico/virtualenvs/pygi/pygi/interface.ui')
        self.builder.connect_signals(self)

    # destroy
    def destroy(self, **args):
        Gtk.main_quit()

    # Run
    def Run(self, **args):
        self.builder.get_object('window1')
        Gtk.main()

#==============================================================================#
if __name__ == "__main__":
    user = Dummy()
    user.Run()
