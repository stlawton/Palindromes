def palindromes(string: string):
  front = 0  #set index for the first character in the string
  end = 1  #Intialize the helper for the last index of the string
  while front != end: # Loop through the string until the front and end are at the same index
    end = (len(string) - 1) - front  # move the end index in one as the front index advances one
    if string[front] != string[end]: # Test if the characters at the current front and end index are equal
      return False  # If they are not equal the word is not a palindrome, exits funstion and returns False
    front += 1  # Advance the front index by one
  return True # If the while loop exits without any of the characters being different return true

if __name__ == "__main__":
  string = input("Please type in a palindrome: ") #Initial string input
  palindrome = palindromes(string) # Call the palindromes function
  while palindrome == False: # if the first string is not a palindrome, loop until a palindrome is enetered
    print("that wasn't a palindrome")
    string = input("Please type in a palindrome: ")
    palindrome = palindromes(string)
  print(f"{string} is a palindrome!") # prints once a palindrome is entered by user
