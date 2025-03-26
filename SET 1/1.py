while True:
    ch=int(input("Enter your choice:\n1.Fahrenheit\n2.Celsius\n3.Exit\n"))
    if ch == 1:
        far= float(input("\nEnter the temperature in Fahrenheit:"))
        cel= (far - 32) * (5/9)
        print("\nThe temperature in celsius is: {:.2f}degree celsius".format(cel))
    elif ch == 2:
        cel = float(input("\nEnter the temperature in celsius:"))
        far = (cel*9/5)+32
        print("\nThe temperature in fahrenheit is: {:.2f}degree fahrenheit".format(far))
    elif ch == 3:
        break
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")
            



