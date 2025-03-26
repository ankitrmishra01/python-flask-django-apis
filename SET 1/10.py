# Python program to convert decimal to binary, 
# octal and hexadecimal 

# Function to convert decimal to binary 
def decimal_to_binary(dec): 
	decimal = int(dec) 

	# Prints equivalent decimal 
	print(decimal, " in Binary : ", bin(decimal)) 

# Function to convert decimal to octal 
def decimal_to_octal(dec): 
	decimal = int(dec) 

	# Prints equivalent decimal 
	print(decimal, "in Octal : ", oct(decimal)) 

# Function to convert decimal to hexadecimal 
def decimal_to_hexadecimal(dec): 
	decimal = int(dec) 

	# Prints equivalent decimal 
	print(decimal, " in Hexadecimal : ", hex(decimal)) 

# Driver program 
dec = 32
decimal_to_binary(dec) 
decimal_to_octal(dec) 
decimal_to_hexadecimal(dec) 
