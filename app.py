import os.path
from tkinter import *
from tkinter import filedialog

from pdf_parser import Pdf

# creating window
window = Tk()
window.title("Arpan PDF Parser")
window.configure(bg="white")


# initialize variables and instances
filename = "No pdf to parse."
pdf = Pdf()


# some important entries
dataframe_entry = Entry(window, bd=5)
dictionary_entry = Entry(window, bd=5)
csv_entry = Entry(window, bd=5)


# functions to connect entries and buttons
def get_dataframe():
    try:
        entry = dataframe_entry.get()
        return int(entry)
    except Exception as e:
        print(str(e))


def get_dictionary():
    try:
        entry = dictionary_entry.get()
        return int(entry)
    except Exception as e:
        print(str(e))


def get_csv():
    try:
        entry = csv_entry.get()
        return int(entry)
    except Exception as e:
        print(str(e))


def print_output(output_text):
    print(output_text)


# some important buttons
path_btn = Button(window, text="Path", command=lambda: [print_output(pdf.get_pdf_file())])
dataframe_btn = Button(window, text="Dataframe", command=lambda: [print_output(pdf.get_dataframe(get_dataframe()))])
dictionary_btn = Button(window, text="Dictionary", command=lambda: [print_output(pdf.get_dictionary(get_dictionary()))])
csv_btn = Button(window, text="CSV", command=lambda: [print_output(pdf.get_csv(get_csv()))])


# This will remove the widgets from toplevel
def hide_widgets(widgets):
    for widget in widgets:
        widget.pack_forget()


# This will recover the widgets from toplevel
def show_widgets(widgets):
    for widget in widgets:
        widget.pack(fill='x')


# Widgets that will deliver the outputs
output_widgets = [path_btn,
                  dataframe_entry, dataframe_btn,
                  dictionary_entry, dictionary_btn,
                  csv_entry, csv_btn]


# calling to hide widgets
hide_widgets(output_widgets)


# browsing the files
def browse_files():
    global filename
    filename = filedialog.askopenfilename(defaultextension='.pdf')
    label.config(text=filename)
    basename = os.path.basename(filename)
    pdf.set_pdf_file(basename)
    return basename


# creating label
label = Label(window, text=filename)
label.pack(pady=5)


# creating button
button = Button(window, text="Browse", command=lambda: [browse_files(), show_widgets(output_widgets)])
button.pack(pady=5)

window.mainloop()
