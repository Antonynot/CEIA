import ast

def capter(message):
    
    string = str(message.decode("utf-8"))
    string = string.replace(" ","")
    response = ast.literal_eval(string)
    print(response)
