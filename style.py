KV = '''
ScreenManager:
    MenuScreen:
    QuestionsScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Menu Screen'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'questions'

<QuestionsScreen>:
    name: 'questions'
    MDLabel:
        text:  'Hello, Baldo'
        halign: 'center'


    MDRectangleFlatButton:
        text: 'Questions Screen'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

'''