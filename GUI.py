#!/usr/bin/python3
#-*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import os
os.system("clear")

    


class Handler:
    builder=None
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("GUI.blade")
        self.handlers = {
                        "on_main_destroy" : Gtk.main_quit,
                        "on_add_button_clicked" : self.on_add_button_clicked
                        }
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("main")
        self.add_button = self.builder.get_object("add_button")
        self.grid = self.builder.get_object("grid")
        model = Gtk.ListStore(str)
        model.append(["Benjamin"])
        model.append(["Charles"])
        model.append(["alfred"])
        model.append(["Alfred"])
        model.append(["David"])
        model.append(["charles"])
        model.append(["david"])
        model.append(["benjamin"])

        treeView = Gtk.TreeView(model)

        cellRenderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", cellRenderer, text=0)
        self.grid.add(treeView)

        self.window.show_all()
        self.window.resize(300,300)
    def on_add_button_clicked(self, button):
        print("Botton pressed")

def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()