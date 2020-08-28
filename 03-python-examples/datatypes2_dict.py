vocabulary = dict() # optional
vocabulary = {
    'hello' : ['你好', '您好'],
    'bye' : '再见',
    'good evening' : '晚上好',
    20200812 : ('Shanghai','33.8','141')
}

print(vocabulary)
print(vocabulary.get('bye'))
print(vocabulary['bye'])
print(vocabulary.get('test'))