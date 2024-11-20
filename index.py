def avg(array):

    if len(array) <= 1:

        return array[0]
    
    else:
        count = len(array)
        
        return (array[0] + (count - 1) * avg(array[1:]))/count


 
