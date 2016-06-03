
def headntail(filename,**kwargs):
    valid_keys = ['count','order']

    for param in kwargs:
        if param not in valid_keys:
            raise TypeError(" '%s' is an invalid keyword argument for this function" % param)

    order = kwargs.get('order','head') #assign the default values
    count = kwargs.get('count',10) #defaule values

    if order == 'head':
        content = open(filename).readlines()[:count]
    elif order == 'tail':
        content = open(filename).readlines()[-count:]

    return ''.join(content)


config = {'order':'tail' , 'count':2}
print headntail('D:\passwd.txt' , **config)   #head /etc/passwd
#headntail('D:\passwd.txt', count=5) #head -5 /etc/passwd
print headntail('D:\passwd.txt', count=4 , order='tail') #tail -5 /etc/passwd


#headntail('D:\passwd.txt', order='head') #head  /etc/passwd