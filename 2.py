def translate(text:str):
    vowel:list = ['a','e','i','o','u',' ']
    final_text:str = ""
    for char in text:
        if not vowel.__contains__(char):
            final_text+=char+'o'+char
        else: 
            final_text+=char
    return final_text
print(translate('this is fun'))