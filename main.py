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

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(QuestionsScreen(name='questions'))

class MainApp(MDApp):
    def build(self):
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