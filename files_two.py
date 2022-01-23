# у нас 2 текстовых файла, в каждом в отдельной  строке прписано одно число;
# в первом файле n, во втором m чисел

from random import randint


with open('1.txt', 'w') as f1, open('2.txt', 'w') as f2:
    
    n = randint(5, 15)
    m = randint(5, 15)

    list1 = sorted( [ randint(-100, 100) for i in range(n) ] )
    for i in range(n):
        f1.write( str(list1[i]) + '\n')


    list2 = sorted( [ randint(-100, 100) for i in range(m) ] )
    for i in range(m):
        f2.write( str(list2[i]) + '\n')
    
    
with open('1.txt', 'r') as f1, open('2.txt', 'r') as f2, open('out.txt', 'w') as outf:
    f1.seek(0)
    f2.seek(0)
    # нам неизвестен размер файлов изначально, нужно найти
    
    #для файла f1
    s = f1.readline()
    n=0
    while s.strip() != '':
        n+=1
        s = f1.readline()
    # не забываем переместить в начало!
    f1.seek(0)
        
    #для файла f2
    s = f2.readline()
    m=0
    while s.strip() != '':
        m +=1
        s = f2.readline()
        
    # не забываем переместить в начало!
    f2.seek(0)
        
        
    #текущие считанные элементы, фиксируют продвижение по соответствующим файлам
    pointer1 = int( ( f1.readline() ).strip() )
    pointer2 = int( ( f2.readline() ).strip() )

    i=2

    processed_f1 = 1
    processed_f2 = 1

    while i < (n+m):
        
        
        # обрабатываем первый файл
        # пока текущий элемент (pointer1) меньше pointer2 и обработанных элементов в файле f1 меньше общего количества элементов
        # или пока не кончился файл f1, если второй, f2, уже кончился
        #для обоих условий выше должно выполняться также то, что сам файл f1 не кончился
        
        while processed_f1 < n and (pointer1 <= pointer2 or processed_f2 >=m):
            
            outf.write(str(pointer1) + '\n' )
            pointer1 = f1.readline()
            pointer1 = int( pointer1.strip() )
            i+=1
            processed_f1 +=1
            
            
        # аналогично с f2
        while processed_f2 < m and (pointer2 <= pointer1 or processed_f1 >= n):
            
            outf.write(str(pointer2) + '\n' )
            pointer2 = f2.readline()
            pointer2 = int( pointer2.strip() )
            i+=1
            processed_f2 +=1
            
