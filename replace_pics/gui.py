from os.path import exists, abspath
from tkinter import RIGHT, Tk, PhotoImage, TOP, BOTTOM, END, LEFT, Button, BOTH
from tkinter.ttk import Frame, Entry, Label
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk


class Application(Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Replace Images")
        self.geometry("500x500")
        self.minsize(500, 500)
        #self['bg'] = "#404040"
        self._make_frames()
        self._place_widgets()
        self._load_images()
        self._place_images()
        self._update_image_size()

        # Part of a delay loop. Prevents high-speed consecutive function calls
        # when the window is being resized.
        self.should_update_image_size = True
        
    

        # Buttons
        """self.next_button = Button(self.top_bottom_frame, text="Next", command=self.next_image, \
                                    relief='flat', border=0, image=self.right_arrow)
        self.next_button.pack(side=RIGHT)

        self.previous_button = Button(self.top_bottom_frame, text="Previous", command=self.previous_image, \
                                    relief='flat', border=0, image=self.left_arrow)
        self.previous_button.pack(side=LEFT)

        self.replace_button = Button(self.top_bottom_frame, text="Replace", command=self.replace_image, cursor='pirate', activebackground='black', image=self.skull,  \
                                        height=20, width=40, relief='flat', border=4)
        self.replace_button.pack()
        self.replace_button.bind('<Enter>', self._button_black)
        self.replace_button.bind('<Leave>', self._button_neutral)"""

    def _load_images(self):
        self.minion = Image.open("./images/alison-wang-mou0S7ViElQ-unsplash.jpg")
        #self.minion = self.minion.resize((500, 500), resample=Image.LANCZOS)
        self.minion_photoimage = ImageTk.PhotoImage(self.minion)
        self.skull = Image.open(abspath("./images/sku11.png"))
        self.skull = ImageTk.PhotoImage(self.skull.resize((20, 22), resample=Image.LANCZOS))
        self.right_arrow = Image.open(abspath("./images/right_arrow_transparent.png"))
        self.right_arrow = ImageTk.PhotoImage(self.right_arrow)
        self.left_arrow = Image.open(abspath("./images/left_arrow_transparent.png"))
        self.left_arrow = ImageTk.PhotoImage(self.left_arrow)

    def _place_widgets(self):
        # Replace Button
        self.replace_button = Button(self.top_top_middle_frame, text="Replace", command=self.replace_image, cursor='pirate', activebackground='black', image=self.skull,  \
                                        height=20, width=40, relief='flat', border=4)
        self.replace_button.pack(side=BOTTOM)
        self.replace_button.bind('<Enter>', self._button_black)
        self.replace_button.bind('<Leave>', self._button_neutral)

        # Replacement Files Directory 
        self.replacements_entry = Entry(self.top_top_left_frame, text='')
        self.replacements_entry.pack(side=TOP, fill='x', expand=True)
    
        # Select Replacement Files Button
        self.select_replacements_button = Button(self.top_top_left_frame, text='Replacements', command=self.select_replacements_dir)             #self.select_directory)
        self.select_replacements_button.pack(side=BOTTOM, pady=10)

        # Original Files Directory
        self.originals_entry = Entry(self.top_top_right_frame, text='')
        self.originals_entry.pack(side=TOP, fill='x', expand=True)
    
        # Select Original Files Button
        self.select_originals_button = Button(self.top_top_right_frame, text='Originals', command=self.select_originals_dir)             #self.select_directory)
        self.select_originals_button.pack(side=BOTTOM, pady=10)
    
    def _place_images(self):
        # Left Image
        self.left_image = Label(self.bottom_frame, image=self.minion_photoimage)
        self.left_image.pack(side=LEFT)

        # Right Image
        self.right_image = Label(self.bottom_frame, image=self.minion_photoimage)
        self.right_image.pack(side=RIGHT)
        self.bottom_frame.bind("<Configure>", self._update_image_size_wrapper)


    def _make_frames(self):
        # Top Frame
        self.top_frame = Frame(self, padding=10)
        self.top_frame.pack(side=TOP, fill='x', expand=False, anchor='n')
        #--------------------------------------------------------------------
        # Top Top Frame
        self.top_top_frame = Frame(self.top_frame, padding=10)
        self.top_top_frame.pack(side=TOP, fill='x', expand=True)
        # Top Top Right Frame
        self.top_top_right_frame = Frame(self.top_top_frame, padding=10)
        self.top_top_right_frame.pack(side=RIGHT, fill='x', expand=True)
        # Top Top Left Frame
        self.top_top_left_frame = Frame(self.top_top_frame, padding=10)
        self.top_top_left_frame.pack(side=LEFT, fill='x', expand=True)
        # Top Top Middle Frame
        self.top_top_middle_frame = Frame(self.top_top_frame, padding=10)
        self.top_top_middle_frame.pack(side=BOTTOM, expand=False, fill='y')
        #--------------------------------------------------------------------
        # Top Bottom Frame
        self.top_bottom_frame = Frame(self.top_frame, padding=10)
        self.top_bottom_frame.pack(side=BOTTOM, fill=None, expand=False)
        #--------------------------------------------------------------------
        # Bottom Frame
        self.bottom_frame = Frame(self) #, borderwidth=2, relief='sunken')
        self.bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=True)


    def _update_image_size_wrapper(self, event):
        if self.should_update_image_size == True:
            self.should_update_image_size = False
            self.after(500, self._update_image_size)
            
    
    def _update_image_size(self):
        self.bottom_frame.update()
        new_height = self.bottom_frame.winfo_height()
        new_width = self.bottom_frame.winfo_width()/2.1
        self.minion_photoimage= ImageTk.PhotoImage(self.minion.copy().resize((int(new_width), new_height), resample=Image.LANCZOS))
        self.left_image = Label(self.bottom_frame, image=self.minion_photoimage)
        self.left_image.pack(side=LEFT)
        self.right_image = Label(self.bottom_frame, image=self.minion_photoimage)
        self.right_image.pack(side=RIGHT)
        self.should_update_image_size = True
        pass
        

    def _button_black(self, event):
        self.replace_button.config(background='black')

    def _button_neutral(self, event):
        self.replace_button.config(background="#f0f0f0")


    def select_replacements_dir(self):
        self.replacements_path = askdirectory(title='Select Folder of Replacements')
        if exists(self.replacements_path):
            self.replacements_entry.delete(0, END)
            self.replacements_entry.insert(0, self.replacements_path)

    def select_originals_dir(self):
        self.originals_path = askdirectory(title='Select Folder of Originals')
        if exists(self.originals_path):
            self.originals_entry.delete(0, END)
            self.originals_entry.insert(0, self.originals_path)
                
    def next_image(self):
            pass

    def previous_image(self):
            pass
    
    def replace_image(self):
            pass

if __name__ == "__main__":
    app = Application()
    app.mainloop()
