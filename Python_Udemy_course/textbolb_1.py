#!/usr/bin/python3

# This script translates from English to German using testblob module

from textblob import TextBlob

print("Hi, I'm a translator. I translate English to German")
insert_txt = input("Input the text you want to translate: ")
add_blob = TextBlob(insert_txt)
output = add_blob.translate(to = 'de')
print(output)
