def something( one, two, three):
    print( "when",  three, "is divided by", two, "add", one )
    return()
    
a = int(input("Insert one number:" "\n"))
b = int(input("Insert two number:" "\n"))
c = int(input("Insert three number:" "\n"))

first = (c/b)+1

something(a, b, c)
print(int(first))


# newfunction

def greeting(lang):
    if lang == "es":
        print("Hello, Holla")
        
    elif lang == "fr":
        print("Bonjour")
        
    else:
        print("Hello, Glad to Have you here")
        
        
greeting("es")
greeting("en")
greeting("fr")

quit()