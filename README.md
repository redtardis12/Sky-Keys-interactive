
# Sky-Keys-interactive
An app for the PC version of sky to key bind expressions and auto play music with sheets


## This is an initial source sync made just for the feedback, not an actual release !!!
The first release with a build and installer will be available soon. Now you can use the app from the source. The code haven't been revised and just a proof of concept

### Currently working features
> Automatic music player
#### "emotes" tab doesn't do anything for now

### Using from source
1. Have the latest version of python installed on your system from [python.org](https://python.org)
2. In your command line execute:

    pip install flet

3. Open cloned directory and execute:

    python app.py

### How to use?
1. Open the app, go to music Tab
2. Download any json format sheet for sky from [here](https://specy.github.io/skyMusic/) as an example
3. Press a **"+"** button and choose your downloaded song.
4. Choose it from the list and press **"play"** button at the bottom right - this will start listening for hotkeys to start and stop the music. The default ones are **"/"** to start playing and **"q"** to stop. You can change them in `config.json`file in the same directory, as well as all the notes buttons. 
5. To switch music **you need** to hit the **play** into pause and play again
6. You change the speed of the music by going into the .txt file of the music itself and adjust its value under the **"bpm"** field, or edit it somewhere like Sky Nightly


### FAQ
**Q:** Can i get banned for this?
**A:** You shouldn't. The app just simulates key presses like any other macro and **does not interfere with the game in any way**
