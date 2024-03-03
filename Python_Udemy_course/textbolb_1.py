#!/usr/bin/python3

# This script translates from English to German using TextBlob module

from textblob import TextBlob

def translate_english_to_german():
    print("Hi, I'm a translator. I translate English to German.")
    insert_txt = input("Input the text you want to translate: ")

    try:
        add_blob = TextBlob(insert_txt)
        output = add_blob.translate(to='de')
        print("Translation:")
        print(output)
    except Exception as e:
        print(f"Error during translation: {e}")

if __name__ == "__main__":
    translate_english_to_german()