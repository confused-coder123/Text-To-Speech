import PySimpleGUI as sg
import pyttsx3

# initializing text to speech engine
engine = pyttsx3.init()

# Defining the window's contents
input_box = sg.Input('Enter your text here', do_not_clear=False, font='8', key='input')
speak_button = sg.Button('Speak', key='speak', font='11')
male_speaker = sg.Radio('Male', 'gen', key='male', default=True, enable_events=True, font='11')
female_speaker = sg.Radio('Female', 'gen', key='female', enable_events=True, font='11')
rate_slider = sg.Slider((0, 10), 5, key='rate', orientation='h')
volume_slider = sg.Slider((0, 10), 10, key='volume', orientation='h')
layout = [[input_box, speak_button],
          [sg.Text('Select Voice Type', font='11'), male_speaker, female_speaker],
          [sg.Text('Adjust rate of speech'), rate_slider],
          [sg.Text('Adjust volume'), volume_slider]
          ]

# Create the window
window = sg.Window('Text To Speech App', layout, font='11', finalize=True)
while True:
    event, values = window.read()
    # QUITTING
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # ON CLICK SPEAK
    if event == 'speak':
        # getting voice from user
        voice = 'male' if values['male'] else 'female'
        # getting voices from engine
        voices = engine.getProperty('voices')

        # telling user to enter text if nothing was entered
        if values['input'] == '':
            engine.say('Please enter some text')
        # speaking out the input text
        else:
            engine.setProperty('rate', values['rate'] * 40)
            engine.setProperty('volume', values['volume'] / 10)
            engine.setProperty('voice', voices[0].id if voice == 'male' else voices[1].id)
            engine.say(values['input'])
        engine.runAndWait()
window.close()
