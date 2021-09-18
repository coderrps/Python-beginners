#translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "R"
            else:
                translation = translation + "r"    
        else:
            translation = translation + letter     
    return translation

print(translate(input("Enter a phrase to translate: ")))            