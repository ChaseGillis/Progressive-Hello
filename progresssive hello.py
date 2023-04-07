import random as r
import string as s
import time as t

z = ''
a = r.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
while a != 'H':
    a = r.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if a == 'H':
        z += a
        print(z)
        break
    z += a
    print(z)
    z = z[:-1]
    t.sleep(0.01)

b = r.choice('abcdefghijklmnopqrstuvwxyz')
while b != 'e':
    b = r.choice('abcdefghijklmnopqrstuvwxyz')
    if b == 'e':
        z += b
        print(z)
        break
    z += b
    print(z)
    z = z[:-1]
    t.sleep(0.01)

c = r.choice('abcdefghijklmnopqrstuvwxyz')
while c!= 'l':
    c = r.choice('abcdefghijklmnopqrstuvwxyz')
    if c == 'l':
        z += c
        print(z)
        break
    z += c
    print(z)
    z = z[:-1]
    t.sleep(0.01)

d = r.choice('abcdefghijklmnopqrstuvwxyz')
while d!= 'l':
    d = r.choice('abcdefghijklmnopqrstuvwxyz')
    if d == 'l':
        z += d
        print(z)
        break
    z += d
    print(z)
    z = z[:-1]
    t.sleep(0.01)

e = r.choice('abcdefghijklmnopqrstuvwxyz')
while e!= 'o':
    e = r.choice('abcdefghijklmnopqrstuvwxyz')
    if e == 'o':
        z += e
        print(z)
        break
    z += e
    print(z)
    z = z[:-1]
    t.sleep(0.01)

z += ' '
print(z)

f = r.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
while f!= 'W':
    f = r.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if f == 'W':
        z += f
        print(z)
        break
    z += f
    print(z)
    z = z[:-1]
    t.sleep(0.01)

g = r.choice('abcdefghijklmnopqrstuvwxyz')
while g!= 'o':
    g = r.choice('abcdefghijklmnopqrstuvwxyz')
    if g == 'o':
        z += g
        print(z)
        break
    z += g
    print(z)
    z = z[:-1]
    t.sleep(0.01)

h = r.choice('abcdefghijklmnopqrstuvwxyz')
while h!= 'r':
    h = r.choice('abcdefghijklmnopqrstuvwxyz')
    if h == 'r':
        z += h
        print(z)
        break
    z += h
    print(z)
    z = z[:-1]
    t.sleep(0.01)

i = r.choice('abcdefghijklmnopqrstuvwxyz')
while i!= 'l':
    i = r.choice('abcdefghijklmnopqrstuvwxyz')
    if i == 'l':
        z += i
        print(z)
        break
    z += i
    print(z)
    z = z[:-1]
    t.sleep(0.01)

j = r.choice('abcdefghijklmnopqrstuvwxyz')
while j!= 'd':
    j = r.choice('abcdefghijklmnopqrstuvwxyz')
    if j == 'd':
        z += j
        print(z)
        break
    t.sleep(0.01)

k = r.choice('!@#$%^&*()_+-=[]|\:;\<>?,./')
while k!= '!':
    k = r.choice('!@#$%^&*()_+-=[]|\:;\<>?,./')
    if k == '!':
        z += k
        print(z)
        break
    z += k
    print(z)
    z = z[:-1]
    t.sleep(0.01)
