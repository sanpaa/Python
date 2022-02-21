import os
from types import TracebackType
os.chdir(r'C:\Users\paulo\Desktop\pastazinha')

with open('james.txt') as jaf:
    data=jaf.readline()
james=data.strip().split(',')
with open('julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')
with open('mikey.txt') as mif:
    data=mif.readline()
mikey=data.strip().split(',')
with open('sarah.txt') as saf:
    data=saf.readline()
sarah=data.strip().split(',')

def sanitize(time_string):
    if '-' in time_string:
            splitter = '-'
    elif':' in time_string:
            splitter = ':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return (None)


james = get_coach_data('james.txt')
julie = get_coach_data('james2.txt')
(james_name, james_dataNasc)= james.pop(0),james.pop(0)
print(james_name+"  Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in james]))[0:3]))

julie = get_coach_data('julie.txt')
julie = get_coach_data('julie2.txt')
(julie_name, julie_dataNasc)= julie.pop(0),julie.pop(0)
print(julie_name+" Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in julie]))[0:3]))

mikey = get_coach_data('mikey.txt')
mikey = get_coach_data('mikey2.txt')
(mikey_name, mikey_dataNasc)= mikey.pop(0),mikey.pop(0)
print(mikey_name+" Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in mikey]))[0:3]))

sarah = get_coach_data('sarah.txt')
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dataNasc)= sarah.pop(0),sarah.pop(0)
print(sarah_name+" Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))








print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])

