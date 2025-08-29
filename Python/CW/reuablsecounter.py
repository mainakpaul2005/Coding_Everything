# Our counter function
def counter():
  c = 0 # Local counter variable
   
  # This function manipulate the
  # local c variable, when called
  def count():
    nonlocal c
    c += 1
    return c
   
  # Return the count() function to manipulate
  # the local c variable on every call
  return count
 
# Assign the result of counter() to
# a variable which we use to count up
my_counter = counter()
for i in range(3):
  print(my_counter())
print('End of my_counter')
   
# Create a new counter
new_counter = counter()
for i in range(3):
  print(new_counter())
print('End of new_counter')