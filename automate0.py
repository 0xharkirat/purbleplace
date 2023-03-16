import pyautogui, time, os


GAME_REGION = ()
BASE_HEART_COORD = (251,686)
BOX_COORD = (245,640)
CHERRY_COORD = (595,635)
CHOCFILL_COORD = (373,602)
CHOCTOP_COORD = (502,598)
CIRCLE_COORD = (249,598)
HEART_COORD = (633,628)
LEAF_COORD = (635,658)
LEFT_COORD = (239,740)
PINKFILL_COORD = (379,640)
PINKTOP_COORD = (496,640)
RIGHT_COORD = (324,740)
SMILEY_COORD = (590,667)
YELLOWFILL_COORD = (377,690)
YELLOWTOP_COORD = (500,690)

time.sleep(5)

def main():
    print('Program Started. Press Ctrl-C to abort at any time.')
    print('TO interrupt mouse movement, move mouse to upper left corner.')
    getGameRegion()

    startBaking()

def imPath(filename):
    return os.path.join('images', filename)

def getGameRegion():
    global GAME_REGION

    print('Finding game region...')
    region = pyautogui.locateOnScreen(imPath('input_area.png'), confidence=0.1)
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')
    
    # calculate the region of the entire game
    GAME_REGION = (region[0], region[1], region[2], region[3])
    print(f'Game region found: {GAME_REGION}')



def startBaking():

    cakes = 0

    # set the ingredients
    while cakes < 5:
        base = getBase(int(input('Enter the base Number (1,2,3): ')))
        fill = getFill(int(input('Enter the fill Number (1, 2, 3): ')))
        top = getTop(int(input('Enter the top number (1, 2, 3): ')))
        cherry = getCherry(int(input('Enter the cherry Number: ')))

        # make base
        pyautogui.moveTo(base)
        pyautogui.doubleClick()

        # moveNext
        moveToRight()

        
        # fill base
        pyautogui.moveTo(fill)
        pyautogui.doubleClick()

        # moveNext
        moveToRight()

        # put top
        pyautogui.moveTo(top)
        pyautogui.doubleClick()

        # moveNext
        moveToRight()

        # put cherry
        pyautogui.moveTo(cherry)
        pyautogui.doubleClick()

        # moveNext
        moveToRight()
        moveToRight()

        cakes += 1





    
def getBase(baseNumber):


    if baseNumber == 1:
        return CIRCLE_COORD
    elif baseNumber == 2:
        return BOX_COORD
    elif baseNumber == 3:
        return BASE_HEART_COORD
    else:
        raise Exception('Base Number out of range. Enter from (1, 2, 3)')

def getFill(fillNumber):
    if fillNumber == 1:
        return CHOCFILL_COORD
    elif fillNumber == 2:
        return PINKFILL_COORD
    elif fillNumber == 3:
        return YELLOWFILL_COORD
    else:
        raise Exception('Fill Number out of range. Enter from (1, 2, 3)')

def getTop(topNumber):
    if topNumber == 1:
        return CHOCTOP_COORD
    elif topNumber == 2:
        return PINKTOP_COORD
    elif topNumber == 3:
        return YELLOWTOP_COORD
    else:
        raise Exception('Top Number out of range. Enter from (1, 2, 3)')
    
def getCherry(cherryNumber):
    if cherryNumber == 1:
        return CHERRY_COORD
    elif cherryNumber == 2:
        return SMILEY_COORD
    elif cherryNumber == 3:
        return HEART_COORD
    elif cherryNumber == 4:
        return LEAF_COORD
    else:
        raise Exception('Cherry Number out of range. Enter from (1, 2, 3, 4)')

def moveToRight():
    pyautogui.moveTo(RIGHT_COORD)
    pyautogui.doubleClick()
    time.sleep(0.5)



main()

    
