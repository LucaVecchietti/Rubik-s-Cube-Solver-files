#from RubikSolver_alg import rubik_solver_function
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty, BooleanProperty, ColorProperty, ObjectProperty
from kivy.uix.popup import Popup


"""
This is the file python for the GUI of this program and it is connected
to a file kivy(.kv) with the same name.
In this file I wrote the function to change the color of the squares
of the Rubik's cube.
Each button is connected to a function that changes the value of
the BooleanObject from False to True and opens a Popup. 
Depending on the color you have selected from the Popup, the pressed button 
changes color because the program changes the color of all buttons 
with True value. 
"""





alg = " "   #String of the algorithm for the resolution


class ColorPopup(Popup):                    #Popup for color selection
    change_color = ObjectProperty(None)
    white_button = ObjectProperty(None)
    blue_button = ObjectProperty(None)
    red_button = ObjectProperty(None)
    green_button = ObjectProperty(None)
    orange_button = ObjectProperty(None)
    yellow_button = ObjectProperty(None)




class MainRubikWindow(PageLayout):  #Main Window
    color = ColorProperty()   # Color property used to change color
    alg = StringProperty(alg)    # String property used to output the resolution algorithm
    # face1 buttons (face1_button4 is always white)
    bool_face1_0 = BooleanProperty(False)
    bool_face1_1 = BooleanProperty(False)
    bool_face1_2 = BooleanProperty(False)
    bool_face1_3 = BooleanProperty(False)
    bool_face1_5 = BooleanProperty(False)
    bool_face1_6 = BooleanProperty(False)
    bool_face1_7 = BooleanProperty(False)
    bool_face1_8 = BooleanProperty(False)
    # face2 buttons
    bool_face2_0 = BooleanProperty(False)
    bool_face2_1 = BooleanProperty(False)
    bool_face2_2 = BooleanProperty(False)
    bool_face2_3 = BooleanProperty(False)
    bool_face2_4 = BooleanProperty(False)
    bool_face2_5 = BooleanProperty(False)
    bool_face2_6 = BooleanProperty(False)
    bool_face2_7 = BooleanProperty(False)
    bool_face2_8 = BooleanProperty(False)
    # face3 buttons
    bool_face3_0 = BooleanProperty(False)
    bool_face3_1 = BooleanProperty(False)
    bool_face3_2 = BooleanProperty(False)
    bool_face3_3 = BooleanProperty(False)
    bool_face3_4 = BooleanProperty(False)
    bool_face3_5 = BooleanProperty(False)
    bool_face3_6 = BooleanProperty(False)
    bool_face3_7 = BooleanProperty(False)
    bool_face3_8 = BooleanProperty(False)
    # face4 buttons
    bool_face4_0 = BooleanProperty(None)
    bool_face4_1 = BooleanProperty(None)
    bool_face4_2 = BooleanProperty(None)
    bool_face4_3 = BooleanProperty(None)
    bool_face4_4 = BooleanProperty(None)
    bool_face4_5 = BooleanProperty(None)
    bool_face4_6 = BooleanProperty(None)
    bool_face4_7 = BooleanProperty(None)
    bool_face4_8 = BooleanProperty(None)

    # The functions connected to the buttons
    def face1_0_cliked(self):
        print("Button Face1_0 Cliked!!!")
        self.bool_face1_0 = True


    def face1_1_cliked(self):
        print("Button Face1_1 Cliked!!!")
        self.bool_face1_1 = True


    def face1_2_cliked(self):
        print("Button Face1_2 Cliked!!!")
        self.bool_face1_2 = True


    def face1_3_cliked(self):
        print("Button Face1_3 Cliked!!!")
        self.bool_face1_3 = True


    def face1_5_cliked(self):
        print("Button Face1_5 Cliked!!!")
        self.bool_face1_5 = True


    def face1_6_cliked(self):
        print("Button Face1_6 Cliked!!!")
        self.bool_face1_6 = True


    def face1_7_cliked(self):
        print("Button Face1_7 Cliked!!!")
        self.bool_face1_7 = True


    def face1_8_cliked(self):
        print("Button Face1_8 Cliked!!!")
        self.bool_face1_8 = True


    def face2_0_cliked(self):
        print("Button Face2_0 Cliked!!!")
        self.bool_face2_0 = True


    def face2_1_cliked(self):
        print("Button Face2_1 Cliked!!!")
        self.bool_face2_1 = True


    def face2_2_cliked(self):
        print("Button Face2_2 Cliked!!!")
        self.bool_face2_2 = True


    def face2_3_cliked(self):
        print("Button Face2_3 Cliked!!!")
        self.bool_face2_3 = True


    def face2_4_cliked(self):
        print("Button Face2_4 Cliked!!!")
        self.bool_face2_4 = True


    def face2_5_cliked(self):
        print("Button Face2_5 Cliked!!!")
        self.bool_face2_5 = True


    def face2_6_cliked(self):
        print("Button Face2_6 Cliked!!!")
        self.bool_face2_6 = True


    def face2_7_cliked(self):
        print("Button Face2_7 Cliked!!!")
        self.bool_face2_7 = True


    def face2_8_cliked(self):
        print("Button Face2_8 Cliked!!!")
        self.bool_face2_8 = True


    def face3_0_cliked(self):
        print("Button Face3_0 Cliked!!!")
        self.bool_face3_0 = True


    def face3_1_cliked(self):
        print("Button Face3_1 Cliked!!!")
        self.bool_face3_1 = True


    def face3_2_cliked(self):
        print("Button Face3_2 Cliked!!!")
        self.bool_face3_2 = True


    def face3_3_cliked(self):
        print("Button Face3_3 Cliked!!!")
        self.bool_face3_3 = True


    def face3_4_cliked(self):
        print("Button Face3_4 Cliked!!!")
        self.bool_face3_4 = True


    def face3_5_cliked(self):
        print("Button Face3_5 Cliked!!!")
        self.bool_face3_5 = True


    def face3_6_cliked(self):
        print("Button Face3_6 Cliked!!!")
        self.bool_face3_6 = True


    def face3_7_cliked(self):
        print("Button Face3_7 Cliked!!!")
        self.bool_face3_7 = True


    def face3_8_cliked(self):
        print("Button Face3_8 Cliked!!!")
        self.bool_face3_8 = True


    def face4_0_cliked(self):
        print("Button Face4_0 Cliked!!!")
        self.bool_face4_0 =True


    def face4_1_cliked(self):
        print("Button Face4_1 Cliked!!!")
        self.bool_face4_1 = True


    def face4_2_cliked(self):
        print("Button Face4_2 Cliked!!!")
        self.bool_face4_2 = True


    def face4_3_cliked(self):
        print("Button Face4_3 Cliked!!!")
        self.bool_face4_3 = True


    def face4_4_cliked(self):
        print("Button Face4_4 Cliked!!!")
        self.bool_face4_4 = True


    def face4_5_cliked(self):
        print("Button Face4_5 Cliked!!!")
        self.bool_face4_5 = True


    def face4_6_cliked(self):
        print("Button Face4_6 Cliked!!!")
        self.bool_face4_6 = True


    def face4_7_cliked(self):
        print("Button Face4_7 Cliked!!!")
        self.bool_face4_7 = True


    def face4_8_cliked(self):
        print("Button Face4_8 Cliked!!!")
        self.bool_face4_8 = True


    def face5_0_cliked(self):
        print("Button Face5_0 Cliked!!!")


    def face5_1_cliked(self):
        print("Button Face5_1 Cliked!!!")


    def face5_2_cliked(self):
        print("Button Face5_2 Cliked!!!")


    def face5_3_cliked(self):
        print("Button Face5_3 Cliked!!!")


    def face5_4_cliked(self):
        print("Button Face5_4 Cliked!!!")


    def face5_5_cliked(self):
        print("Button Face5_5 Cliked!!!")


    def face5_6_cliked(self):
        print("Button Face5_6 Cliked!!!")


    def face5_7_cliked(self):
        print("Button Face5_7 Cliked!!!")


    def face5_8_cliked(self):
        print("Button Face5_8 Cliked!!!")


    def face6_0_cliked(self):
        print("Button Face6_0 Cliked!!!")


    def face6_1_cliked(self):
        print("Button Face6_1 Cliked!!!")


    def face6_2_cliked(self):
        print("Button Face6_2 Cliked!!!")


    def face6_3_cliked(self):
        print("Button Face6_3 Cliked!!!")


    def face6_4_cliked(self):
        print("Button Face6_4 Cliked!!!")

    def face6_5_cliked(self):
        print("Button Face6_5 Cliked!!!")


    def face6_6_cliked(self):
        print("Button Face6_6 Cliked!!!")


    def face6_7_cliked(self):
        print("Button Face6_7 Cliked!!!")


    def face6_8_cliked(self):
        print("Button Face6_8 Cliked!!!")

    # Function for the color selection

    def color_selection(self):
        self.color_popup = ColorPopup(
            title="Choose The Color",
            white_button=self.white_button,
            blue_button=self.blue_button,
            red_button=self.red_button,
            green_button=self.green_button,
            orange_button=self.orange_button,
            yellow_button=self.yellow_button,
            change_color=self.change_color,
        )
        self.color_popup.open()

    def white_button(self):
        print("white_button cliked!")
        self.color = (255, 255, 255, 1)
        print(self.color)

    def blue_button(self):
        print("blue_button cliked!")
        self.color = (0, 0, 255, 1)
        print(self.color)

    def red_button(self):
        print("white_button cliked!")
        self.color = (255, 0, 0, 1)
        print(self.color)

    def green_button(self):
        print("blue_button cliked!")
        self.color = (0, 255, 0, 1)
        print(self.color)

    def orange_button(self):
        print("white_button cliked!")
        self.color = (255, .7, 0, 1)
        print(self.color)

    def yellow_button(self):
        print("blue_button cliked!")
        self.color = (255, 255, .2, 1)
        print(self.color)

    def change_color(self):
        if self.bool_face1_0 == True:
            self.ids.face1_button0.background_color = self.color
            self.bool_face1_0 = False
            print("OK Face1_0")
        elif self.bool_face1_1 == True:
            self.ids.face1_button1.background_color = self.color
            self.bool_face1_1 = False
            print("OK Face1_1")
        elif self.bool_face1_2 == True:
            self.ids.face1_button2.background_color = self.color
            self.bool_face1_2 = False
            print("OK Face1_2")
        elif self.bool_face1_3 == True:
            self.ids.face1_button3.background_color = self.color
            self.bool_face1_3 = False
            print("OK Face1_3")
        elif self.bool_face1_5 == True:
            self.ids.face1_button5.background_color = self.color
            self.bool_face1_5 = False
            print("OK Face1_5")
        elif self.bool_face1_6 == True:
            self.ids.face1_button6.background_color = self.color
            self.bool_face1_6 = False
            print("OK Face1_6")
        elif self.bool_face1_7 == True:
            self.ids.face1_button7.background_color = self.color
            self.bool_face1_7 = False
            print("OK Face1_7")
        elif self.bool_face1_8 == True:
            self.ids.face1_button8.background_color = self.color
            self.bool_face1_8 = False
            print("OK Face1_8")


        elif self.bool_face2_0 == True:
            self.ids.face2_button0.background_color = self.color
            self.bool_face2_0 = False
            print("OK Face2_0")
        elif self.bool_face2_1 == True:
            self.ids.face2_button1.background_color = self.color
            self.bool_face2_1 = False
            print("OK Face2_1")
        elif self.bool_face2_2 == True:
            self.ids.face2_button2.background_color = self.color
            self.bool_face2_2 = False
            print("OK Face2_2")
        elif self.bool_face2_3 == True:
            self.ids.face2_button3.background_color = self.color
            self.bool_face2_3 = False
            print("OK Face2_3")
        elif self.bool_face2_4 == True:
            self.ids.face2_button4.background_color = self.color
            self.bool_face2_4 = False
            print("OK Face2_4")
        elif self.bool_face2_5 == True:
            self.ids.face2_button5.background_color = self.color
            self.bool_face2_5 = False
            print("OK Face2_5")
        elif self.bool_face2_6 == True:
            self.ids.face2_button6.background_color = self.color
            self.bool_face2_6 = False
            print("OK Face2_6")
        elif self.bool_face2_7 == True:
            self.ids.face2_button7.background_color = self.color
            self.bool_face2_7 = False
            print("OK Face2_7")
        elif self.bool_face2_8 == True:
            self.ids.face2_button8.background_color = self.color
            self.bool_face2_8 = False
            print("OK Face2_8")


        elif self.bool_face3_0 == True:
            self.ids.face3_button0.background_color = self.color
            self.bool_face3_0 = False
            print("OK Face3_0")
        elif self.bool_face3_1 == True:
            self.ids.face3_button1.background_color = self.color
            self.bool_face3_1 = False
            print("OK Face3_1")
        elif self.bool_face3_2 == True:
            self.ids.face3_button2.background_color = self.color
            self.bool_face3_2 = False
            print("OK Face3_2")
        elif self.bool_face3_3 == True:
            self.ids.face3_button3.background_color = self.color
            self.bool_face3_3 = False
            print("OK Face3_3")
        elif self.bool_face3_4 == True:
            self.ids.face3_button4.background_color = self.color
            self.bool_face3_4 = False
            print("OK Face3_4")
        elif self.bool_face3_5 == True:
            self.ids.face3_button5.background_color = self.color
            self.bool_face3_5 = False
            print("OK Face3_5")
        elif self.bool_face3_6 == True:
            self.ids.face3_button6.background_color = self.color
            self.bool_face3_6 = False
            print("OK Face3_6")
        elif self.bool_face3_7 == True:
            self.ids.face3_button7.background_color = self.color
            self.bool_face3_7 = False
            print("OK Face3_7")
        elif self.bool_face3_8 == True:
            self.ids.face3_button8.background_color = self.color
            self.bool_face3_8 = False
            print("OK Face3_8")


        elif self.bool_face4_0 == True:
            self.ids.face4_button0.background_color = self.color
            self.bool_face4_0 = False
            print("OK Face4_0")
        elif self.bool_face4_1 == True:
            self.ids.face4_button1.background_color = self.color
            self.bool_face4_1 = False
            print("OK Face4_1")
        elif self.bool_face4_2 == True:
            self.ids.face4_button2.background_color = self.color
            self.bool_face4_2 = False
            print("OK Face4_2")
        elif self.bool_face4_3 == True:
            self.ids.face4_button3.background_color = self.color
            self.bool_face4_3 = False
            print("OK Face4_3")
        elif self.bool_face4_4 == True:
            self.ids.face4_button4.background_color = self.color
            self.bool_face4_4 = False
            print("OK Face4_4")
        elif self.bool_face4_5 == True:
            self.ids.face4_button5.background_color = self.color
            self.bool_face4_5 = False
            print("OK Face4_5")
        elif self.bool_face4_6 == True:
            self.ids.face4_button6.background_color = self.color
            self.bool_face4_6 = False
            print("OK Face4_6")
        elif self.bool_face4_7 == True:
            self.ids.face4_button7.background_color = self.color
            self.bool_face4_7 = False
            print("OK Face4_7")
        elif self.bool_face4_8 == True:
            self.ids.face4_button8.background_color = self.color
            self.bool_face4_8 = False
            print("OK Face4_8")

        print(self.color)
        print("ok")


class RubikSolver_guiApp(App):
    def build (self):
        return MainRubikWindow()

rubik_app = RubikSolver_guiApp()
rubik_app.run()