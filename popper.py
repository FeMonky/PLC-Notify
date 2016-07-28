# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:02:50 2016

@author: avieux
"""
import plcRead
import plcWrite3
import Logger
from tkinter import Tk, Label, Button, messagebox

electric_blue="#7DF9FF"
slate_gray="#6C7B8B"
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Alarm Condition")
    popup.configure(background='#FFE6E6')
    label = Label(popup, text=msg, font=NORM_FONT, fg = '#460303', bg='#FFE6E6')
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Dismiss", bg='red',command=popup.destroy)
    B1.pack()
    if messagebox.askyesno("Acknowledge Alarm?",msg):
        plcWrite3.write_xv()
        Logger.Logit("ACK",msg)
        popup.destroy
    else :
        Logger.Logit("Not ACK",msg)
    popup.mainloop()       