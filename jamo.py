a = '한'
b = ord(a)-ord('가')
cho = [chr(i) for i in range(0x1100, 0x1113)]
jung = [chr(i) for i in range(0x1161, 0x1176)]
jong = [''] + [chr(i) for i in range(0x11A8, 0x11C3)]
print(cho)
print(jung)
print(jong)

print(cho[b//588])
print(jung[b//28%21])
print(jong[b%28])

print(chr(b//588*588+b//28%21*28+b%28 + ord('가')))

