def minmax(data):
    if len(data):
        small = large = data[0]
        for value in data:
            if value<small: small = value 
            elif value>large: large = value
        return (small, large)
        
    else:
        print ('Data anda kosong')
        return
    
print(minmax([4,2,1,6,5,3]))
print(minmax([4,2,5,4,5,6]))
print(minmax([]))
print(minmax([3,35,7]))
