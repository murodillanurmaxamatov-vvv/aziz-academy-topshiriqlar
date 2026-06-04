
th1, lang1, dbg1 = input().split()

th2, lang2, dbg2 = input().split()

settings = {
    'theme': th1,
    'lang': lang1,
    'debug': True if dbg1 == '1' else False,
    'override': {
        'theme': th2,
        'lang': lang2,
        'debug': None if dbg2 == '-' else (True if dbg2 == '1' else False)
    }
}


x = th2 if th2 != '-' else th1
v = lang2 if lang2 != '-' else lang1
c = settings['override']['debug'] if settings['override']['debug'] is not None else (True if dbg1 == '1' else False)

print(f"{x} {v} {1 if c else 0}")