from tkinter import *
from tkinter import ttk

class CountdownTimer:
    def __init__(self, frm):
        self.frm = frm
        self.input_box =None
        self.enter_label = None
        self.time_left = None
        self.time_left_label = None
        self.timer_label = None
        self.start_button = None
        self.stop_button = None
        self.pause_button = None
        self.create_widgets()
    
    def create_widgets(self):
        self.enter_label = ttk.Label(self.frm, text ='Enter time in seconds : ')
        self.enter_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_box = ttk.Entry(self.frm, )
        self.input_box.grid(row=0, column=1, padx=10, pady=10)
        self.timer_label = ttk.Label(self.frm, text="Time Left:" , )
        self.timer_label.grid(row=1, column=0, padx=10, pady=10)
        self.time_left_label = ttk.Label(self.frm, text="" , )
        self.time_left_label.grid(row=1, column=1, padx=10, pady=10)
        self.start_button = ttk.Button(self.frm, text="Start", command=self.start_timer)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)
        self.stop_button = ttk.Button(self.frm, text="Pause", command=self.pause_timer)
        self.stop_button.grid(row=2, column=1,padx=10,pady=10 )
        self.stop_button = ttk.Button(self.frm, text="Stop", command=self.stop_timer)
        self.stop_button.grid(row=2, column=2,padx=10,pady=10 )
    
    def start_timer(self):
        try:
            if self.time_left is None:
                time_input = 1 + int(self.input_box.get())
                self.time_left = time_input
                self.time_left_label.configure(text=f"Time Left: {self.time_left} seconds")
            self.input_box.delete(0, 'end')
            self.update_timer()
            time_input = self
        except ValueError:
            self.time_left_label.configure(text="Invalid input")
    
    def update_timer(self):
        if self.time_left is not None: 
            if self.time_left <= 0:
                self.stop_timer()
                self.time_left_label.configure(text="0 seconds")
            else:
                i = 1
                self.time_left -= i
                self.time_left_label.configure(text=f"{self.time_left} seconds")
                self.timer = self.frm.after(1000, self.update_timer)
    
    def stop_timer(self):
        
        self.time_left_label.configure(text="0 seconds")
        self.time_left = None
    
    def pause_timer(self):
        if self.time_left is not None:
            self.frm.after_cancel(self.timer)

root = Tk()
root.title('Countdown Timer ')
frm = ttk.Frame(root, padding=10)
frm.grid()

timer = CountdownTimer(frm)

root.mainloop()