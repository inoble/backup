# Compress.py - by Ian Noble (iannoble.org.uk | iannoble@gmail.com | github.com/inoble)
# Tkinter GUI to select and compress directories and upload them to a webserver.

import os, shutil
import upload
from tkinter import *
from tkinter import filedialog

	
# change location of directory to compress
def select_loc():
	""" Return selected directory location. """
	
	# delete any previous location information in textbox and status text
	entry.delete(0, 'end')
	status_text.config(text='')
	
	location = filedialog.askdirectory()
	
	entry.insert(END, location)

	
# find directory location and compress directory
def backup():
	""" Compress selected directory location and upload. """
	
	location = entry.get()
	
	# if textbox is empty, prompt user to select a directory to compress
	if not location:
	
		status_text.config(text='click ... to select a directory to compress')
	
	# if textbox contains a directory, compress directory
	else:
	
		os.chdir(location)
		
		status_text.config(text='compressing: ' + location)
		
		shutil.make_archive('backup', 'zip', location)
		
		status_text.config(text='uploading...')
		
		upload.upload(location)
		
		status_text.config(text='backup successful')


# initiate Tkinter GUI
master = Tk()
master.geometry('{}x{}'.format(400, 50))
master.title('Backup Directory')

# Tkinter text entry box
entry = Entry(master, width=50)
entry.grid(row = 0, column = 0, columnspan = 5)

# Tkinter button to search for a directory
filedialog_button = Button(master, text="...", command=select_loc)
filedialog_button.grid(row = 0, column = 6, sticky=W)

# Tkinter 'zip' button to compress and upload directory
compress_button = Button(master, text="backup", command=backup)
compress_button.grid(row = 0, column = 7, sticky=W)

# Tkinter status textbox
status_text = Label(master, justify=LEFT)
status_text.grid(row = 1, column = 0)

# end Tkinter GUI
mainloop()