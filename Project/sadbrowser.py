from tkinter import *
from tkinter import ttk
from webbrowser import open_new_tab
import webbrowser

class WebBrowser:
    def __init__(self, master):
        self.master = master
        master.title("Web Browser")

        self.back_button = Button(master, text="<", command=self.go_back)
        self.back_button.grid(row=0, column=0)

        self.forward_button = Button(master, text=">", command=self.go_forward)
        self.forward_button.grid(row=0, column=1)

        self.url_entry = Entry(master)
        self.url_entry.grid(row=0, column=2)

        self.go_button = Button(master, text="Go", command=self.go_to_url)
        self.go_button.grid(row=0, column=3)

        self.browser = ttk.Frame(master)
        self.browser.grid(row=1, column=0, columnspan=4)

        self.master.bind("<Control-t>", self.open_new_tab)

    def go_back(self):
        webbrowser.back()

    def go_forward(self):
        webbrowser.forward()

    def go_to_url(self):
        url = self.url_entry.get()
        webbrowser.open(url)

    def open_new_tab(self, event):
        open_new_tab("https://www.google.com")


root = Tk()
my_browser = WebBrowser(root)
root.mainloop()
