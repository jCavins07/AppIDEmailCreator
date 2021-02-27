from tkinter import *

def writeToFile(entries):
	for entry in entries:
		if entry.get() == "":
			print("Failed miss entry!!!!")	
			return

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		
		self.master = master
		
		self.labels = []
		self.entries = []
		self.labelEntryDict = {}
		
		self.init_window()

		
	def init_window(self):
	
		self.master.title("App ID Filling Out")
		self.pack(fill=BOTH, expand=1)
		greeting = Label(text="Hello, welcome to filling out App ID: ",
		foreground="black",
		background="white"
		)
		greeting.pack()
        # # Create Labels and Entries
		deviceLbl = Label(text="Enter Device: ", fg='black', bg='white')
		deviceEnt = Entry(fg="black", bg='white', width=30)
		appIDLab = Label(text="Enter App ID: ", fg='black', bg='white')
		appID = Entry(fg="black", bg='white', width=30)
		pnLbl = Label(text="Enter Partnumber: ", fg='black', bg='white')
		pnEnt = Entry(fg="black", bg='white', width=30)
		radioLab = Label(text="Enter Radio: ", fg='black', bg='white')
		radio = Entry(fg="black", bg='white', width=30)
		fw = Entry(fg='black', bg='white', width=30)
		fwLab = Label(text="Enter Firmware: ", fg='black', bg='white')
		prevFw = Entry(fg="black", bg='white', width=30)
		prevFwLab = Label(text="Enter Previous Firmware: ", fg='black', bg='white')
		OTACnfg = Entry(fg="black", bg='white', width=30)
		OTACnfg.insert(0,"50.44")
		OTACnfgLab = Label(text="Enter OTAConfig: ", fg='black', bg='white')
		
		self.labels.append(deviceLbl)
		self.labels.append(radioLab)
		self.labels.append(appIDLab)
		self.labels.append(pnLbl)
		self.labels.append(fwLab)
		self.labels.append(prevFwLab)
		self.labels.append(OTACnfgLab)
		
		self.entries.append(deviceEnt)
		self.entries.append(radio)
		self.entries.append(appID)
		self.entries.append(pnEnt)
		self.entries.append(fw)
		self.entries.append(prevFw)
		self.entries.append(OTACnfg)
		
		enterBttn = Button(self, text="Enter ", command=self.myClick)
		enterBttn.pack()
		# Creates a label entry dictionary where labels are the key and entry are the item
		for index in range(0,len(self.labels)):
			# self.labelEntryDict[self.labels[index].text] = self.entries[index]
			self.labelEntryDict[self.labels[index]] = self.entries[index]
		for key, item in self.labelEntryDict.items():
			key.pack()
			item.pack()

		quitButton = Button(self, text="Quit", command=self.client_exit)
		quitButton.pack()
				

	def myClick(self):
		for key, item in self.labelEntryDict.items():
			print(key.cget("text") + " " + item.get())
		print("********************************\n")
		print("********************************\n")
		writeToFile(self.entries)
			

	def client_exit(self):
		exit()
		
root = Tk()
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
