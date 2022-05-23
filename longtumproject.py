from cProfile import label
from importlib.resources import contents
from optparse import Option
from secrets import choice
from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from setuptools import Command
from PIL import ImageTk,Image


root = Tk()
root.title("IDONTHAVECPU")
root.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
canvas = Canvas(root, width = 1120, height = 800)
canvas.place(x=0,y=0,relwidth=1,relheight=1)
img = PhotoImage(file=r"E:\work\project\Image\zzanya4.png")
canvas.create_image(0,0,anchor=NW,image=img)
root.geometry("1120x800+200+100")
def pageinfo():
    startwind = Toplevel()
    startwind.title("IDONTHAVECPU")
    startwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
    canvas = Canvas(startwind, width = 1120, height = 800)
    canvas.place(x=0,y=0,relwidth=1,relheight=1)
    img = PhotoImage(file=r"E:\work\project\Image\zzanya3.png")
    canvas.create_image(0,0,anchor=NW,image=img)
    startwind.geometry("1120x800+200+100")
    def listcpu():
        cpuwind = Toplevel()
        cpuwind.title("IDONTHAVECPU")
        cpuwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(cpuwind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        cpuwind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\0.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\1.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\2.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)
        def showcpu3():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\3.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)
        def showcpu4():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\4.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)
        def showcpu5():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\5.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)
        def showcpu6():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\6.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)
        def showcpu7():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\7.png"))
            label2 = Label(cpuwind,image=img2).place(x=150,y=350)

        
        lists0=Button(cpuwind, text="AMD RYZEN 5 3600 3.6 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(cpuwind, text="AMD RYZEN 5 5600X 3.7 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(cpuwind, text="AMD RYZEN 3 3300X 3.8 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        lists3=Button(cpuwind, text="AMD RYZEN 7 5800X 3.8 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu3).pack()
        lists4=Button(cpuwind, text="INTEL CORE I5-10400F 2.9 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu4).pack()
        lists5=Button(cpuwind, text="INTEL CORE I5-10400 2.9 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu5).pack()
        lists6=Button(cpuwind, text="INTEL CORE I3-10100 3.6 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu6).pack()
        lists7=Button(cpuwind, text="INTEL CORE I3-10105F 3.7 GHz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu7).pack()

        exit_cpu=Button(cpuwind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=cpuwind.destroy).place(x=5,y=5)
        cpuwind.mainloop()
    def listmain():
        mainwind = Toplevel()
        mainwind.title("IDONTHAVECPU")
        mainwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(mainwind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        mainwind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\11.png"))
            label2 = Label(mainwind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\22.png"))
            label2 = Label(mainwind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\33.png"))
            label2 = Label(mainwind,image=img2).place(x=150,y=350)
        def showcpu3():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\44.png"))
            label2 = Label(mainwind,image=img2).place(x=150,y=350)
        def showcpu4():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\55.png"))
            label2 = Label(mainwind,image=img2).place(x=150,y=350)
        def showcpu5():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\66.png"))
            label2 = Label(mainwind,image=img2).place(x=150,y=350)

        cpulists0=Button(mainwind, text="AM4 ASROCK B450M STEEL LEGEND",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        cpulists1=Button(mainwind, text="AM4 ASROCK B450 STEEL LEGEND",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        cpulists2=Button(mainwind, text="AM4 ASUS PRIME A320M-K",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        cpulists3=Button(mainwind, text="AM4 ASUS PRIME X570-P/CSM",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu3).pack()
        cpulists4=Button(mainwind, text="AM4 ASUS ROG STRIX X570-F GAMING",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu4).pack()
        cpulists5=Button(mainwind, text="1700 ASUS TUF GAMING Z690-PLUS WIFI D4",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu5).pack()

        exit_main=Button(mainwind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=mainwind.destroy).place(x=5,y=5)
        mainwind.mainloop()
    def listvga():
        vgawind = Toplevel()
        vgawind.title("IDONTHAVECPU")
        vgawind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(vgawind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        vgawind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\111.png"))
            label2 = Label(vgawind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\222.png"))
            label2 = Label(vgawind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\333.png"))
            label2 = Label(vgawind,image=img2).place(x=150,y=350)
        def showcpu3():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\444.png"))
            label2 = Label(vgawind,image=img2).place(x=150,y=350)
        def showcpu4():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\555.png"))
            label2 = Label(vgawind,image=img2).place(x=150,y=350)


        lists0=Button(vgawind, text="MANLI GEFORCE RTX 3070 TI GALLARDO - 8GB GDDR6X",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(vgawind, text="MANLI GEFORCE RTX 3060 TI GALLARDO - 8GB GDDR6",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(vgawind, text="MANLI GEFORCE RTX 3080 TI GALLARDO - 12GB GDDR6X",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        lists3=Button(vgawind, text="POWER COLOR RED DEVIL RX6900XT 16GB GDDR6",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu3).pack()
        lists4=Button(vgawind, text="GIGABYTE GT1030 DDR5 2GB",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu4).pack()

        exit_vga=Button(vgawind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=vgawind.destroy).place(x=5,y=5)
        vgawind.mainloop()
    def listmem():
        memwind = Toplevel()
        memwind.title("IDONTHAVECPU")
        memwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(memwind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        memwind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\1111.png"))
            label2 = Label(memwind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\2222.png"))
            label2 = Label(memwind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\3333.png"))
            label2 = Label(memwind,image=img2).place(x=150,y=350)
        def showcpu3():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\4444.png"))
            label2 = Label(memwind,image=img2).place(x=150,y=350)
        def showcpu4():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\5555.png"))
            label2 = Label(memwind,image=img2).place(x=150,y=350)


        lists0=Button(memwind, text="16GB (8GBx2) DDR4 3200MHz RAM G.SKILL TRIDENT Z RGB",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(memwind, text="16GB (8GBx2) DDR3 1600MHz RAM KINGSTON HyperX FURY",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(memwind, text="16GB (8GBx2) DDR4 2666MHz RAM CORSAIR VENGEANCE LPX",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        lists3=Button(memwind, text="16GB (8GBx2) DDR4 3200MHz RAM G.SKILL TRIDENT Z NEO",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu3).pack()
        lists4=Button(memwind, text="64GB (32GBx2) DDR4 3200MHz RAM ZADAK SHIELD DC RGB",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu4).pack()

        exit_mem=Button(memwind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=memwind.destroy).place(x=5,y=5)
        memwind.mainloop()
    def listhhd():
        hhdwind = Toplevel()
        hhdwind.title("IDONTHAVECPU")
        hhdwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(hhdwind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        hhdwind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\11111.png"))
            label2 = Label(hhdwind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\22222.png"))
            label2 = Label(hhdwind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\33333.png"))
            label2 = Label(hhdwind,image=img2).place(x=150,y=350)

        lists0=Button(hhdwind, text="1 TB 3.5 HDD WD BLUE - 7200RPM SATA3",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(hhdwind, text="1 TB 3.5 HDD (SEAGATE BARRACUDA - 7200RPM SATA3",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(hhdwind, text="2 TB 3.5 HDD WD BLACK - 7200RPM SATA3",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()


        exit_hhd=Button(hhdwind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=hhdwind.destroy).place(x=5,y=5)
        hhdwind.mainloop()
    def listm2():
        m2wind = Toplevel()
        m2wind.title("IDONTHAVECPU")
        m2wind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(m2wind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        m2wind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\111111.png"))
            label2 = Label(m2wind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\222222.png"))
            label2 = Label(m2wind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\333333.png"))
            label2 = Label(m2wind,image=img2).place(x=150,y=350)
        
        lists0=Button(m2wind, text="250GB SSD SAMSUNG 970 EVO PLUS PCIe/NVMe M.2 2280",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(m2wind, text="500GB SSD WD BLUE SATA M.2 2280",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(m2wind, text="1TB SSD SAMSUNG 970 PRO PCIe/NVMe M.2 2280",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        
        exit_m2=Button(m2wind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=m2wind.destroy).place(x=5,y=5)
        m2wind.mainloop()
    def listpws():
        pwswind = Toplevel()
        pwswind.title("IDONTHAVECPU")
        pwswind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(pwswind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        pwswind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\a.png"))
            label2 = Label(pwswind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\b.png"))
            label2 = Label(pwswind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\c.png"))
            label2 = Label(pwswind,image=img2).place(x=150,y=350)
        def showcpu3():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\d.png"))
            label2 = Label(pwswind,image=img2).place(x=150,y=350)


        lists0=Button(pwswind, text="POWER SUPPLY COUGAR STX550 - 550W 80 PLUS WHITE",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(pwswind, text="POWER SUPPLY THERMALTAKE TR2 S 550W 80 PLUS",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(pwswind, text="POWER SUPPLY ASUS ROG STRIX 1000G - 1000W 80PLUS GOLD",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        lists3=Button(pwswind, text="POWER SUPPLY ANTEC ATOM B650 - 650W 80PLUS BRONZE",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu3).pack()
        
        exit_pws=Button(pwswind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=pwswind.destroy).place(x=5,y=5)
        pwswind.mainloop()
    def listlq():
        lqwind = Toplevel()
        lqwind.title("IDONTHAVECPU")
        lqwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(lqwind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        lqwind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\E (1).png"))
            label2 = Label(lqwind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\E (2).png"))
            label2 = Label(lqwind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\E (3).png"))
            label2 = Label(lqwind,image=img2).place(x=150,y=350)
        


        lists0=Button(lqwind, text="CPU LIQUID COOLER NZXT KRAKEN X53",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(lqwind, text="CPU LIQUID COOLER ASUS ROG STRIX LC 240(WHITE EDITION)",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(lqwind, text="CPU LIQUID COOLER ASUS ROG RYUJIN II 360",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        
        exit_lq=Button(lqwind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=lqwind.destroy).place(x=5,y=5)
        lqwind.mainloop()
    def listmnt():
        mntwind = Toplevel()
        mntwind.title("IDONTHAVECPU")
        mntwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(mntwind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        mntwind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\Q (1).png"))
            label2 = Label(mntwind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\Q (2).png"))
            label2 = Label(mntwind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\Q (3).png"))
            label2 = Label(mntwind,image=img2).place(x=150,y=350)
        def showcpu3():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\Q (4).png"))
            label2 = Label(mntwind,image=img2).place(x=150,y=350)
        def showcpu4():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\Q (5).png"))
            label2 = Label(mntwind,image=img2).place(x=150,y=350)
        def showcpu5():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\Q (6).png"))
            label2 = Label(mntwind,image=img2).place(x=150,y=350)

        cpulists0=Button(mntwind, text="MONITOR ASUS TUF GAMING VG27AQ 27IPS 2K 165Hz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        cpulists1=Button(mntwind, text="MONITOR ASUS VP249QGR 23.8IPS SPEAKER 144Hz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        cpulists2=Button(mntwind, text="MONITOR BENQ ZOWIE XL2546 24.5TN 240Hz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        cpulists3=Button(mntwind, text="MONITOR ACER VG240YBMIIX 23.8IPS 75Hz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu3).pack()
        cpulists4=Button(mntwind, text="MONITOR LG 29WK600-W 29IPS 75Hz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu4).pack()
        cpulists5=Button(mntwind, text="MONITOR DELL U2720Q 27IPS 4K 60Hz",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu5).pack()

        exit_mnt=Button(mntwind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=mntwind.destroy).place(x=5,y=5)
        mntwind.mainloop()
    def listcase():
        casewind = Toplevel()
        casewind.title("IDONTHAVECPU")
        casewind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        canvas = Canvas(casewind, width = 1120, height = 800)
        canvas.place(x=0,y=0,relwidth=1,relheight=1)
        img = PhotoImage(file=r"E:\work\project\Image\zzanya1.png")
        canvas.create_image(0,0,anchor=NW,image=img)
        casewind.geometry("1120x800+200+100")
        def showcpu0():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\R (1).png"))
            label2 = Label(casewind,image=img2).place(x=150,y=350)
        def showcpu1():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\R (2).png"))
            label2 = Label(casewind,image=img2).place(x=150,y=350)
        def showcpu2():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\R (3).png"))
            label2 = Label(casewind,image=img2).place(x=150,y=350)
        def showcpu3():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\R (4).png"))
            label2 = Label(casewind,image=img2).place(x=150,y=350)
        def showcpu4():
            global img2
            global label2
            img2 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\R (5).png"))
            label2 = Label(casewind,image=img2).place(x=150,y=350)


        lists0=Button(casewind, text="CASE CORSAIR OBSIDIAN 1000D",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu0).pack()
        lists1=Button(casewind, text="CASE COOLER MASTER NR200P MAX",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu1).pack()
        lists2=Button(casewind, text="CASE COUGAR CONQUER2",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu2).pack()
        lists3=Button(casewind, text="CASE AEROCOOL TALON(RGB)(ATX)",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu3).pack()
        lists4=Button(casewind, text="CASE MONTECH X2 MESH(WHITE)",bg='light salmon',font =('Bahnschrift Condensed',15),width=70,command=showcpu4).pack()

        exit_case=Button(casewind, text="Back",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=casewind.destroy).place(x=5,y=5)
        casewind.mainloop()
    def req():
        global reqwind
        global req2
        global inputreq
        reqwind = Toplevel()
        reqwind.title("IDONTHAVECPU")
        reqwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        reqwind.geometry("220x100+500+300")
        inputreq = StringVar()
        inputreq = Entry(reqwind,text="",width=25)
        inputreq.place(x=35,y=40)
        req_bt = Button(reqwind, text="Request",bg='light salmon',font =('Bahnschrift Condensed',9),width=20,command=lambda:reqq()).place(x=55,y=65)
        lblqu=Label(reqwind,font=('Bahnschrift Condensed',10),text="request products here").place(x=60,y=10)
        def reqq():
            messagebox.showinfo("REQ","การ Req สำเร็จ")
            conn = sqlite3.connect(r"E:\work\project\rstockdatabase.db")
            c=conn.cursor()
            req2 = inputreq.get()
            c.execute("INSERT INTO reqdatacustumer(REQ)VALUES(?)",(req2,))
            conn.commit()
            reqwind.resizable(False, False)


    cpuinfo=Button(startwind, text="CPU",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listcpu).place(x=475,y=210)
    cpuinfo=Button(startwind, text="Mainboard",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listmain).place(x=475,y=260)
    cpuinfo=Button(startwind, text="VGA gard",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listvga).place(x=475,y=310)
    cpuinfo=Button(startwind, text="Memory",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listmem).place(x=475,y=360)
    cpuinfo=Button(startwind, text="Harddisk",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listhhd).place(x=475,y=410)
    cpuinfo=Button(startwind, text="SSD M.2",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listm2).place(x=475,y=460)
    cpuinfo=Button(startwind, text="Power Supply",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listpws).place(x=475,y=510)
    cpuinfo=Button(startwind, text="CPU LIQUID",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listlq).place(x=475,y=560)
    cpuinfo=Button(startwind, text="Monitor",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listmnt).place(x=475,y=610)
    cpuinfo=Button(startwind, text="Case",bg='light salmon',font =('Bahnschrift Condensed',15),width=20,command=listcase).place(x=475,y=660)
    reqinfo=Button(startwind, text="Request",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=req).place(x=10,y=750)
    lblq=Label(startwind,font=('Bahnschrift Condensed',10),text="You can request products here.").place(x=10,y=720)
    exit_startwind=Button(startwind, text="Quit",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=startwind.destroy).place(x=965,y=750)
    startwind.mainloop()

def pagecal():
    calculater = Toplevel()
    calculater.title("IDONTHAVECPU")
    calculater.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
    canvas = Canvas(calculater, width = 1120, height = 800)
    canvas.place(x=0,y=0,relwidth=1,relheight=1)
    img = PhotoImage(file=r"E:\work\project\Image\zzanya4.png")
    canvas.create_image(0,0,anchor=NW,image=img)
    calculater.geometry("1120x800+200+100")
    def gonext():
        global buyiwind
        buyiwind = Toplevel(calculater)
        buyiwind.title("IDONTHAVECPU")
        buyiwind.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        bg = PhotoImage(file =r"E:\work\project\Image\zzanya5.png")
        label1 = Label( buyiwind, image = bg)
        label1.place(x = 0, y = 0)
        buyiwind.geometry("1120x800+200+100")
        #pay text
        lbl0=Label(buyiwind,font=('Bahnschrift Condensed',9),text="เมื่อจ่ายเงินเสร็จเรียบร้อย").place(x=435,y=485)
        lbl1=Label(buyiwind,font=('Bahnschrift Condensed',9),text="กรุณาส่งหลักฐานทางไลน์ พร้อมระบุชื่อผู้รับสินค้า").place(x=625,y=545)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',9),text="Press when u have paid").place(x=850,y=715)
        #name
        Label(buyiwind,font=("Bahnschrift Condensed",25),text="Address ツ").pack()
        lbl=Label(buyiwind,font=('Bahnschrift Condensed',16),text="Name-Surname : ").place(x=300,y=70)
        lbl=Label(buyiwind,font=('Bahnschrift Condensed',9),text="(ex.นายกรณ์ดนัย พันธุ์ฤทธิ์)").place(x=610,y=78)
        inputnameEntry=Entry(buyiwind,text="")
        inputnameEntry.place(x=480,y=80)
        #input_data_rank
        lbl2=Label(buyiwind,font=('Bahnschrift Condensed',16),text="Your Address : ").place(x=300,y=120)
        lbl2=Label(buyiwind,font=('Bahnschrift Condensed',9),text="(ex. 11 หมู่ 12 ต.อีกา อ.หนองกึ่ม จ.ขอนแก่น 40000)").place(x=610,y=128)
        inputadressEntry=Entry(buyiwind,text="")
        inputadressEntry.place(x=480,y=130)
        #input_contact
        lbl3=Label(buyiwind,font=('Bahnschrift Condensed',16),text="Tel.Number : ").place(x=300,y=170)
        lbl3=Label(buyiwind,font=('Bahnschrift Condensed',9),text="(ex.094397xxxx)").place(x=610,y=178)
        def phone(S):
            if S.isdigit():
                return True
            buyiwind.bell()
            return False
        vcmd = (buyiwind.register(phone), '%S')
        inputtelEntry=Entry(buyiwind,text="", validate='key', vcmd=vcmd)
        inputtelEntry.place(x=480,y=178)
        #infocus
        Label(buyiwind,font=("Bahnschrift Condensed",25),text="Information ツ").place(x=480,y=230)
        #gmail
        lbl4=Label(buyiwind,font=('Bahnschrift Condensed',16),text="Gmail : ").place(x=300,y=280)
        lbl4=Label(buyiwind,font=('Bahnschrift Condensed',9),text="(ex.aekkie@gmail.com)").place(x=610,y=288)
        inputgmailEntry=Entry(buyiwind,text="")
        inputgmailEntry.place(x=480,y=290)
        #fb
        lbl5=Label(buyiwind,font=('Bahnschrift Condensed',16),text="Facebook : ").place(x=300,y=330)
        lbl5=Label(buyiwind,font=('Bahnschrift Condensed',9),text="(Bank korndanai)").place(x=610,y=338)
        inputfbEntry=Entry(buyiwind,text="")
        inputfbEntry.place(x=480,y=340)
        #bill
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_cpu.get()).place(x=10,y=500)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_mainboard.get()).place(x=10,y=525)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_vga.get()).place(x=10,y=550)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_memory.get()).place(x=10,y=575)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_hhd.get()).place(x=10,y=600)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_m2.get()).place(x=10,y=625)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_pws.get()).place(x=10,y=650)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_cpulq.get()).place(x=10,y=675)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_case.get()).place(x=10,y=700)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',11),text=cbo_mnt.get()).place(x=10,y=725)
        mylabel = Label(buyiwind, font=('Bahnschrift Condensed',14),text=f"price : {sum} Bath").place(x=10,y=750)
        #แก้ตรงใส่เบอร์ ทรศ
        
        btn2 = Button(buyiwind, text="Accept",bg='orange',font=('Bahnschrift Condensed',15),width=15,command =lambda:adddata())
        btn2.place(x=965,y=705)
        exit_buy=Button(buyiwind, text="Quit",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=buyiwind.destroy).place(x=965,y=750)

        def adddata():
            #หน้าต่างยืนยันสำเร็จ เพิ่มตรง adddata 
            global newgm
            global newfb
            newgm = inputgmailEntry.get()
            newfb = inputfbEntry.get()
            messagebox.showinfo("การสั่งซื้อสำเร็จ","thank you for support")
            conn = sqlite3.connect(r"E:\work\project\rstockdatabase.db")
            c=conn.cursor()
            newnamelast=inputnameEntry.get()
            newadress = inputadressEntry.get()
            newtel = inputtelEntry.get()
            
            c.execute("INSERT INTO datacustomer(namelast,adress,tel,GM,FB) VALUES (?,?,?,?,?)",(newnamelast,newadress,newtel,newgm,newfb))
            conn.commit()
        
            def adddata2():
                
                conn = sqlite3.connect(r"E:\work\project\rstockdatabase.db")
                c=conn.cursor()
                newgm = inputgmailEntry.get()
                newfb = inputfbEntry.get()
                c.execute("INSERT INTO itemcustumer(CPU,MNB,VGA,RAM,HHD,M2,PWS,CPULQ,CS,MNT,GM,FB) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(cbo_cpu.get(),cbo_mainboard.get(),cbo_vga.get(),cbo_memory.get(),cbo_hhd.get(),cbo_m2.get(),cbo_pws.get(),cbo_cpulq.get(),cbo_case.get(),cbo_mnt.get(),newgm,newfb,))
                conn.commit() 
                calculater.resizable(False, False)
            adddata2()
            calculater.destroy()
            buyiwind.destroy()
            discal.destroy()
        buyiwind.mainloop()

    def selected():
        #คำณวนราคา
        conn=sqlite3.connect(r"E:\work\project\rstockdatabase.db")
        c=conn.cursor()
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_cpu.get(),))
        cpuit = c.fetchone()
        cpuit2 = cpuit[0]
        print(cpuit2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_mainboard.get(),))
        mb = c.fetchone()
        mb2 = mb[0]
        print(mb2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_vga.get(),))
        vga = c.fetchone()
        vga2 = vga[0]
        print(vga2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_memory.get(),))
        mm = c.fetchone()
        mm2 = mm[0]
        print(mm2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_hhd.get(),))
        hhd = c.fetchone()
        hhd2 = hhd[0]
        print(hhd2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_m2.get(),))
        m2 = c.fetchone()
        m22 = m2[0]
        print(m22)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_pws.get(),))
        pws = c.fetchone()
        pws2 = pws[0]
        print(pws2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_cpulq.get(),))
        cpulq = c.fetchone()
        cpulq2 = cpulq[0]
        print(cpulq2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_case.get(),))
        case = c.fetchone()
        case2 = case[0]
        print(case2)
        c.execute('SELECT PRICE FROM stockitem WHERE ITEM = ?',(cbo_mnt.get(),))
        mnt = c.fetchone()
        mnt2 = mnt[0]
        print(mnt2)
        conn.commit()
        global sum
        sum = int(cpuit2) + int(mb2) + int(vga2) + int(mm2) + int(hhd2) + int(m22) + int(pws2) + int(case2) + int(mnt2) + int(cpulq2)
        #แสดงผล
        global discal
    
        discal = Toplevel()
        discal.title("IDONTHAVECPU")
        discal.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
        bg = PhotoImage(file =r"E:\work\project\Image\zzanya6.png")
        label1 = Label( discal, image = bg)
        label1.place(x = 0, y = 0)
        discal.geometry("1120x800+200+100")
        mylabel = Label(discal, font=('Bahnschrift Condensed',21),text="Your Computer ツ ").place(x=250,y=200)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_cpu.get()).place(x=250,y=250)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_mainboard.get()).place(x=250,y=290)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_vga.get()).place(x=250,y=330)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_memory.get()).place(x=250,y=370)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_hhd.get()).place(x=250,y=410)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_m2.get()).place(x=250,y=450)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_pws.get()).place(x=250,y=490)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_cpulq.get()).place(x=250,y=530)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_case.get()).place(x=250,y=570)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=cbo_mnt.get()).place(x=250,y=610)
        mylabel = Label(discal, font=('Bahnschrift Condensed',10),text="If you want to order click here").place(x=825,y=715)
        mylabel = Label(discal, font=('Bahnschrift Condensed',16),text=f"price : {sum} Bath").place(x=250,y=660)
        exit_discal=Button(discal, text="Quit",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=discal.destroy).place(x=965,y=750)
        buy_bt=Button(discal, text="Buy",bg='orange',font =('Bahnschrift Condensed',15),width=15,command=gonext).place(x=965,y=705)
        discal.mainloop()
    #list สินค้า
    CPU_list = ['CPU (None)'
    ,'AMD RYZEN 5 3600 3.6 GHz : 7390 Bath ' 
    ,'AMD RYZEN 5 5600X 3.7 GHz : 9790 Bath'
    ,'AMD RYZEN 3 3300X 3.8 GHz : 4490 Bath'
    ,'AMD RYZEN 7 5800X 3.8 GHz : 13700 Bath'
    ,'INTEL CORE I5-10400F 2.9 GHz : 5050 Bath'
    ,'INTEL CORE I5-10400 2.9 GHz : 5750 Bath'
    ,'INTEL CORE I3-10100 3.6 GHz : 4090 Bath'
    ,'INTEL CORE I3-10105F 3.7 GHz : 3190 Bath'
    ]

    Mainboard_list = ['Mainboard (None)'
    ,'AM4 ASROCK B450M STEEL LEGEND : 2990 Bath'
    ,'AM4 ASROCK B450 STEEL LEGEND : 3690 Bath'
    ,'AM4 ASUS PRIME A320M-K : 1490 Bath'
    ,'AM4 ASUS PRIME X570-P/CSM : 3590 Bath'
    ,'AM4 ASUS ROG STRIX X570-F GAMING : 8390 Bath'
    ]

    INTEL_list= ['1700 ASUS TUF GAMING Z690-PLUS WIFI D4 : 10500 Bath']

    VGA_list = ['VGA gard (None)'
    ,'MANLI GEFORCE RTX 3070 TI GALLARDO - 8GB GDDR6X : 38400 Bath'
    ,'MANLI GEFORCE RTX 3060 TI GALLARDO - 8GB GDDR6 : 27500 Bath'
    ,'MANLI GEFORCE RTX 3080 TI GALLARDO - 12GB GDDR6X : 66900 Bath'
    ,'POWER COLOR RED DEVIL RX6900XT 16GB GDDR6 : 56900 Bath'
    ,'GIGABYTE GT1030 DDR5 2GB : 3650 Bath'
    ]

    Memory_list = ['Memory (None)'
    ,'16GB (8GBx2) DDR4 3200MHz RAM G.SKILL TRIDENT Z RGB : 3990 Bath'
    ,'16GB (8GBx2) DDR3 1600MHz RAM KINGSTON HyperX FURY : 4490 Bath'
    ,'16GB (8GBx2) DDR4 2666MHz RAM CORSAIR VENGEANCE LPX : 2840 Bath'
    ,'16GB (8GBx2) DDR4 3200MHz RAM G.SKILL TRIDENT Z NEO : 4290 Bath'
    ,'64GB (32GBx2) DDR4 3200MHz RAM ZADAK SHIELD DC RGB : 33990 Bath'
    ]

    hhd_list = ['Harddisk (None)'
    ,'1 TB 3.5" HDD WD BLUE - 7200RPM SATA3 : 980 Bath'
    ,'1 TB 3.5" HDD (SEAGATE BARRACUDA - 7200RPM SATA3 : 960 Bath'
    ,'2 TB 3.5" HDD WD BLACK - 7200RPM SATA3 : 4290 Bath'
    ]

    m2_list = ['SSD M.2 (None)'
    ,'250GB SSD SAMSUNG 970 EVO PLUS PCIe/NVMe M.2 2280 : 1990 Bath'
    ,'500GB SSD WD BLUE SATA M.2 2280 : 2290 Bath'
    ,'1TB SSD SAMSUNG 970 PRO PCIe/NVMe M.2 2280 : 17900 Bath'
    ]

    pws_list = ['Power Supply (None)'
    ,'POWER SUPPLY COUGAR STX550 - 550W 80 PLUS WHITE : 1590 Bath'
    ,'POWER SUPPLY THERMALTAKE TR2 S 550W 80 PLUS : 1590 Bath'
    ,'POWER SUPPLY ASUS ROG STRIX 1000G - 1000W 80PLUS GOLD : 7090 Bath'
    ,'POWER SUPPLY ANTEC ATOM B650 - 650W 80PLUS BRONZE : 1790 Bath'
    ]

    cpulq_list = ['CPU LIQUID (None)'
    ,'CPU LIQUID COOLER NZXT KRAKEN X53 : 5290 Bath'
    ,'CPU LIQUID COOLER ASUS ROG STRIX LC 240(WHITE EDITION) : 6990 Bath'
    ,'CPU LIQUID COOLER ASUS ROG RYUJIN II 360 : 12500 Bath'
    ]

    mnt_list = ['Monitor (None)'
    ,'MONITOR ASUS TUF GAMING VG27AQ 27"IPS 2K 165Hz : 14900 Bath'
    ,'MONITOR ASUS VP249QGR 23.8"IPS SPEAKER 144Hz : 5900 Bath'
    ,'MONITOR BENQ ZOWIE XL2546 24.5"TN 240Hz : 14500 Bath'
    ,'MONITOR ACER VG240YBMIIX 23.8"IPS 75Hz : 4850 Bath'
    ,'MONITOR LG 29WK600-W 29"IPS 75Hz : 7500 Bath'
    ,'MONITOR DELL U2720Q 27"IPS 4K 60Hz : 21900 Bath'
    ]

    case_list = ['Case (None)'
    ,'CASE CORSAIR OBSIDIAN 1000D : 17890 Bath'
    ,'CASE COOLER MASTER NR200P MAX : 13900 Bath'
    ,'CASE COUGAR CONQUER2 : 10900 Bath'
    ,'CASE AEROCOOL TALON(RGB)(ATX) : 1190 Bath'
    ,'CASE MONTECH X2 MESH(WHITE) : 1250 bath'
    ]

    def comboclick(event):
                cpudata=cbo_cpu.get()
                mndata=cbo_mainboard.get()
                vgadata=cbo_vga.get()
                memorydata=cbo_memory.get()
                hhddata=cbo_hhd.get()
                m2data=cbo_m2.get()
                pwsdata=cbo_pws.get()
                cpulqdata=cbo_cpulq.get()
                csdata=cbo_case.get()
                mntdata=cbo_mnt.get()

    #CPU
    cbo_cpu = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = CPU_list ,width = 80,state ="readonly")
    cbo_cpu.current(0)
    cbo_cpu.bind("<<ComboboxSelectted>>",comboclick)
    cbo_cpu.place(x=148,y=170)

        #Mainboard
    cbo_mainboard = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = Mainboard_list ,width = 80,state ="readonly")
    cbo_mainboard.current(0)
    cbo_mainboard.bind("<<ComboboxSelectted>>",comboclick)
    cbo_mainboard.place(x=148,y=210)

        #VGA
    cbo_vga = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = VGA_list,width = 80,state ="readonly")
    cbo_vga.current(0)
    cbo_vga.bind("<<ComboboxSelectted>>",comboclick)
    cbo_vga.place(x=148,y=250)

        #Memory
    cbo_memory = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = Memory_list,width = 80,state ="readonly")
    cbo_memory.current(0)
    cbo_memory.bind("<<ComboboxSelectted>>",comboclick)
    cbo_memory.place(x=148,y=290)

        #HHD
    cbo_hhd = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = hhd_list,width = 80,state ="readonly")
    cbo_hhd.current(0)
    cbo_hhd.bind("<<ComboboxSelectted>>",comboclick)
    cbo_hhd.place(x=148,y=330)

        #M2
    cbo_m2 = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = m2_list,width = 80,state ="readonly")
    cbo_m2.current(0)
    cbo_m2.bind("<<ComboboxSelectted>>",comboclick)
    cbo_m2.place(x=148,y=370)

        #PWS
    cbo_pws = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = pws_list,width = 80,state ="readonly")
    cbo_pws.current(0)
    cbo_pws.bind("<<ComboboxSelectted>>",comboclick)
    cbo_pws.place(x=148,y=410)

        #CQULQ
    cbo_cpulq = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = cpulq_list,width = 80,state ="readonly")
    cbo_cpulq.current(0)
    cbo_cpulq.bind("<<ComboboxSelectted>>",comboclick)
    cbo_cpulq.place(x=148,y=450)

        #Case
    cbo_case = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = case_list,width = 80,state ="readonly")
    cbo_case.current(0)
    cbo_case.bind("<<ComboboxSelectted>>",comboclick)
    cbo_case.place(x=148,y=490)

        #Monitor
    cbo_mnt = ttk.Combobox(calculater, font=('Bahnschrift Condensed',17),values = mnt_list,width = 80,state ="readonly")
    cbo_mnt.current(0)
    cbo_mnt.bind("<<ComboboxSelectted>>",comboclick)
    cbo_mnt.place(x=148,y=530)

    def retrieve():
        if cbo_cpu.get() == "INTEL CORE I5-10400F 2.9 GHz : 5050 Bath":
            cbo_mainboard["values"] = (INTEL_list)
        elif cbo_cpu.get() == "INTEL CORE I5-10400 2.9 GHz : 5750 Bath":
            cbo_mainboard["values"] = (INTEL_list)
        elif cbo_cpu.get() == "INTEL CORE I3-10100 3.6 GHz : 4090 Bath":
            cbo_mainboard["values"] = (INTEL_list)
        elif cbo_cpu.get() == "INTEL CORE I3-10105F 3.7 GHz : 3190 Bath":
            cbo_mainboard["values"] = (INTEL_list)
        else:
            cbo_mainboard["values"] = (Mainboard_list)

    cur = Button(calculater, text="/",bg='orange',font =('Bahnschrift Condensed',8),width=5,command=retrieve).place(x=985,y=175)
    
    def clear_cbo():     
        cbo_cpu.set('CPU (None)') 
        cbo_case.set('Case (None)')     
        cbo_cpulq.set('CPU LIQUID (None)')     
        cbo_hhd.set('Harddisk (None)')     
        cbo_m2.set('SSD M.2 (None)')     
        cbo_mainboard.set('Mainboard (None)')     
        cbo_memory.set('Memory (None)')     
        cbo_pws.set('Power Supply (None)')     
        cbo_vga.set('VGA gard (None)')     
        cbo_mnt.set('Monitor (None)')       
    
    cal_bt=Button(calculater, text="Calculate",bg='light salmon',font=('Bahnschrift Condensed',15),width=20,command=selected).place(x=475,y=580)
    clear_bt=Button(calculater, text="Clear",bg='light salmon',font=('Bahnschrift Condensed',15),width=20,command=clear_cbo).place(x=475,y=630)
    exit_discal=Button(calculater, text="Quit",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=calculater.destroy).place(x=965,y=750)
    calculater.mainloop()

def pagehow():
    how = Toplevel()
    how.title("IDONTHAVECPU")
    how.iconbitmap(r'E:\work\project\AnyConv.com__Idonthavecpu (2).ico')
    bg = PhotoImage(file =r"E:\work\project\Image\zzhow4.png")
    label1 = Label(how, image = bg)
    label1.place(x = 0, y = 0)
    how.geometry("1120x800+200+100")
    def howinfo():
        global img5
        global label5
        img5 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\zzhow1.png"))
        label5 = Label(how,image=img5).place(x=160,y=18)
    def howcal():
        global img4
        global label4
        img4 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\zzhow2.png"))
        label4 = Label(how,image=img4).place(x=160,y=18)
    def howbuy():
        global img3
        global label3
        img3 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\zzhow3.png"))
        label3 = Label(how,image=img3).place(x=160,y=18)
    def howstep():
        global img6
        global label6
        img6 = ImageTk.PhotoImage(Image.open(r"E:\work\project\Image\zzzzblack.png"))
        label6 = Label(how,image=img6).place(x=160,y=18)
    infoo = Button(how, text="What's Info",bg='orange',font=('Bahnschrift Condensed',15),width=15,command=howinfo).place(x=15,y=10)
    call = Button(how, text="What's cal",bg='orange',font=('Bahnschrift Condensed',15),width=15,command=howcal).place(x=15,y=55)
    buys = Button(how, text="How to buy",bg='orange',font=('Bahnschrift Condensed',15),width=15,command=howbuy).place(x=15,y=100)
    stepz = Button(how, text="Step by Step",bg='orange',font=('Bahnschrift Condensed',15),width=15,command=howstep).place(x=15,y=145)
    exit_buy=Button(how, text="Quit",bg='light salmon',font =('Bahnschrift Condensed',15),width=15,command=how.destroy).place(x=965,y=750)
    how.mainloop()

how_bt=Button(root, text="How to use",bg='orange',font =('Bahnschrift Condensed',15),width=20,command=pagehow).place(x=475,y=250)
info_bt=Button(root, text="Information",bg='orange',font =('Bahnschrift Condensed',15),width=20,command= pageinfo).place(x=475,y=300)
start_bt=Button(root, text="Calculator",bg='orange',font =('Bahnschrift Condensed',15),width=20,command= pagecal).place(x=475,y=350)
exit_bt=Button(root, text="Quit",bg='orange',font =('Bahnschrift Condensed',15),width=20,command=root.destroy).place(x=475,y=400)

root.mainloop() 