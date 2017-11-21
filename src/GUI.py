#!/usr/bin/python
#-*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import DB_funcionality as DBlib

import os
os.system("clear")

    


class Handler:
    builder=None
    def __init__(self):
        self.DB_initializated = False
        #----------------------------GLADE AND SIGNAL INITIALIZATION----------------------------
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./GUI/GUI.glade")
        self.handlers = {
                        "on_main_destroy" : Gtk.main_quit,
                        "on_add_button_clicked" : self.on_add_button_clicked,
                        "on_delete_button_clicked" : self.on_delete_button_clicked,
                        "on_update_button_clicked" : self.on_update_button_clicked,
                        "on_edit_button_clicked" : self.on_edit_button_clicked,
                        "on_load_button_clicked" : self.on_load_button_clicked
                        }
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("main")

        #----------------------------CRUD BUTTONS----------------------------
        
        self.add_button = self.builder.get_object("add_button")
        self.delete_button = self.builder.get_object("delete_button")
        self.update_button = self.builder.get_object("update_button")
        self.edit_button = self.builder.get_object("edit_button")
        self.load_button = self.builder.get_object("load_button")

        #----------------------------TREE VIEW MANAGEMENT----------------------------
        
        self.treeView_DB = self.builder.get_object("treeView_DB")

        self.model = Gtk.ListStore(int, str, str, str, str, str)

        self.model.append([1,"Working","Working","Working","Working","Working"])
        self.model.append([2,"Working","Working","Working","Working","Working"])
        self.model.append([3,"Working","Working","Working","Working","Working"])
        self.model.append([4,"Working","Working","Working","Working","Working"])
        self.model.append([5,"Working","Working","Working","Working","Working"])

        self.treeView_DB.set_model(self.model)

        renderer0 = Gtk.CellRendererText(xalign=0.5)
        column0 = Gtk.TreeViewColumn("Field 0", renderer0, text=0)
        self.treeView_DB.append_column(column0)

        renderer1 = Gtk.CellRendererText(xalign=0.5)
        column1 = Gtk.TreeViewColumn("Field 1", renderer1, text=1)
        self.treeView_DB.append_column(column1)

        renderer2 = Gtk.CellRendererText(xalign=0.5)
        column2 = Gtk.TreeViewColumn("Field 2", renderer2, text=2)
        self.treeView_DB.append_column(column2)

        renderer3 = Gtk.CellRendererText(xalign=0.5)
        column3 = Gtk.TreeViewColumn("Field 3", renderer3, text=3)
        self.treeView_DB.append_column(column3)

        renderer4 = Gtk.CellRendererText(xalign=0.5)
        column4 = Gtk.TreeViewColumn("Field 4", renderer4, text=4)
        self.treeView_DB.append_column(column4)

        renderer5 = Gtk.CellRendererText(xalign=0.5)
        column5 = Gtk.TreeViewColumn("Field 5", renderer5, text=5)
        self.treeView_DB.append_column(column5)

        #----------------------------WINDOW PREFERENCES----------------------------
        self.window.show_all()

    #----------------------------CRUD BUTTONS(FUNCTIONS CLICKED)----------------------------
    
    def on_add_button_clicked(self,button):
        if self.DB_initializated:
            self.DB.addRegister(1,"TESTING","TESTING","TESTING","TESTING","TESTING")

    def on_delete_button_clicked(self,button):
        print("Delete button")
    
    def on_update_button_clicked(self,button):
        data = self.DB.getRegisters()
        for reg in data:
            self.model.append(reg)
        print("DB updated")        
    
    def on_edit_button_clicked(self,button):
        print("Edit button")
    
    def on_load_button_clicked(self, button):
        if not self.DB_initializated:
            self.DB = DBlib.DB_Handler()
            self.DB.openDB(host='localhost', user='antonio', passwd='antonio', db='GUI')
            data = self.DB.getRegisters()
            print(data)
            for reg in data:
                self.model.append(reg)
            self.DB_initializated = True
            print("DB initializated")

def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()