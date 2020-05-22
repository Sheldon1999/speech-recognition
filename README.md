# speech-recognition

This is a python script that will first **recognize whether device is connected to internet or not**, on the basis of that information **it will choose proper speech recognition engine and apply to the service**. I have also added a model(Indian english) which i have trained with my voice you can try that [model](https://github.com/Sheldon1999/speech-recognition/tree/master/en-in).

## Dependencies

1. [python](https://www.python.org/downloads/)
2. [pip](https://pip.pypa.io/en/stable/installing/)
3. [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
4. [python3-pyaudio](https://pypi.org/project/PyAudio/)
5. [pyttx3](https://pypi.org/project/pyttsx3/)
6. [pocketsphinx](https://pypi.org/project/pocketsphinx/)

## Local setup

1. install all the dependencies above.
2. download or clone repo.
3. open command prompt or terminal.
4. go to the repo folder.
3. run [script](https://github.com/Sheldon1999/speech-recognition/blob/master/script.py).

## Add your own model

You can make [your own speech recognition model](https://cmusphinx.github.io/wiki/tutorialadapt/) and just replace my model with your model.To replac go to line.68 in [script.py](https://github.com/Sheldon1999/speech-recognition/blob/master/script.py) and add the path specified.

