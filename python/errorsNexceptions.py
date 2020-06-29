# f = open('simple.txt', 'r')
# f.write('Test write to simple text!')

try:
    f = open('simple.txt', 'r')
    f.write('Test write to simple text!')
except:
    print('Error: Could not find file or read data')
else:
    print('success!')
    f.close()
finally:
    print('I always work. No matter what')
print('Hello World')
