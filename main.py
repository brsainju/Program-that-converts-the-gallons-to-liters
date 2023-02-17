#Example Program that converts the gallons to liters
def main():
    # displays the intro screen.
    intro() 
    try:  
      #Get the number of gallons
      gallons_needed = int(input('Please enter the number of gallons: '))
      #Converts the gallons to liters.
      gallons_to_liters(gallons_needed)
    except:
      print("An execption occurred try again by entering only a number")
      print()
      main()
def intro(): 
    print("Welcome to Program ")
    print("This program converts measurements in gallons to liters.")
    print("For your reference,the formula is: 1 gallon = 3.7854 liters.")
    print()
def gallons_to_liters(gallons):
    liters = gallons * 3.7854
    print('That converts to', liters, 'liters.')
# Call the main fuction.
main()
print('Thank you!')
print('Have a great day!')