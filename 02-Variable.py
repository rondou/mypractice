# 02-Variable
# '#'號開頭的是註解

"""
或是連續三個 " 號裡面也是註解
如此就可以一次打多行的註解了
"""

name = raw_input('Your name:')
company = raw_input('Your company:')
age = raw_input('Your age:')

print '*' * 30  # 字串也是可以做乘法運算的
print 'I am %s, works at %s, and I am %d years old' % (name.upper(), company.upper(), int(age) - 5)
print '*' * 30    

raw_input('Press Enter to Exit...')


