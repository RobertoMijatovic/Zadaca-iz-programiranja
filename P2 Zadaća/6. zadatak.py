def obrnuto(string):
    if len(string) <= 1:
        return string
    else:
        return obrnuto(string[1:]) + string[0]

print(obrnuto("kolokvij"))
