def countdown(i):
    print(i)

    if i <= 1:  #base base 
        return
    else:       #recursive case 
        countdown(i-1)

countdown(3)