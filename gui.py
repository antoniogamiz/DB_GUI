#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import os
os.system("clear")

class Handler:
    builder=None
    def __init__(self):
        #Iniciamos el GtkBuilder para tirar del fichero de glade.
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui.blade")
        self.handlers = {
                        "onDeleteWindow" : self.onDeleteWindow,
                        "on_button1_clicked" : self.on_button1_clicked,
                        "on_button2_clicked" : self.on_button2_clicked,
                        "on_button3_clicked" : self.on_button3_clicked
                        }
        #Conectamos las señales e iniciamos la applicación.
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window1")
        self.button1 = self.builder.get_object("button1")
        self.button2 = self.builder.get_object("button2")
        self.button3 = self.builder.get_object("button3")
        self.window.show_all()
        self.window.resize(300,300)
    def onDeleteWindow(self, *args):
        print "Cerrando"
        Gtk.main_quit(*args)
    def on_button1_clicked(self, window):
        print "Boton 1"
    def on_button2_clicked(self, window):
        print "Boton 2"
    def on_button3_clicked(self, window):
        self.onDeleteWindow(self, window)

def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()