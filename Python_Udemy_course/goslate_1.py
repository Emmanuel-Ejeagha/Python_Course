#!/usr/bin/python3
# This program translates words from english to fr

import goslate

print("Hi, I'm a translator. I translate English to French")
inserted_text = input("Input the text you want to translate: ")
new_gs = goslate.Goslate()
trans_late = new_gs.translate(inserted_text, 'fr')
print(trans_late + "\n")
