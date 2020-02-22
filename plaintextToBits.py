
def textToInt(text):
    # text is a 4 char string
    # return one int

    res = [ord(s) for s in text]
    
    return sum(res)



text = 'yeah'
res = textToInt(text)

ilist = [ord(s) for s in text]

print(res)
print(ilist)
