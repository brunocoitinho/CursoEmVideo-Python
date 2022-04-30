txt = str(input('Digite um frase: '))
txt_split = txt.split()
txt_sum = ''

for c in range(0, len(txt_split), 1):
    txt_sum += txt_split[c].lower()

i = len(txt_sum)-1
t = 0

for c in range(0, len(txt_sum), 1):

    if txt_sum[c] != txt_sum[i]:
        t += 1
    i -= 1

if t == 0:
    print('A frase é um palindromo')
else:
    print('A frase NÃO é um palindromo')

