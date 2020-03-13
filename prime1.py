def prime(num):
    if(num<=0):
        print('invalid input')
    elif(num>1):
        for i in range(2,num):
            if(num%i)==0:
                print('it it not a prime number')
                break
        else:
            print('it is a prime number')
    else:
        print('It is not a prime number')

