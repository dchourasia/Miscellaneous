import random, itertools

smalls = [chr(n) for n in range(97, 123)]
caps = [chr(n) for n in range(65, 91)]
ints = [str(n) for n in range(0, 10)]
specials = [chr(n) for n in itertools.chain(range(33, 47), range(58, 65), range(91, 97), range(123, 127))]

#print(smalls, caps, specials)

# all = [(n, chr(n)) for n in range(1, 150)]
#print(all)
# caps 65 to 90
# smalls 97 to 122
# specials 33 to 46, 58 to 64, 91 to 96, 123 to 126

passwd = random.choices(smalls, k=3) + random.choices(caps, k=3) + random.choices(ints, k=3) + random.choices(specials, k=3)

random.shuffle(passwd)
print(''.join(passwd))