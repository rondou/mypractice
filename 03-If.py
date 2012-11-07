# 03-If

name = raw_input('Your name:').upper()
company = raw_input('Your company:').upper()
age = int(raw_input('Your age:'))
sex = raw_input('M/F:').upper()

if age >= 24 and sex == 'M':
    s1 = 'handsome'
    s2 = 'man'
elif age >= 24 and sex == 'F':
    s1 = 'beauty'
    s2 = 'woman'
# 到這邊，一定是 < 24 了，所以不用再判斷年齡，直接判斷性別就好了
# 這種邏輯的運用熟悉之後，可以優化你的程式
elif sex == 'M':
    s1 = 'cute'
    s2 = 'boy'
elif sex == 'F':
    s1 = 'cute'
    s2 = 'girl'

# print 統一寫在一個地方，好處是今天我要輸出 Hi 巴拉巴拉
# 改天我想要改成 Yo 巴拉巴拉，我只要改一個地方就好
# 不用每個 if 裡面的 print 都改
print 'Hi %s %s, %s' % (s1, s2, name)

if company == 'GIGABYTE':
    stock = '2376'
elif company == 'HTC':
    stock = '2498'
else:
    stock = 'Unknow'

print 'You company %s, stock id is %s' % (company, stock)
    



