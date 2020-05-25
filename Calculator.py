if __name__ == '__main__':
  while True:
    działanie = input("Wybierz rodzaj działania: +, -, *, /, **:  ")
    try:
        number1 = int(input("Podaj liczbę:"))
    except ValueError:
        print("To nie jest liczba")
        number1 = False
    try:
      number2 = int(input ("Podaj kolejną liczbę:"))
    except ValueError:
        print("To nie jest liczba")
        number2 = False
    if number1 and number2 :
        if (działanie == "+"):
            print(str(number1) + (" + ") + str(number2) + (" = ") + str(number1 + number2))
        elif (działanie == "-"):
            print(str(number1) + (" - ") + str(number2) + (" = ") + str(number1 - number2))
        elif (działanie == "*"):
            print(str(number1) + (" * ") + str(number2) + (" = ") + str(number1 * number2))
        elif (działanie == "/"):
            try:
                print(str(number1) + (" / ") + str(number2) + (" = ") + str(number1 / number2))
            except ZeroDivisionError:
                print("Nie dzielimy przez zero.")
        elif (działanie == "**"):
            print(str(number1) + (" ** ") + str(number2) + (" = ") + str(number1 ** number2))
        else:
            print("Wybrałeś/aś nieprawidłowy rodzaj działania.")
    else:
        print ("Coś poszło nie tak :(")
