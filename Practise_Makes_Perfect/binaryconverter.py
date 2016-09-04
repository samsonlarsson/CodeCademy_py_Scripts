def binary_converter(number):
    if number < 0:
      return "Invalid input"
    elif number > 255:
      return "Invalid input"
    else:
      return "{0:b}".format(number)
