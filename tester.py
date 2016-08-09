# from PIL import Image                                                                                
# img = Image.open('winnerscreen.gif')
# img.show() 
# img = Image.open('winnerscreen2.gif')
# img.show() 



# from PIL import Image
# with Image.open('/Users/vivek/Desktop/happyface.jpg') as img:
#     #img.show()

# from PIL import Image
# from PIL import ImageSequence
# img = Image.open('winner.gif')
# # im.seek(0) # skip to the second frame
# img.seek(1)
# # im.seek(2)
# while 1:
#     img.seek(img.tell()+1)

# for frame in ImageSequence.Iterator(img):
#     img.seek(frame) # ...do something to frame...

# import os
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111)
# plt.ion()
# plt.show()

# dir = '/Users/vivek/Desktop/cs10final/winner.gif'

# for fname in os.listdir(dir):
#     fname = os.path.join(dir, fname)
#     im = plt.imread(fname)
#     img = ax.imshow(im)
#     plt.draw()
#     accept = raw_input('OK? ')

import turtle as t
def s():
	t.bgpic("looserscreen.gif")
def s1():
	t.bgpic("looserscreen2.gif")
def s2():
	t.bgpic("looserscreen3.gif")
def s3():
	t.bgpic("looserscreen4.gif")

import time

t.ontimer(s, 0)
t.ontimer(s1, 900)
t.ontimer(s2, 1800)
t.ontimer(s3, 2700)
t.ontimer(s, 3600)

# t.bgpic("looserscreen2.gif")
# time.sleep(10)
# 
# time.sleep(10)
# t.bgpic("looserscreen4.gif")













