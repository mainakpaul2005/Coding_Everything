def alphabetPattern(N):
    Top, Bottom, Diagonal = 1, 1, N - 1
  
    
    for index in range(N):
        print("#", end = ' ')
        Top += 1
    print()
  
     
    for index in range(1, N - 1):
  
        
        for side_index in range(2 * (N - index - 1)):
            print(' ', end = '')
  
        
        print("#", end = '')
        Diagonal -= 1
        print()
  
    
    for index in range(N):
        print("#", end = ' ')
        Bottom += 1
  

N = int(input("Enter the no of lines: "))
alphabetPattern(N)
  