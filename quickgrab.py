from PIL import ImageGrab
import os
import time
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
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
