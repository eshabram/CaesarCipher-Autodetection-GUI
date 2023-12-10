# Caesar Cipher GUI:
## Dependencies:
```
pip3 install pyside6
```
---
### Run the code:
To run the program properly, ensure the gui.py, decrypt.py, and en-US.dic are all present in the same folder.
Simply run this command to activate the GUI:
```
python3 gui.py
```
This will open the GUI, in which you can enter either cipher or plain text to be decrypted or encrypted, respectively. 
Select the checkbox for autodetection of a given ciphertext. If it is already in plaintext, the same plain text will be shown 
with 0 shift. If the encrypt button is pressed when the autodetect checkbox is selected, the program wil simply clear the 
array 0 - 26 without a problem. 

### Change Highlight Color:
There is a variable at the top of gui.py named "color_autodetect". Change the hex value to change the color of the 
highlighted autodetected plaintext for the autodetection method.
