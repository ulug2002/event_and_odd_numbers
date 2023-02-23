#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value
var_int = 4567
#Print the number of even digits in the variable "var_int".
a = var_int%10

var_int = var_int//10
b = var_int%10

var_int = var_int//10
c = var_int%10

v = var_int//10
print(v,c,b,a)