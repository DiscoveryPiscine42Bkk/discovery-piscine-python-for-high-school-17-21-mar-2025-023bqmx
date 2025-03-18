def check_number_type(number_str):
  
  try:
    num = float(number_str)
    if num.is_integer():
      return "integer."
    else:
      return "demical."
  except ValueError:
    return "Error"

if __name__ == "__main__":
  number_input = input("Give me a number : ")
  result = check_number_type(number_input)
  print(f"This number is {result}")