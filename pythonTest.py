print('Hallo Welt!')
name = 'Julia'
b = "b"
print("b is 'b'")
print('Is it true that 4 is greater than the length of b?')
print(4 > len(b))
print('Is it false that 237 is smaller than 397 and that 5 is not 5?')
print(not (237 < 397 and 5 !=5))
a = True
print('Is it true that a equals True and the length of b is greater than 0?')
print(a and len(b)>0)
if 3 > 2 :
    print("It works!")
    print('Erfolg')
else :
    print("The author's name is " + name)
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
    if 40 <= volume < 60:
        print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
# Dies ist ein Kommentar!
def hi():
    print('Hi there!')
    print('How are you?')
hi()
def hey(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hey('Sonja')
hi()
hey('Woah')
name = 'Julia'
def huhu(name):
        print('Huhu ' + name + '!')
huhu(name)