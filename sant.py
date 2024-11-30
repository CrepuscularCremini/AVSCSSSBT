import os
from random import shuffle, choices
import string

os.chdir(r"c:\users\brenn\Desktop\SecretSanta")

html = """
<!DOCTYPE html>
<html>
  <head>
    <title>A Letter from Sant</title>
    <link rel="stylesheet" href="secret.css">
  </head>

  <body>
    <div class="typewriter">
      <h1>Dear {person_one},</h1>
      <br>
      <p>I cordially invite you to partake in the most secret of traditions, the Sant. On this most joyous of eves, we shall imbibe, and we shall gift.</p>
      <br>
      <p>Your person is:</p>
      <h1>{person_two}</h1>
      <br>
      <p>A quick reminder that you should bring (a) a gift for your special someone of a max of $20 and (b) a beer (perchance two so we can try a wee more) that embodies that absolute and true essance of your soul, or, just a beer you like. We shall do flights of the beers and a classic lil swappy boi for the Sant.</p>
      <br>
      <h1>With love and joy,<h1>
      <h1>Sant</h1>
    </div>
  </body>
</html>
"""

##

names = ['one', 'two', 'three', 'four']

def shuffle_check(n, r):
    rv = False
    for i in range(len(n)):
        if n[i] == r[i]:
            rv = True
    return rv

recips = names.copy()

sc = True
while sc:
    shuffle(recips)
    sc = shuffle_check(names, recips)

print(names, recips)

##

for person_one, person_two in zip(names, recips):
    rstring = ''.join(choices(string.ascii_letters, k = 5))
    with open(f"Letters/{person_one}{rstring}.html", 'w') as html_file:
        html_file.write(html.format(person_one = person_one, person_two = person_two))