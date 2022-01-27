from random import randint

with open('in2.txt', 'w') as f2:
    n=4
    for i in range(n):
        num1 = randint(-100, 100)
        num2 = randint(-100, 100)

        f2.write(str(num1)+' '+str(num2)+'\n')
        
    
with open('in1.txt', 'r') as f1, open('in2.txt', 'r') as f2, open('out.txt', 'w') as outf:

    n=4
    for i in range(1, n+1):

        
        s1 = f1.readline()
        print(s1)
        string2 = f2.readline()

        while s1.strip() != str(i): 
            s1 = f1.readline()
            #print(s1)
            string2 = f2.readline()

        string2 = string2.strip()
        num1, num2 = map(int, string2.split())
        summ = num1+num2
        ##########
        odd = 0
        even = 0
        summ= abs(summ)

        while summ>0:
            digit = summ%10
            
            if digit%2:
                odd+=1
            else:
                even+=1

            summ = summ//10

        if even > odd:
            outf.write( str( num1+num2) + '\n' )

        

        ########
        f1.seek(0)
        f2.seek(0)
        
            
