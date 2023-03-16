import tkinter as tk
import subprocess


root = tk.Tk()
root.geometry('400x400+1097+117')
root.title('Dropdown Example')

selected_options = None

# Define the options for the dropdowns
options = {
    'Select Base Shape': ['Round', 'Square', 'Heart'],
    'Select Base Color': ['Choc', 'Pink', 'Yellow'],
    'Select Base Top': ['Choc', 'Pink', 'Yellow'],
    'Select Cherry on Top': ['Triple', 'Smiley', 'Heart', 'Leaf']
}

# Create the dropdowns and labels
dropdowns = []
labels = []

for i, (option_label, option_list) in enumerate(options.items()):
    label = tk.Label(root, text=option_label)
    label.grid(row=i, column=0, padx=10, pady=10)
    labels.append(label)

    var = tk.StringVar()
    dropdown = tk.OptionMenu(root, var, *option_list)
    dropdown.grid(row=i, column=1, padx=10, pady=10)
    dropdowns.append(var)

# Define the function to print the selected options to the console
def pass_selected_options():
    global selected_options
    selected_options = [dropdown.get() for dropdown in dropdowns]
    for dropdown in dropdowns:
        dropdown.set('')
    print(selected_options)
    subprocess.call(['python', 'automate0.py', *selected_options])

# Create the button to pass the selected options to the other script
button = tk.Button(root, text='Pass Selected Options', command=pass_selected_options)
button.grid(row=len(options), column=0, columnspan=2, padx=10, pady=10)




root.mainloop()


def getSelectedOptions():

    return selected_options