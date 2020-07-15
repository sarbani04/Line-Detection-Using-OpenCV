# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:31:08 2019

@author: Asus
"""
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox 
import csv
import os

def Display(file_path):
	
	sroot = Tk()
	sroot.title("CAMERA DETAILS")
	width = 700
	height = 400
	screen_width = sroot.winfo_screenwidth()
	screen_height = sroot.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	sroot.geometry("%dx%d+%d+%d" % (width, height, x, y))
	#sroot.resizable(0, 0)

	TableMargin = Frame(sroot, width=700)
	TableMargin.pack(side=TOP)
	scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
	scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
	tree = ttk.Treeview(TableMargin, columns=("Camera Name", "RTSP Link", "LiveStream"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
	scrollbary.config(command=tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)
	tree.heading('Camera Name', text="Camera Name",anchor=CENTER)
	tree.heading('RTSP Link', text="RTSP Link",anchor=CENTER)
	tree.heading('LiveStream', text="LiveStream", anchor=CENTER )
	tree.column('#0', stretch=NO, minwidth=0, width=0)
	tree.column('#1', stretch=NO, minwidth=0, width=130,anchor=CENTER)
	tree.column('#2', stretch=NO, minwidth=0, width=450,anchor=CENTER)
	tree.column('#3', stretch=NO, minwidth=0, width=120,anchor=CENTER)
	tree.pack()
	
	with open(file_path) as f:
	    reader = csv.DictReader(f, delimiter=',')
	    for row in reader:
	        firstname = row['Name']
	        lastname = row['URL']
	        address = row['LiveStream']
	        tree.insert("", 0, values=(firstname, lastname, address))
	        
	sroot.mainloop()