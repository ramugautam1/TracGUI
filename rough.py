# try:
#     import tkinter as tk  # python 3
#     from tkinter import font as tkfont  # python 3
# except ImportError:
#     import Tkinter as tk  # python 2
#     import tkFont as tkfont  # python 2
# import tkinter.filedialog as fd
# from segmentation_code import segment_predict, segment_train
#
#
# class SampleApp(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.title('FIAPP')
#         self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
#         # the container is where we'll stack a bunch of frames
#         # on top of each other, then the one we want visible
#         # will be raised above the others
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#         for F in (HomePage, SegmentationPage, TrackingPage, AnalysisPage, TrainOptPage, TestOptPage, PredictOptPage):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame
#
#             # put all of the pages in the same location;
#             # the one on the top of the stacking order
#             # will be the one that is visible.
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.show_frame("HomePage")
#
#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
# # message_0 = tk.Label(text="Welcome to MOSTHyFI", fg = "white", bg="black", width=40, height=5)
# # message_0.pack()
# # segButton = tk.Button(text="Segmentation",width=20, height=3, bg="blue",fg="white")
# # segButton.pack(side=tk.TOP, padx = 100, pady=20)
# # trackButton = tk.Button(text="Tracking",width=20, height=3, bg="navy",fg="white")
# # trackButton.pack(side=tk.TOP, padx = 100, pady=20)
# # anaButton = tk.Button(text="Analysis",width=20, height=3, bg="#CD58F6",fg="white")
# # anaButton.pack(side=tk.TOP, padx = 100, pady=20)
# # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# class HomePage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Welcome to FIAPP", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#
#         button1 = tk.Button(self, text="Segmentation",
#                             command=lambda: controller.show_frame("SegmentationPage"))
#         button2 = tk.Button(self, text="Tracking",
#                             command=lambda: controller.show_frame("TrackingPage"))
#         button3 = tk.Button(self, text="Analysis", command=lambda: controller.show_frame("AnalysisPage"))
#         button1.pack()
#         button2.pack()
#         button3.pack()
#
#
# # =======================================================================================================================
# class SegmentationPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         label = tk.Label(self, text="Segmentation", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button1 = tk.Button(self, text="<- Back", command=lambda: controller.show_frame("HomePage"))
#         button2 = tk.Button(self, text="Train", command=lambda: controller.show_frame("TrainOptPage"))
#         button3 = tk.Button(self, text="Test", command=lambda: controller.show_frame("TestOptPage"))
#         button4 = tk.Button(self, text="Predict", command=lambda: controller.show_frame("PredictOptPage"))
#         button1.pack()
#         button2.pack()
#         button3.pack()
#         button4.pack()
#
#
# # -----------------------------------------------------------------------------------------------------------------------
#
# class TrainOptPage(tk.Frame):
#     gtPath = ''
#     outputPath = ''
#     epochs = 0
#
#     def browseFile(self):
#         try:
#             self.gtPath = fd.askdirectory() + '/'
#         except:
#             self.gtPath = 'default/gt/path/'
#
#     def outputLocation(self):
#         try:
#             self.outputPath = fd.askdirectory() + '/'
#         except:
#             self.outputPath = '/default/output/path/'
#
#     def callTrain(self, epochs):
#         segment_train(epochs, self.gtPath, self.outputPath)
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         label1 = tk.Label(self, text="Segmentation/Train", font=controller.title_font)
#         label1.pack(side="top", fill="x", pady=10)
#
#         button1 = tk.Button(self, text="<- Back", command=lambda: controller.show_frame("SegmentationPage"))
#         button2 = tk.Button(self, text="Select Ground Truth", command=lambda: self.browseFile())
#         button3 = tk.Button(self, text="Select Output Folder", command=lambda: self.outputLocation())
#         numEpochs = tk.IntVar()
#         label2 = tk.Label(self, text="No. of Epochs")
#         entry1 = tk.Entry(self, textvariable=numEpochs)
#         button4 = tk.Button(self, text="check", command=lambda: print(numEpochs.get(), self.gtPath, self.outputPath))
#         button5 = tk.Button(self, text="RUN", background="red", foreground="white",
#                             command=lambda: self.callTrain(numEpochs.get()))
#
#         button1.pack()
#         button2.pack()
#         button3.pack()
#         label2.pack()
#         entry1.pack()
#
#         button4.pack()
#         button5.pack()
#
#
# # -----------------------------------------------------------------------------------------------------------------------
# class TestOptPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Coming Soon!", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="<- Back",
#                            command=lambda: controller.show_frame("SegmentationPage"))
#         button.pack()
#
#
# # -----------------------------------------------------------------------------------------------------------------------
# class PredictOptPage(tk.Frame):
#     imageName = ''
#     outputPath = ''
#     weightsPath = ''
#     startTime = 1
#     endTime = 41
#
#     def browseFile(self):
#         self.imageName = fd.askopenfilename(defaultextension=".nii")
#
#     def outputLocation(self):
#         self.outputPath = fd.askdirectory() + '/'
#
#     def weightLocation(self):
#         self.weightsPath = fd.askdirectory() + '/'
#
#     def getTimes(self, st, et):
#         self.startTime = st
#         self.endTime = et
#
#     def callPredict(self, st, et):
#         self.startTime = st
#         self.endTime = et
#         segment_predict(self.imageName, self.weightsPath, self.outputPath, self.startTime, self.endTime)
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         label = tk.Label(self, text="Segmentation/Predict", font=controller.title_font)
#
#         button1 = tk.Button(self, text="<- Back", command=lambda: controller.show_frame("SegmentationPage"))
#         buttonIm = tk.Button(self, text="Select Image", command=lambda: self.browseFile())
#
#         label2 = tk.Label(self, text="Start Time")
#         startT = tk.IntVar()
#         entry1 = tk.Entry(self, textvariable=startT)
#
#         label3 = tk.Label(self, text="End Time")
#         endT = tk.IntVar()
#         entry2 = tk.Entry(self, textvariable=endT)
#
#         button2 = tk.Button(self, text="Select Weights", command=lambda: self.browseFile())
#         button3 = tk.Button(self, text="Select Output Folder", command=lambda: self.outputLocation())
#         button4 = tk.Button(self, text="Check",
#                             command=lambda: print(startT.get(), endT.get(), self.imageName, self.outputPath,
#                                                   self.weightsPath))
#         button5 = tk.Button(self, text="RUN", background="red", foreground="white",
#                             command=lambda: self.callPredict(startT.get(), endT.get()))
#
#         label.pack(side="top", fill="x", pady=10)
#
#         button1.pack()
#         button2.pack()
#         button3.pack()
#         buttonIm.pack()
#
#         label2.pack()
#         entry1.pack()
#         label3.pack()
#         entry2.pack()
#         button4.pack()
#         button5.pack()
#
#
# # =======================================================================================================================
#
# class TrackingPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Tracking", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="<- Back",
#                            command=lambda: controller.show_frame("HomePage"))
#         button.pack()
#
#
# # =======================================================================================================================
# class AnalysisPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Analysis", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="<- Back>",
#                            command=lambda: controller.show_frame("HomePage"))
#         button.pack()
#
#
# # =======================================================================================================================
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()

from tkinter import *

root = Tk()
root.title('MOSTHyFI - Segmentation, Tracking and Analysis')
img = PhotoImage(file='/home/nirvan/Downloads/ikon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("900x720")

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
app_menu = Menu(my_menu)
seg_menu = Menu(my_menu)
trac_menu = Menu(my_menu)
fam_menu = Menu(my_menu)
ana_menu = Menu(my_menu)

my_menu.add_cascade(label='File', menu=file_menu)
my_menu.add_cascade(label='App', menu=app_menu)
my_menu.add_cascade(label='Segmentation', menu=seg_menu)
my_menu.add_cascade(label='Tracking', menu=trac_menu)
my_menu.add_cascade(label='Family Tree', menu=fam_menu)
my_menu.add_cascade(label='Analysis', menu=ana_menu)

file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Save as')

app_menu.add_command(label='Quit!', command=root.quit)

ana_menu.add_command(label='Cross-Correlation')
ana_menu.add_command(label='Other Analysis')
ana_menu.add_command(label='Analysis III')

# Create Frames
seg_frame = Frame(root, width=900, height=720, bg='#DDDDDD')


# Functions
def seg_command():
    None


root.mainloop()

