from Adafruit_LED_Backpack import BicolorMatrix8x8
from PIL import Image,ImageDraw
import signal,time,sox,random
from gpiozero import Button
import subprocess as sp

left = BicolorMatrix8x8.BicolorMatrix8x8()
right = BicolorMatrix8x8.BicolorMatrix8x8(address=0x72)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
COLOURS = [RED, GREEN, YELLOW]
left.begin()
right.begin()
button = Button(5)
global reinpro
global plinpro
plinpro=False
reinpro=False

def recordit():
    global reinpro
    global plinpro
    print('hi')
    sp.Popen(['rm','/home/pi/test.wav'])
    sp.Popen(['rm','/home/pi/out.wav'])
    reinpro=True
    print('hello')
    sp.Popen(['arecord','-D','plughw:1','-d','5','-t','wav','/home/pi/test.wav'])
    time.sleep(6)
    tfm=sox.Transformer()
    tfm.pitch(10.0)
    tfm.pitch(1)
    plinpro=True
    reinpro=False
    tfm.build('/home/pi/test.wav','/home/pi/out.wav')
    sp.Popen(['aplay','-D','plughw:0','/home/pi/out.wav'])
    time.sleep(6)
    plinpro=False
    button.when_pressed = recordit

def both_eyes(image):
    left.set_image(image)
    right.set_image(image)
    left.write_display()
    right.write_display()

def eyes_off():
    right.clear()
    left.clear()
    left.write_display()
    right.write_display()

def eyes_centre():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    both_eyes(eye)

def eyes_colour():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    for x in range(random.randint(5,10)):
        d1.line((2,7,5,7), fill=random.choice(COLOURS))
        d1.line((2,0,5,0), fill=random.choice(COLOURS))
        d1.line((6,1,6,6), fill=random.choice(COLOURS))
        d1.line((1,1,1,6), fill=random.choice(COLOURS))
        both_eyes(eye)
        time.sleep(0.1248)
    
def eyes_wink():
    leye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(leye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    reye = Image.new('RGB',(8,8))
    d2 = ImageDraw.Draw(reye)
    d2.line((4,0,4,7), fill=RED)
    right.clear()
    left.clear()
    left.set_image(leye)
    right.set_image(reye)
    left.write_display()
    right.write_display()
    time.sleep(1)
    right.set_image(leye)
    right.write_display()

def eyes_blink():
    leye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(leye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    reye = Image.new('RGB',(8,8))
    d2 = ImageDraw.Draw(reye)
    d2.line((4,0,4,7), fill=RED)
    right.clear()
    left.clear()
    left.set_image(reye)
    right.set_image(reye)
    left.write_display()
    right.write_display()
    time.sleep(1)
    right.set_image(leye)
    left.set_image(leye)
    right.write_display()
    left.write_display()

def eyes_right():
    eyes_right = Image.new('RGB',
(8,8))
    d1 = ImageDraw.Draw(eyes_right)
    d1.rectangle((3,2,4,3),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    both_eyes(eyes_right)
    
def eyes_left():
    eyes_left = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eyes_left)
    d1.rectangle((3,4,4,5),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    both_eyes(eyes_left)


def eyes_wide():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((1,7,6,7), fill=RED)
    d1.line((1,0,6,0), fill=RED)
    d1.line((7,1,7,6), fill=RED)
    d1.line((0,1,0,6), fill=RED)
    both_eyes(eye)

def eyes_googly():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.line((1,7,6,7), fill=RED)
    d1.line((1,0,6,0), fill=RED)
    d1.line((7,1,7,6), fill=RED)
    d1.line((0,1,0,6), fill=RED)
    for x in range(20):

        offsetx = random.randint(-2,2)
        offsety = random.randint(-2,2)
        d1.rectangle((3+offsetx,3+offsety,4+offsetx,4+offsety),outline=(255,0,0))
        both_eyes(eye)
        time.sleep(0.2)
        d1.rectangle((1,1,6,6),outline=(0,0,0),fill=(0,0,0))
        both_eyes(eye)

def eyes_narrow():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((3,7,4,7), fill=RED)
    d1.line((3,0,4,0), fill=RED)
    d1.line((5,1,5,6), fill=RED)
    d1.line((2,1,2,6), fill=RED)
    both_eyes(eye)

def eyes_hypno(n):
    eyes_right = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eyes_right)
    
    for x in range(n):
        d1.rectangle((0,0,7,7),outline=COLOURS[x%3])
        d1.rectangle((1,1,6,6),outline=COLOURS[(x+1)%3])
        d1.rectangle((2,2,5,5),outline=COLOURS[(x+2)%3])
        d1.rectangle((3,3,4,4),outline=COLOURS[x%3])
        both_eyes(eyes_right)
        time.sleep(0.05)
        
def disco():
    disco=Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(disco)
    for b in range(random.randint(4,8)):
        for i in range(8):
            for y in range(8):
                d1.rectangle((i,y,i,y),fill=random.choice(COLOURS))
        time.sleep(0.1248)
        both_eyes(disco)
    
    
def random_eyes():
    global reinpro
    global plinpro
    r = random.randint(1,9)
    t = random.randint(int(1.24),int(1.84))
    if reinpro:
        eyes_hypno(93)
        while plinpro:
            print('sasauges')
            disco()
    elif r ==  1:
        eyes_centre()
        time.sleep(t)
    elif r == 2:
        eyes_left()
        time.sleep(t)
    elif r == 3:
        eyes_right()
        time.sleep(t)
    elif r == 4:
        eyes_colour()
    elif r == 5:
        eyes_narrow()
        time.sleep(t)
    elif r == 6:
        eyes_wide()
        time.sleep(t)
    elif r == 7:
        eyes_wink()
        time.sleep(t)
    elif r == 8:
        eyes_centre()
        time.sleep(t)
    elif r == 9:
         eyes_blink()
         time.sleep(t)
    print(r)
    if reinpro:
        print(':-)')
button.when_pressed = recordit
while True:
    random_eyes()
    
