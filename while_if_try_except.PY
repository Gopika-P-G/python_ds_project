largest = None
smallest = None
while  True:
    num = input("Enter the number:")
    if num == "done":
        print('Maximum is',largest)
        print('minimum is',smallest)
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
		
        continue
       
    if smallest is None:
        smallest = num
    elif num < smallest:
    	smallest = num
        
    if largest is None:
        largest = num
    elif num > largest:
    	largest = num