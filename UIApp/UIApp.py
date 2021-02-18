from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

        self.labels = []
        self.entries = []

        self.labelEntryDict = {}

    def init_window(self, self.labels, self.entries):

        self.master.title("App ID Filling Out")
        self.pack(fill=BOTH, expand=1)
        greeting = Label(text="Hello, welcome to filling out App ID: ",
        foreground="black",
        background="white"
        )
        greeting.place(x=10, y= 20)
        # # Create Labels and Entries
        deviceLbl = Label(text="Enter Device: ", fg='white', bg='black')
        deviceEnt = Entry(fg="black", bg='white', width=30)
        appIDLab = Label(text="Enter App ID: ", fg='white', bg='black')
        appID = Entry(fg="black", bg='white', width=30)
        pnLbl = Label(text="Enter Partnumber: ", fg='white', bg='black')
        pnEnt = Entry(fg="black", bg='white', width=30)
        radioLab = Label(text="Enter Radio: ", fg='white', bg='black')
        radio = Entry(fg="black", bg='white', width=30)
        fw = Entry(fg='black', bg='white', width=30)
        fwLab = Label(text="Enter Firmware: ", fg='white', bg='black')
        prevFw = Entry(fg="black", bg='white', width=30)
        prevFwLab = Label(text="Enter Previous Firmware: ", fg='white', bg='black')
        OTACnfg = Entry(fg="black", bg='white', width=30)
        OTACnfg.insert(0,"50.44")
        OTACnfgLab = Label(text="Enter OTAConfig: ", fg='white', bg='black')

        self.labels.append(deviceLbl)
        self.labels.append(appIDLab)
        self.labels.append(pnLbl)
        self.labels.append(radioLab)
        self.labels.append(fwLab)
        self.labels.append(prevFwLab)
        self.labels.append(OTACnfgLab)

        self.entries.append(deviceEnt)
        self.entries.append(appID)
        self.entries.append(pnEnt)
        self.entries.append(radio)
        self.entries.append(fw)
        self.entries.append(prevFw)
        self.entries.append(OTACnfg)

       
        

        for index in range(0,len(labels)):
            self.labelEntryDict[self.labels[index]] = self.entries[index]


        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=10,y=365)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x400")
app = Window(root)

root.mainloop()










# ########################

# def get_entries():
#     entryValues = []
#     for entry in entries:
#         entryValues.append(entry.get())
#         # print(entry.get())

#     return entryValues

# getEntryButton = tk.Button(text='Enter', 
#                         height = 5,
#                         width=10,
#                         command=get_entries)


# for key, item in labelEntryDict.items():
#     key.pack(pady=10,padx=10)
#     item.pack()

# getEntryButton.pack(pady=10,padx=10)




# for entryValue in entryValues:
#     print(entryValue)
# window.mainloop()



# firstStr = "All, Here is the test report for the: "

# header = labels[0] + ' ' + ' App ID'
