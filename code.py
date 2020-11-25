from PIL import ImageGrab
import os
import time
import win32api, win32con
from PIL import ImageOps
from numpy import *

'''
Chrome maximised with bookmarks tab enabled.
scroll down button hit 11 times to centre the play area
top left=(301,223)
bottom right=(1101,823)

'''
x_pad=300
y_pad=222
 
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+801,y_pad+601)
    im = ImageGrab.grab(box)
    '''im.save(os.getcwd() + '\\full_snap__' + str(int(time.time()))+'.png', 'PNG')'''
    return im

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click.")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')


     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y )
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

class Cord:
     
    f_shrimp = (-23,301)
    f_rice = (32,286)
    f_nori = (-27,348)
    f_roe = (28,351)
    f_salmon = (-26,405)
    f_unagi = (34,407)

    phone=(522,310)

    menu_toppings=(470,230)
    menu_rice=(470,252)

    t_shrimp = (450,180)
    t_nori = (505,176)
    t_roe = (426,232)
    t_salmon = (518,232)
    t_unagi = (426,285)
    t_exit = (534,291)

    buy_rice=(481,235)
    delivery_norm=(429,256)

sushiTypes = {2333:'onigiri',2269:'onigiri',2397:'onigiri', 
              2851:'caliroll',3105:'caliroll',2987:'caliroll',
              2466:'gunkan',2499:'gunkan',2212:'gunkan'}
class Blank:
    seat_1 = 7520
    seat_2 = 6116
    seat_3 = 10738
    seat_4 = 10343
    seat_5 = 6578
    seat_6 = 9426

def makeFood(food):
    if food=='caliroll':
        print('making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print('Making a onigiri')
        foodOnHand['rice'] -= 2 
        foodOnHand['nori'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print('Making a gunkan')
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
def foldMat():
    mousePos((Cord.f_rice[0]+45,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)
    
def clear_tables():
    mousePos((20,160))
    leftClick()

    mousePos((126,160))
    leftClick()

    mousePos((221,160))
    leftClick()

    mousePos((322,160))
    leftClick()

    mousePos((426,160))
    leftClick()

    mousePos((522,160))
    leftClick()

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print ('%s is low and needs to be replenished' , i)
                buyFood(i)    
    
def buyFood(food):

    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel(Cord.buy_rice) != (255, 255, 255):
            print ('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            

            
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (0, 153, 255):
            print( 'nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)


    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (127, 127, 127):
            print ('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print( 'roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
	



    
     
    mousePos(Cord.phone)
     
    mousePos(Cord.menu_toppings)
     
     
    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)
     
    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)
     
    mousePos(Cord.delivery_norm)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def get_seat_one():
    box = (x_pad+34,y_pad+77,x_pad+34+76,y_pad+77+18)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_two():
    box = (x_pad+160,y_pad+77,x_pad+160+76,y_pad+77+18)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_three():
    box = (x_pad+286,y_pad+77,x_pad+286+76,y_pad+77+18)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_four():
    box = (x_pad+412,y_pad+77,x_pad+412+76,y_pad+77+18)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_five():
    box = (x_pad+538,y_pad+77,x_pad+538+76,y_pad+77+18)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (x_pad+665,y_pad+77,x_pad+665+76,y_pad+77+18)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

def startGame():
    #location of first menu
    mousePos((254, 163))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((269, 344))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((522, 413))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((357, 332))
    leftClick()
    time.sleep(.1)
    
def check_bubs():
 
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print ('table 1 is occupied and needs %s' ,sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print ('sushi not found!\n sushiType = %i' ,s1)
 
    else:
        print ('Table 1 unoccupied')
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print ('table 2 is occupied and needs %s' , sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print ('sushi not found!\n sushiType = %i' , s2)
 
    else:
        print ('Table 2 unoccupied')
    clear_tables() 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print ('table 3 is occupied and needs %s', sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print ('sushi not found!\n sushiType = %i',s3)
 
    else:
        print ('Table 3 unoccupied')
    clear_tables() 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print ('table 4 is occupied and needs %s' ,sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print ('sushi not found!\n sushiType = %i', s4)
 
    else:
        print ('Table 4 unoccupied')
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print ('table 5 is occupied and needs %s' ,sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print ('sushi not found!\n sushiType = %i', s5)
 
    else:
        print ('Table 5 unoccupied')
    clear_tables() 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print ('table 1 is occupied and needs %s' ,sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print ('sushi not found!\n sushiType = %i',s6)
 
    else:
        print ('Table 6 unoccupied')
 
    clear_tables()    

                          
 
def main():
    startGame()
    for i in range(10):
        check_bubs()
        
    
 
if __name__ == '__main__':
    main()

