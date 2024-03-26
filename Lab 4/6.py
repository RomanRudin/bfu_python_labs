#symbols = ',.!?:;"()\t\n'
#data = input("Please, enter the text: ")
#for sym in symbols:
#    data = data.replace(sym, '')
#data = data.split()
#answer = sorted(set(data))
#answer = sorted(answer, key=lambda word: data.count(x), reverse=True)
#answer = '\n'.join(answer)
#print('The asnwer is:', answer, sep='\n')

symbols = ',.!?:;"()\t\n'
data = input("Please, enter the text: ")
for sym in symbols:
    data = data.replace(sym, '')
data = data.split()
print('The asnwer is:\n' +'\n'.join(sorted(sorted(set(data)), key=lambda word: data.count(word), reverse=True)))