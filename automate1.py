from pywinauto.application import Application

ppWin = Application(backend='uia').connect(title='Purble Place', timeout=100)

ppWin.PurblePlace.print_control_Identifiers()