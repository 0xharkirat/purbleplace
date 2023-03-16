import pyautogui, time, os


import sys

# Get the selected options from the command line arguments
selected_options = sys.argv[1:]


class Cake():
    def __init__(self, shape, fill, top, cherry):
        self.SHAPE = shape
        self.FILL = fill
        self.TOP = top
        self.CHERRY = cherry

class DoubleCake(Cake):
    def __init__(self, shape, fill, sheet, secFill, top, cherry): 
        super().__init__(shape, fill, top, cherry)
        self.SHEET = sheet
        self.SECFILL = secFill


class TripleCake(DoubleCake):
    def __init__(self, shape, fill, sheet, secFill, secSheet, thirdfill, top, cherry, toppings):
        super().__init__(shape, fill, sheet, secFill, top, cherry)
        self.SECSHEET = secSheet
        self.THIRDFILL = thirdfill
        self.TOPPINGS = toppings
    


GAME_REGION = ()
    

class Easy:

    # coordinates
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
    
    def __init__(self, selectedOptions):
        self.Cake = Cake(selectedOptions[0], selectedOptions[1], selectedOptions[2], selectedOptions[3])

    def selectedShape(self):
        if self.Cake.SHAPE == 'Round':
            return self.CIRCLE_COORD
        elif self.Cake.SHAPE == 'Square':
            return self.BOX_COORD
        elif self.Cake.SHAPE == 'Heart':
            return self.BASE_HEART_COORD
        else:
            raise Exception('Base Number out of range. Select only from (Cicle, Square, Heart)')

    def selectedFill(self):
        if self.Cake.FILL == 'Choc':
            return self.CHOCFILL_COORD
        elif self.Cake.FILL == 'Pink':
            return self.PINKFILL_COORD
        elif self.Cake.FILL == 'Yellow':
            return self.YELLOWFILL_COORD
        else:
            raise Exception('Fill Number out of range. Select only from (CHoc, Pink, Yellow)')
        
    def selectedTop(self):
        if self.Cake.TOP == 'Choc':
            return self.CHOCTOP_COORD
        elif self.Cake.TOP == 'Pink':
            return self.PINKTOP_COORD
        elif self.Cake.TOP == 'Yellow':
            return self.YELLOWTOP_COORD
        else:
            raise Exception('Top Number out of range. Select only from (CHoc, Pink, Yellow)')
        
    def selectedCherry(self):
        if self.Cake.CHERRY == 'Triple':
            return self.CHERRY_COORD
        elif self.Cake.CHERRY == 'Smiley':
            return self.SMILEY_COORD
        elif self.Cake.CHERRY == 'Heart':
            return self.HEART_COORD
        elif self.Cake.CHERRY == 'Leaf':
            return self.LEAF_COORD


    def moveToRight(self):
        pyautogui.moveTo(self.RIGHT_COORD)
        pyautogui.doubleClick()
        time.sleep(0.5)

    
    def startBaking(self):

        # make base
        pyautogui.moveTo(self.selectedShape())
        pyautogui.doubleClick()

         # moveNext
        self.moveToRight()

    
        # fill base
        pyautogui.moveTo(self.selectedFill())
        pyautogui.doubleClick()

         # moveNext
        self.moveToRight()

        # put top
        pyautogui.moveTo(self.selectedTop())
        pyautogui.doubleClick()

         # moveNext
        self.moveToRight()

        # put cherry
        pyautogui.moveTo(self.selectedCherry())
        pyautogui.doubleClick()

        # moveNext
        self.moveToRight()
        self.moveToRight()

class Intermediate(Easy):

    # coordinates
    CIRCLE_COORD = (134,603)
    BOX_COORD = (133,646)
    BASE_HEART_COORD = (129,691)
    CHOCFILL_COORD = (254,603)
    PINKFILL_COORD = (254,655)
    YELLOWFILL_COORD = (254,687)
    CHOCSHEET_COORD = (379,605)
    GREENSHEET_COORD = (379,643)
    WHITESHEET_COORD = (379,688)

    def __init__(self, selectedOptions):
        self.Cake= DoubleCake(shape=selectedOptions[0], fill=selectedOptions[1], sheet=selectedOptions[2], secFill=selectedOptions[3], top=selectedOptions[4], cherry=selectedOptions[5])
        self.position = int(selectedOptions[6])



    def selectedSheet(self):
        if self.Cake.SHEET == 'Brown':
            return self.CHOCSHEET_COORD
        elif self.Cake.SHEET == 'Green':
            return self.GREENSHEET_COORD
        elif self.Cake.SHEET == 'White':
            return self.WHITESHEET_COORD
        else:
            raise Exception("Sheet number out of range, select only from (Brown, Green, white)")
        
    def selectedSecondFill(self):
        if self.Cake.SECFILL == 'Choc':
            return self.CHOCFILL_COORD
        elif self.Cake.SECFILL == 'Pink':
            return self.PINKFILL_COORD
        elif self.Cake.SECFILL == 'Yellow':
            return self.YELLOWFILL_COORD
        else:
            raise Exception('Fill Number out of range. Select only from (CHoc, Pink, Yellow)')
        
    def moveToLeft(self):
        pyautogui.moveTo(self.LEFT_COORD)
        pyautogui.doubleClick()
        time.sleep(0.5)

        
    def startBaking(self):

        for i in range(self.position - 1):
            self.moveToLeft()


        self.position *= 2
        pyautogui.moveTo(self.selectedShape())
        pyautogui.doubleClick()

         # moveNext
        self.moveToRight()

    
        # fill base
        pyautogui.moveTo(self.selectedFill())
        pyautogui.doubleClick()

         # moveNext
        self.moveToRight()

        # sheet
        pyautogui.moveTo(self.selectedSheet())
        pyautogui.doubleClick()

        # move back two
        self.moveToLeft()
        self.moveToLeft()

        # second shape
        pyautogui.moveTo(self.selectedShape())
        pyautogui.doubleClick()

         # moveNext
        self.moveToRight()

    
        # fill second base
        pyautogui.moveTo(self.selectedSecondFill())
        pyautogui.doubleClick()

        # two right moves
        self.moveToRight()
        self.moveToRight()

        # put top
        pyautogui.moveTo(self.selectedTop())
        pyautogui.doubleClick()

         # moveNext
        self.moveToRight()

        # put cherry
        pyautogui.moveTo(self.selectedCherry())
        pyautogui.doubleClick()

        # moveNext
        self.moveToRight()
        self.moveToRight()

    def twoAtATime(self):
        for i in range(4):
            self.moveToLeft()

        pyautogui.moveTo(self.selectedShape())
        pyautogui.doubleClick()

        self.moveToRight()

        pyautogui.moveTo(self.selectedFill())
        pyautogui.doubleClick()

        self.moveToRight()

        pyautogui.moveTo(self.selectedSheet())
        pyautogui.doubleClick()
        pyautogui.moveTo(self.selectedShape())
        pyautogui.doubleClick()

        for i in range(2):
            self.moveToLeft()

        pyautogui.moveTo(self.selectedShape())
        pyautogui.doubleClick()

        self.moveToRight()

        pyautogui.moveTo(self.selectedSecondFill())
        pyautogui.doubleClick()

        self.moveToRight()

        pyautogui.moveTo(self.selectedFill())
        pyautogui.doubleClick()

        self.moveToRight()

        pyautogui.moveTo(self.selectedTop())
        pyautogui.doubleClick()
        pyautogui.moveTo(self.selectedSheet())
        pyautogui.doubleClick()

        for i in range(2):
            self.moveToLeft()

        pyautogui.moveTo(self.selectedShape())
        pyautogui.doubleClick()
        
        self.moveToRight()

        pyautogui.moveTo(self.selectedSecondFill())
        pyautogui.doubleClick()

        self.moveToRight()
        self.moveToRight()

        pyautogui.moveTo(self.selectedCherry())
        pyautogui.doubleClick()
        pyautogui.moveTo(self.selectedTop())
        pyautogui.doubleClick()

        self.moveToRight()

        pyautogui.moveTo(self.selectedCherry())
        pyautogui.doubleClick()

        self.moveToRight()
        time.sleep(1.25)
        self.moveToRight()


        






def main():

    game = None

    if len(selected_options) == 4:
        # Easy game
        
        game = Easy(selectedOptions=selected_options)

    elif len(selected_options) == 7:
        game = Intermediate(selectedOptions=selected_options)
        
    for i in range(5):
        if i < 3:
            game.startBaking()
        else:
            game.twoAtATime()
            break
    
    
main()

    
