from os.path import exists
from tkinter import Tk, PhotoImage, TOP, BOTTOM, END, LEFT
from tkinter.ttk import Frame, Button, Entry
from tkinter.filedialog import askdirectory

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Replace Images")
        self.geometry("1000x1000")
        self.minsize(500, 500)

        # Top Frame
        self.top_frame = Frame(self, padding=10)
        self.top_frame.pack(side=TOP, fill='x', expand=True)

        # Top Top Frame
        self.top_top_frame = Frame(self.top_frame, padding=10)
        self.top_top_frame.pack(side=TOP)

        # Top Bottom Frame
        self.top_bottom_frame = Frame(self.top_frame, padding=10)
        self.top_bottom_frame.pack(side=BOTTOM, fill='x', expand=True)

        # Bottom Frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill='x', expand=True)

        # Directory Text 
        self.csv_entry = Entry(self.top_top_frame, text='')
        self.csv_entry.pack(fill='x', expand=True)

        # Select Directory Button
        self.select_directory_button = Button(self.top_top_frame, text='Select Directory', command=select_directory)
        self.select_directory_button.pack(anchor='e')

        # Buttons
        self.next_button = Button(self.top_bottom_frame, text="Next", command=next_image)
        self.next_button.pack(side=LEFT)

        self.previous_button = Button(self.top_bottom_frame, text="Previous", command=previous_image)
        self.previous_button.pack(side=LEFT)

        self.replace_button = Button(self.top_bottom_frame, text="replace", command=replace_image)
        self.replace_button.pack(side=LEFT)

        


        def select_directory(self):
            self.directory_path = askdirectory(title='Select Directory')
            if exists(self.output_path):
                self.output_entry.delete(0, END)
                self.output_entry.insert(0, self.output_path)
                
        def next_image(self):
            # Image
            image = 0
            for i in range(image):

                self.image = PhotoImage(image)

        def previous_image(self):
            pass
    
        def replace_image(self):
            pass