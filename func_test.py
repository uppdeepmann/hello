

def change_list (list):
    list [1] = 4
    print(list)
    return

list  = [ 1 , 2,  4 , 8]
print(list)
change_list(list)
print(list)


def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)


# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))


total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total1 = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total :", total1)
   global total
   total = 10
   return total1;


str = input("Enter your input: ");
print ("Received input is : ", str)

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total)