
# Sky-Keys-interactive
An app for the PC version of Sky:COTL to key bind expressions and auto play music with sheets
[![J4bp4AN.md.png](https://iili.io/J4bp4AN.md.png)](https://freeimage.host/i/J4bp4AN)

[![J4bppHl.md.png](https://iili.io/J4bppHl.md.png)](https://freeimage.host/i/J4bppHl)

## This is an initial source sync made just for the feedback, not an actual release !!!
<br />

### You can now download the pre-relase version [here](https://github.com/redtardis12/Sky-Keys-interactive/releases/tag/pre-release)
<ins>**Just extract the archive and launch .exe**</ins>
The code haven't been revised and just a proof of concept
<br />

### Currently working features
> Automatic music player
#### "emotes" tab doesn't do anything for now
<br />

### How to use?
1. Open the app, go to music Tab
2. Download any json format sheet for sky from [here](https://specy.github.io/skyMusic/) as an example
3. Press a **"+"** button and choose your downloaded song.
4. Choose it from the list and press **"play"** button at the bottom right - this will start listening for hotkeys to start and stop the music. Got to sky, pick your instrument and press the keybind. The default ones are **"/"** to start playing and **"q"** to stop. You can change them in `config.json`file in the same directory, as well as all the notes buttons. 
5. You can change the speed of the music by going into the .txt file of the music itself and adjust its value under the **"bpm"** field, or edit it somewhere like Sky Nightly
<br />
<br />
<br />

### Using from source
1. Have the latest version of python installed on your system from [python.org](https://python.org)
2. In your command line execute:
```bash
    pip install -r requirements.txt
```

3. Open cloned directory and execute:
```bash
    python app.py
```
4. For building use flet packaging with pyinstaller:
```bash
    pip install pyinstaller
    flet pack app.py
```
or more optimized variant with UPX
```bash
    pyinstaller --noconsole --onefile --upx-dir [your upx installation folder here] app.py
```


### FAQ
**Q:** Can i get banned for this?

**A:** You shouldn't. The app just simulates key presses like any other macro and **does not interfere with the game in any way**
