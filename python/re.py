import re

def multi_re_find(patterns, phrase):
     for pat in patterns:
            print('searching for pattern: {}'.format(pat))
            print(re.findall(pat, phrase))
            print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds..dssssss...sddddd'

test_patterns = ['sd+']

multi_re_find(test_patterns, test_phrase)
