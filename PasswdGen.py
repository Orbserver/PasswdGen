init = 2018
end = 2024

def passwdPattern(user_inpput):
    comb = []

    for year in range(init, end + 1):
        comb.append(f"{user_input}{year}")

    for i in range(len(user_input)):
        for j in range(i, len(user_input)):
            for year in range(init, end + 1):
                comb.append(f"{user_input[:i]}{user_input[i:j+1].upper()}{user_input[j+1:]}{year}")

    string = "\n".join(comb)
    print(string)

user_input = input("Introduce una cadena de caracteres: ")
passwdPattern(user_input)
