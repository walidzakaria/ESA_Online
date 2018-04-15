
"""
str_image = '''
data:image/jpeg;base64,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…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
'''

encoded = str_image.encode('utf-8')

imgdata = base64.b64decode(str_image.encode('utf-8'))

file_name = 'profile.jpg'
with open(file_name, 'wb') as f:
    f.write(imgdata)

"""
string = ' walid '
print('"' + string.strip() +'"')
