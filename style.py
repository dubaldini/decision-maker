KV = '''
ScreenManager:
    MenuScreen:
    QuestionsScreen:
    Question1Screen:
    Question2Screen:

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
        on_press: root.manager.current = 'question1'

<Question1Screen>:
    name: 'question1'
    MDLabel:
        text:  'Você gosta e se sente bem/confortável com as pessoas que estão envolvidas nessa decisão?'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Sim'
        pos_hint: {'center_x':0.25, 'center_y':0.2}
        on_press: root.manager.current = 'question2'

    MDRectangleFlatButton:
        text: 'Não'
        pos_hint: {'center_x':0.75, 'center_y':0.2}
        on_press: root.manager.current = 'question2'

    MDRectangleFlatButton:
        text: 'Não se aplica'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question2'

<Question2Screen>:
    name: 'question2'
    MDLabel:
        text:  'Uma situação igual ou parecida a essa já aconteceu no passado? Avalie como foi de ótima a péssima.'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Ótima'
        pos_hint: {'center_x':0.20, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

    MDRectangleFlatButton:
        text: 'Boa'
        pos_hint: {'center_x':0.35, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

    MDRectangleFlatButton:
        text: 'Média'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

    MDRectangleFlatButton:
        text: 'Ruim'
        pos_hint: {'center_x':0.65, 'center_y':0.2}
        on_press: root.manager.current = 'menu'
    
    MDRectangleFlatButton:
        text: 'Péssima'
        pos_hint: {'center_x':0.80, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<Question3Screen>:
    name: 'question3'
    MDLabel:
        text:  
        halign: 'center'

'''