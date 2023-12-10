"""
Author: Elliot Shabram
Course: cst205
Date: 10/6/2023
Description: This is a gui implementation of a caesar cipher decryptor and encryptor. It
lists all possible encryption and decryption schemes, as well as autodetecting the correct
decryption for a given cipher text.

"""

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QCheckBox, )
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from decrypt import decode, cipher_decrypt


app = QApplication([])
labels = {}
color_autodetect = "#00FF00"

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    # add all the Q items, such as buttons and line_edit
    self.check = QCheckBox('Autodetect (on/off)', self)
    btn1 = QPushButton('Encrypt')
    self.l1 = QLabel('Caesar Cipher:')
    btn2 = QPushButton('Decrypt')
    self.vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    self.btn_box = QHBoxLayout()
    self.lbox = QVBoxLayout()

    # set up the search bar
    self.my_le = QLineEdit("Enter string to decrypt...")
    self.my_le.minimum_width = 600
    self.my_le.select_all()

    # add the widgets to the layout
    self.vbox.add_widget(self.l1)
    self.vbox.add_widget(self.my_le)
    hbox.add_widget(self.check)
    self.btn_box.add_widget(btn1)
    self.btn_box.add_widget(btn2)
    self.vbox.add_layout(self.btn_box)
    self.vbox.add_layout(hbox)
    self.vbox.add_layout(self.lbox)

    # Store labels in a dictionary with indices as keys
    for i in range(26):
        label = QLabel(f'{i}')
        labels[i] = label  
        self.lbox.add_widget(label)
    # set the layout and connect the buttons
    self.set_layout(self.vbox)
    btn1.clicked.connect(self.encrypt)
    btn2.clicked.connect(self.decrypt)


  @Slot()
  def encrypt(self):  
      """
      this method encrypts a given plain text string using caeser shifts, for all
      values 0 - 25.
      """       
      input_text = self.my_le.text.strip()
      for i, label in labels.items():
          decrypted = decode(-abs(26 - i), input_text)
          label.text = f'{i} - {decrypted}'


  @Slot()
  def decrypt(self):      
      """
      This method decrypts a given cipher text for all values 0 - 25, and implements
      the autodetection feature.
      """   
      input_text = self.my_le.text.strip()
      if not self.check.checked:
        for i, label in labels.items():
            decrypted = decode(26 - i, input_text)
            label.text = f'{i} - {decrypted}'
      else:
        shift, plaintext = cipher_decrypt(None, input_text)
        # print(f'Shift = {shift}       Msg = {plaintext}')
        for i, label in labels.items():
          if i != shift:
            decrypted = decode(26 - i, input_text)
            label.text = f'{i} - {decrypted}'          
          else:
            label.text = f'{i} - <font color={color_autodetect}>{plaintext}</font>'
             
      

main = MyWindow()
main.show()
sys.exit(app.exec())