#!/usr/bin/python3

def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 400:
            return "Not found"
        case 418:
            return "I' am a teapot"
        case _:
            return "Something's wrong eith the internet"
