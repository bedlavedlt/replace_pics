from os.path import exists, abspath
from tkinter import RIGHT, Tk, PhotoImage, TOP, BOTTOM, END, LEFT, Button
from tkinter.ttk import Frame, Entry, Style
from tkinter.filedialog import askdirectory
from turtle import bgcolor
from PIL import Image, ImageTk


class Application(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Replace Images")
        self.geometry("")
        self.minsize(500, 100)
        self['bg'] = "#404040"

        self.skull = Image.open(abspath("sku11.png"))
        self.skull = ImageTk.PhotoImage(self.skull.resize((20, 22), resample=Image.ANTIALIAS))
        self.right_arrow = Image.open(abspath("right_arrow_transparent.png"))
        self.right_arrow = ImageTk.PhotoImage(self.right_arrow)
        self.left_arrow = Image.open(abspath("left_arrow_transparent.png"))
        self.left_arrow = ImageTk.PhotoImage(self.left_arrow)
        
        
        # Top Frame
        self.top_frame = Frame(self, padding=10)
        self.top_frame.pack(side=TOP, fill='x', expand=True, anchor='n')
       

        # Top Top Frame
        self.top_top_frame = Frame(self.top_frame, padding=10)
        self.top_top_frame.pack(side=TOP, fill=None, expand=False)
        # Top Bottom Frame
        self.top_bottom_frame = Frame(self.top_frame, padding=10)
        self.top_bottom_frame.pack(side=BOTTOM)

        # Bottom Frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill='x', expand=True)

        # Directory Text 
        self.directory_entry = Entry(self.top_top_frame, text='', width=75)
        self.directory_entry.pack(side=LEFT, fill='x', expand=True)

        # Select Directory Button
        self.select_directory_button = Button(self.top_top_frame, text='Select Directory', command=self.select_directory)
        self.select_directory_button.pack(side=RIGHT)

        # Buttons
        self.next_button = Button(self.top_bottom_frame, text="Next", command=self.next_image, \
                                    relief='flat', border=0, image=self.right_arrow)
        self.next_button.pack(side=RIGHT)

        self.previous_button = Button(self.top_bottom_frame, text="Previous", command=self.previous_image, \
                                    relief='flat', border=0, image=self.left_arrow)
        self.previous_button.pack(side=LEFT)

        self.replace_button = Button(self.top_bottom_frame, text="Replace", command=self.replace_image, cursor='pirate', activebackground='black', image=self.skull,  \
                                        height=20, width=40, relief='flat', border=4)
        self.replace_button.pack()
        self.replace_button.bind('<Enter>', self.button_black)
        self.replace_button.bind('<Leave>', self.button_neutral)
        
        


    def button_black(self, event):
        self.replace_button.config(background='black')

    def button_neutral(self, event):
        self.replace_button.config(background="#f0f0f0")


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

if __name__ == "__main__":
    app = Application()
    app.mainloop()