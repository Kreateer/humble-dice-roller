import random
import os
import PySimpleGUI as sg

folder = os.getcwd()
file_list = os.listdir(folder)
is_img_folder = os.path.isdir(folder)

# Gets list of .png files in current directory
fnames = [folder + '\\' + f for f in os.listdir(folder) if '.png' in f]

num_files = len(fnames)

# Checks if in correct folder and returns error otherwise
if not is_img_folder:
    sg.popup_ok_cancel('Error! Folder not found!')
    raise SystemExit()

# Checks if there are files in folder and returns error if none
if num_files == 0:
    sg.popup('No files in folder!')

background = '#F0F0F0'

# First image to appear on program start
first_img = os.path.join(folder, fnames[0])

# Picks a random dice image from list
random_img = os.path.join(folder, fnames[random.randint(0, 5)])


def SimpleGUI():
    # Sets the background the same color as the buttons
    sg.SetOptions(background_color=background, element_background_color=background)

    # Define GUI layout
    layout = [[sg.Text("Simple Dice Roller", background_color=background, text_color='#000000', font=("Helvetica", 15),
                       justification='center')],
              [sg.Text("Press 'Roll the Dice' to get a random dice number or press 'Exit' to close the program.",
                       background_color=background, text_color='#000000', font=("Helvetica", 15),
                       justification='center')],
              [sg.Image(filename=fnames[0], background_color=background, key='__IMAGE__')],
              [sg.Button("Roll the Dice!"),
               sg.Button("Exit")]]

    window = sg.Window("Simple Dice Roller v1.0", layout, resizable=True, default_element_size=(5, 5),
                       element_justification='center', font=("Helvetica", 25))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event in ('Roll the Dice!'):
            window.Element('__IMAGE__').update(filename=fnames[random.randint(0, 5)])
    window.close()


SimpleGUI()