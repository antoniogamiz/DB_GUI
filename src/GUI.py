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
        self.treeIter = None
        #----------------------------GLADE AND SIGNAL INITIALIZATION----------------------------
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./GUI/GUI3.glade")
        self.handlers = {
                        "on_main_destroy" : Gtk.main_quit,
                        "on_add_button_clicked" : self.on_add_button_clicked,
                        "on_delete_button_clicked" : self.on_delete_button_clicked,
                        "on_update_button_clicked" : self.on_update_button_clicked,
                        "on_edit_button_clicked" : self.on_edit_button_clicked,
                        "on_load_button_clicked" : self.on_load_button_clicked,
                        "on_destroy_button_clicked" : self.on_destroy_button_clicked,
                        "on_about_dialog_response" : self.on_about_dialog_response,
                        "on_about_select" : self.on_about_select
                        }
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("main")

        self.window_grid = self.builder.get_object("window_grid")
        self.top_menu = self.builder.get_object("top_menu")
        self.about_dialog = self.builder.get_object("about_dialog")
        self.about_dialog.show()
        #----------------------------CRUD BUTTONS----------------------------
        
        self.crud_buttons_grid = self.builder.get_object("crud_buttons_grid")

        self.add_button = self.builder.get_object("add_button")
        self.delete_button = self.builder.get_object("delete_button")
        self.update_button = self.builder.get_object("update_button")
        self.edit_button = self.builder.get_object("edit_button")
        self.load_button = self.builder.get_object("load_button")
        self.destroy_button = self.builder.get_object("destroy_button")

        #----------------------------TEXT ENTRY WIDGET------------------

        self.entry1 = self.builder.get_object("entry1")
        self.entry2 = self.builder.get_object("entry2")
        self.entry3 = self.builder.get_object("entry3")
        self.entry4 = self.builder.get_object("entry4")
        self.entry5 = self.builder.get_object("entry5")

        #----------------------------TREE VIEW MANAGEMENT----------------------------
        
        self.treeView_DB = Gtk.TreeView()

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.set_hexpand(True)
        self.window_grid.attach(self.scrollable_treelist,0,1,2,1)

        self.scrollable_treelist.add(self.treeView_DB)

        self.model = Gtk.ListStore(int, str, str, str, str, str)

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

        #----------------------------ID COMBO BOX----------------------------

        self.id_model = Gtk.ListStore(int)

        self.id_combo_box = Gtk.ComboBox.new_with_model(self.id_model)
        self.crud_buttons_grid.attach(self.id_combo_box, 1, 1, 1, 1)

        renderer_text = Gtk.CellRendererText()
        self.id_combo_box.pack_start(renderer_text, True)
        self.id_combo_box.add_attribute(renderer_text, "text", 0)
        self.id_combo_box.connect("changed", self.on_id_combo_box_changed)

        #----------------------------WINDOW PREFERENCES----------------------------
        self.window.show_all()

    #----------------------------CRUD BUTTONS(FUNCTIONS CLICKED)----------------------------
    
    def on_add_button_clicked(self,button):
        if self.DB_initializated:
            if self.entry1.get_text() and self.entry2.get_text() and self.entry3.get_text() and self.entry4.get_text() and self.entry5.get_text() :
                self.DB.addRegister(self.entry1.get_text(),self.entry2.get_text(),self.entry3.get_text(),self.entry4.get_text(),self.entry5.get_text())
                print("Register added")
                self.on_update_button_clicked(button)
            else:
                print("Error while adding.")

    def on_delete_button_clicked(self,button):
        if self.treeIter != None:
            self.DB.remove(self.id_model[self.treeIter][0])
            print("Register deleted")
            self.on_update_button_clicked(button)
        else:
            print("Error: no ID register selected")
    
    def on_update_button_clicked(self,button):
        if self.DB_initializated:
            data = self.DB.getRegisters()
            for row in self.model:
                treeIter = self.model.get_iter_first()
                self.model.remove(treeIter)
            for reg in data:
                self.model.append(reg)

            for row in self.id_model:
                treeIter = self.id_model.get_iter_first()
                self.id_model.remove(treeIter)

            ids = self.DB.getIDs()
            for i in ids:
                    self.id_model.append([i])
            print("DB updated")
        else:
            print("Error: Data Base not initializated")      
    
    def on_edit_button_clicked(self,button):
        if self.treeIter != None:
            self.DB.editRegisterWithID(self.id_model[self.treeIter][0],self.entry1.get_text(),self.entry2.get_text(),self.entry3.get_text(),self.entry4.get_text(),self.entry5.get_text())
            print("Register edited")
            self.on_update_button_clicked(button)
        else:
            print("Error: no ID register selected")
    
    def on_load_button_clicked(self, button):
        if not self.DB_initializated:
            self.DB = DBlib.DB_Handler()
            self.DB.openDB(host='localhost', user='antonio', passwd='antonio', db='GUI')
            data = self.DB.getRegisters()
            for reg in data:
                self.model.append(reg)
            self.DB_initializated = True

            ids = self.DB.getIDs()
            for i in ids:
                self.id_model.append([i])

            print("DB loaded")
        else:
            print("Error: DB is already loaded")

    def on_destroy_button_clicked(self, button):
        if self.DB_initializated:
            self.DB.clear()
            print("DB cleared")
        else:
            print("Error: Data Base not initializated")

    def on_id_combo_box_changed(self, combo):
        self.treeIter = combo.get_active_iter()
        if self.treeIter != None:
            reg = self.DB.getRegisterWithID(self.id_model[self.treeIter][0])
            self.entry1.set_text(reg[0][1])
            self.entry2.set_text(reg[0][2])
            self.entry3.set_text(reg[0][3])
            self.entry4.set_text(reg[0][4])
            self.entry5.set_text(reg[0][5])

    def on_about_dialog_response(self, window):
        self.about_dialog.hide()
    def on_about_select(self, window):
        print("AAAAAAAAAAAAAAAAAAAAA")
        self.about_dialog.show()

def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()