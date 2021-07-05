from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import  MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from style import KV

# MDFloatLayout:
#     radius: [25, 0, 0, 0]
#     md_bg_color: app.theme_cls.primary_color

#     MDToolbar:
#         title: "MDToolbar"

#     MDRectangleFlatButton:
#         text: "Hello Baldo"
#         halign: "center"


class MenuScreen(Screen):
    pass

class QuestionsScreen(Screen):
    pass

class Question1Screen(Screen):
    pass

class Question2Screen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(QuestionsScreen(name='questions'))
sm.add_widget(Question1Screen(name='question1'))
sm.add_widget(Question2Screen(name='question2'))


class MainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"       
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.primary_hue = "200"  # "500" 
        return Builder.load_string(KV)

        # self.theme_cls.primary_palette = 'Green'
        # screen = Screen()
        # screen.add_widget(
        #         MDRectangleFlatButton(
        #             text='Hello, Baldo!',
        #             pos_hint={"center_x": 0.5, "center_y": 0.5},
        #     )
        # )
        # return screen

MainApp().run()