from tkinter import *

def writeToFile(entries):
	appIdFile = open("AppIDFile.txt", "w")
	for entry in entries:
		#### Return and dont write to file unless they fill all inputs
		if entry.get() == "":
			print("Failed miss entry!!!!")	
			return 
		### Now we know every entry has been filled 
		else:
			appIdFile.write("- " + entry.get().strip() + "\n")
			
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
		entryOrder = ['device: ', 'radio: ' , 'App ID: ', 'firmware: ', 'previous firmware: ', 'part number: ', 'Ate passnumber: ', 'OTA Config: ']
		# # Create Labels and Entries
		deviceLbl = Label(text=entryOrder[0], fg='black', bg='white')
		deviceEnt = Entry(fg="black", bg='white', width=30)
		appIDLab = Label(text=entryOrder[2], fg='black', bg='white')
		appID = Entry(fg="black", bg='white', width=30)
		pnLbl = Label(text=entryOrder[5], fg='black', bg='white')
		pnEnt = Entry(fg="black", bg='white', width=30)
		radioLab = Label(text=entryOrder[1], fg='black', bg='white')
		radio = Entry(fg="black", bg='white', width=30)
		fw = Entry(fg='black', bg='white', width=30)
		fwLab = Label(text=entryOrder[3], fg='black', bg='white')
		prevFw = Entry(fg="black", bg='white', width=30)
		prevFwLab = Label(text=entryOrder[4], fg='black', bg='white')
		atePassNumberLbl = Label(text=entryOrder[6], fg='black', bg='white')
		atePassNumberEnt = Entry(fg="black", bg='white', width=30)
		OTACnfg = Entry(fg="black", bg='white', width=30)
		OTACnfg.insert(0,"50.44")
		OTACnfgLab = Label(text=entryOrder[7], fg='black', bg='white')
		
		self.labels.append(deviceLbl)
		self.labels.append(radioLab)
		self.labels.append(appIDLab)
		self.labels.append(pnLbl)
		self.labels.append(fwLab)
		self.labels.append(prevFwLab)
		self.labels.append(atePassNumberLbl)
		self.labels.append(OTACnfgLab)
		
		self.entries.append(deviceEnt)
		self.entries.append(radio)
		self.entries.append(appID)
		self.entries.append(pnEnt)
		self.entries.append(fw)
		self.entries.append(prevFw)
		self.entries.append(atePassNumberEnt)
		self.entries.append(OTACnfg)
		
		enterBttn = Button(self, text="Enter ", command=self.myClick)
		enterBttn.pack()
		
		
		# Creates a label entry dictionary where labels are the key and entry are the item
		for index in range(0,len(entryOrder)):
			# self.labelEntryDict[self.labels[index].text] = self.entries[index]
			self.labelEntryDict[self.labels[index].cget('text')] = self.entries[index]
		for index in range(0, len(entryOrder)):
			self.labels[index].pack()
			if entryOrder[index] in self.labelEntryDict.keys():
				self.labelEntryDict[entryOrder[index]].pack()
				# pass
		quitButton = Button(self, text="Quit", command=self.client_exit)
		quitButton.pack()
				

	def myClick(self):
		for key, item in self.labelEntryDict.items():
			print(key + " " + item.get())
		print("********************************\n")
		print("********************************\n")
		writeToFile(self.entries)
			

	def client_exit(self):
		exit()
		
root = Tk()
app = Window(root)

root.mainloop()


