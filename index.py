def avg(array):

    if len(array) <= 1:

        return array[0]
    
    else:
        count = len(array)
        
        return (array[0] + (count - 1) * avg(array[1:]))/count

#array = [5 , 5 , 5]
#array = [10 , 20 , 30 , 40]
array = [3, 7, 12, -5, 8, 15]
print(avg(array))
 
