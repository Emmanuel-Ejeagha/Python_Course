#!/usr/bin/python3
# This script translates from English to arabic

from translate import Translator

print("Enter a text and I will translate it to Arabic")
inserted_txt = input("Input the text you want to translate: ")
translator = Translator(from_lang="english", to_lang="arabic")
translation = translator.translate(inserted_txt)
print(translation + "\n")
