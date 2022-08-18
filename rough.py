# import tkinter as tk
# # from tkinter import *
# # import tkinter.filedialog as fd
# import os
#
# window = tk.Tk()
# # fn=''
# # def browseFile():
# #     fname = fd.askopenfilename(defaultextension=".nii")
# #     fn = fname
# #
# # def printFilename():
# #     print(fn)
# #
# # button1 = tkinter.Button(master=root, text='Select 5D image', width=20, command = lambda:browseFile())
# # button1.pack(side=tkinter.TOP, padx = 100, pady=20)
# #
# # button2 = tkinter.Button(master=root, text='Print File Name', width=20, command = lambda:printFilename())
# # button2.pack(side=tkinter.BOTTOM, padx = 100, pady=20)
#
#
#
# # currdir = os.getcwd()
# # tempdir = fd.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
# # if len(tempdir) > 0:
# #     print("You chose %s" % tempdir)
#
# greeting = tk.Label(text = "Welcome to MOSTHyFI", foreground="white", background="red")
# greeting.pack()
#
# window.mainloop()
#
#
# # window = tk.Tk()
# # message_0 = tk.Label(text="Welcome to MOSTHyFI", fg = "white", bg="black", width=40, height=5)
# # message_0.pack()
# # segButton = tk.Button(text="Segmentation",width=20, height=3, bg="blue",fg="white")
# # segButton.pack(side=tk.TOP, padx = 100, pady=20)
# # trackButton = tk.Button(text="Tracking",width=20, height=3, bg="navy",fg="white")
# # trackButton.pack(side=tk.TOP, padx = 100, pady=20)
# # anaButton = tk.Button(text="Analysis",width=20, height=3, bg="#CD58F6",fg="white")
# # anaButton.pack(side=tk.TOP, padx = 100, pady=20)
# # window.mainloop()


def rof(str1,str2,int1,int2):
    print([str1,str2,int1,int2])