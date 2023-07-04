with open('artifact.txt', 'r') as f:
    text = f.read()

with open('artifact.txt','w') as f:
    f.write(text + '\n adding one more line')

print(text)
print('stage 3 done.')