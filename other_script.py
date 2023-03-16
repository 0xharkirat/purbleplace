import subprocess
import tkinter as tk
from tkinter import ttk

# Create GUI window
root = tk.Tk()
root.geometry('400x600+1097+117')
root.title('Dropdown Example')


print('Program Started. Press Ctrl-C to abort at any time.')
print('TO interrupt mouse movement, move mouse to upper left corner.')

# Define function to switch tab
def switch_tab(event):
    tab = event.widget.select()


    
# Create notebook widget
notebook = ttk.Notebook(root)

# Create tabs and corresponding UI components
tab1 = ttk.Frame(notebook)
options1 = {
    'Select Base Shape': ['Round', 'Square', 'Heart'],
    'Select Base Color': ['Choc', 'Pink', 'Yellow'],
    'Select Base Top': ['Choc', 'Pink', 'Yellow'],
    'Select Cherry on Top': ['Triple', 'Smiley', 'Heart', 'Leaf']
}
dropdowns1 = []
labels = []
# label1 = tk.Label(tab1, text="This is tab 1")
# label1.pack()
for i, (option_label, option_list) in enumerate(options1.items()):
    label = tk.Label(tab1, text=option_label)
    label.grid(row=i, column=0, padx=10, pady=10)
    labels.append(label)

    var = tk.StringVar()
    dropdown = tk.OptionMenu(tab1, var, *option_list)
    dropdown.grid(row=i, column=1, padx=10, pady=10)
    dropdowns1.append(var)



tab2 = ttk.Frame(notebook)
# label2 = tk.Label(tab2, text="This is tab 2")
# label2.pack()
options2 = {
    'Select Base Shape': ['Round', 'Square', 'Heart'],
    'Select Base Color': ['Choc', 'Pink', 'Yellow'],
    'Select Sheet Color': ['Brown', 'Green', 'White'],
    'Select Second Base Color': ['Choc', 'Pink', 'Yellow'],
    'Select Base Top': ['Choc', 'Pink', 'Yellow'],
    'Select Cherry on Top': ['Triple', 'Smiley', 'Heart', 'Leaf'],
    'Select Position of white paper': [1,2,3,4,5,6]
}
dropdowns2 = []
label = []
# label1 = tk.Label(tab1, text="This is tab 1")
# label1.pack()
for i, (option_label, option_list) in enumerate(options2.items()):
    label = tk.Label(tab2, text=option_label)
    label.grid(row=i, column=0, padx=10, pady=10)
    labels.append(label)

    var = tk.StringVar()
    dropdown = tk.OptionMenu(tab2, var, *option_list)
    dropdown.grid(row=i, column=1, padx=10, pady=10)
    dropdowns2.append(var)


tab3 = ttk.Frame(notebook)
label3 = tk.Label(tab3, text="This is tab 3")
label3.pack()

# Add tabs to notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")

# Bind event handler to tab change
notebook.bind("<<NotebookTabChanged>>", switch_tab)

# Pack notebook widget
notebook.pack()


def pass_selected_options1():
    global selected_options
    selected_options = [dropdown.get() for dropdown in dropdowns1]
    for dropdown in dropdowns1:
        dropdown.set('')
    print('Easy Game')
    print(selected_options)
    subprocess.call(['python', 'automate0.py', *selected_options])

button1 = tk.Button(tab1, text='Pass Selected Options', command=pass_selected_options1)
button1.grid(row=len(options1), column=0, columnspan=2, padx=10, pady=10)

# Button for tab2
def pass_selected_options2():
    global selected_options
    selected_options = [dropdown.get() for dropdown in dropdowns2]
    dropdowns2[-1].set('')
    print('Intermediate game')
    print(selected_options)
    subprocess.call(['python', 'automate0.py', *selected_options])

button2 = tk.Button(tab2, text='Pass Selected Options', command=pass_selected_options2)
button2.grid(row=len(options2), column=0, columnspan=2, padx=10, pady=10)

# Run GUI window
root.mainloop()
