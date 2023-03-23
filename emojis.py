def emojis(stmnt):
    em = {
        "happy":"😊",
        "sad":"😔"
    }
    words = stmnt.split(" ")
    ret = ""
    for word in words:
        if word in em:
            ret+=em[word]+" "
        else:
            ret+=word+" "
    return ret             

x = input("Enter your feelings")
print(emojis(x))