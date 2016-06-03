
def tuner(**kwargs):   #keyword argumnt param
    print kwargs

tuner()  #empty dictionary
tuner(brightness=0.1,contrast=0.6,hue=0.9)

info = {'hostname' : 'ws1' , 'domain' : 'rootcap.in' , 'pladorm' : 'linux'}
tuner(**info)


l = [1,2,5,6,9,33,24,11]
l.sort(reverse=True)
print l