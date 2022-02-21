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
james = get_coach_data('james2.txt')
james_data={}
james_data ['Nome'] = james.pop(0)
james_data ['DataNasc'] = james.pop(0)
james_data ['Tempos'] = julie
print(james_data['Nome'] + " Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in james_data['Tempos']]))[0:3]))


julie = get_coach_data('julie.txt')
julie = get_coach_data('julie2.txt')
julie_data={}
julie_data ['Nome'] = julie.pop(0)
julie_data ['DataNasc'] = julie.pop(0)
julie_data ['Tempos'] = julie
print(julie_data['Nome'] + " Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in julie_data['Tempos']]))[0:3]))

mikey = get_coach_data('mikey.txt')
mikey = get_coach_data('mikey2.txt')
mikey_data={}
mikey_data ['Nome'] = mikey.pop(0)
mikey_data ['DataNasc'] = mikey.pop(0)
mikey_data ['Tempos'] = mikey
print(mikey_data['Nome'] + " Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in mikey_data['Tempos']]))[0:3]))

sarah = get_coach_data('sarah.txt')
sarah = get_coach_data('sarah2.txt')
sarah_data={}
sarah_data ['Nome'] = sarah.pop(0)
sarah_data ['DataNasc'] = sarah.pop(0)
sarah_data ['Tempos'] = sarah
print(sarah_data['Nome'] + " Os tempos mais rapidos são: " + str(sorted(set([sanitize(t) for t in sarah_data['Tempos']]))[0:3]))
