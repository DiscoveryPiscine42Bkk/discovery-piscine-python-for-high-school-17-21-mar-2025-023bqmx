def swap_case(s):

    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char 

    return result

if __name__ == "__main__":
    input_string = input("In put your word : ")
    output_string = swap_case(input_string)
    print("Your word has been change to : " ,output_string)