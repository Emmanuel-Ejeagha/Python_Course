#!/usr/bin/python3

def mall(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ";", keywords[kw])


mall("shamppo, die and relaxer", "I am in a haste, sir.",
       "It's really very, very urgent, sir.",
        barber="Kingsley",
        customer="Moses",
        haircut_style="Low cut")
