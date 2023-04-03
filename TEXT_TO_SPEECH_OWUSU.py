import PySimpleGUI as psg
import pyttsx3

layout = [
    [psg.Text("Enter Text Here to Speak: "), psg.InputText(key="-INPUT-")],
    [psg.Text("Select Voice Type" ), psg.Radio("Male Voice", "RADIO1", default=True, key="-MALE-"), psg.Radio("Female Voice", "RADIO1", key="-FEMALE-")],
    [psg.Button("Speak", key="-SPEAK-")],
    [psg.Text("Volume:"), psg.Slider(range=(0, 3), resolution=0.1, default_value=2, key="volume_slider")],
    [psg.Text("Speed:"), psg.Slider(range=(0.5, 4), resolution=0.5, default_value=1.5, key="speed_slider")]
]

window = psg.Window("Text-to-Speech App", layout)

engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == "-SPEAK-":
        text = values["-INPUT-"]
        if values["-MALE-"]:
            engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
        elif values["-FEMALE-"]:
            engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        engine.say(text)
        engine.runAndWait()

window.close()
