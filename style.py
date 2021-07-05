KV = '''
ScreenManager:
    MenuScreen:
    QuestionsScreen:
    Question1Screen:
    Question2Screen:
    Question3Screen:
    Question4Screen:
    Question5Screen:
    Question6Screen:    
    Question7Screen:    

<MenuScreen>:
    name: 'menu'


    MDLabel:
        text: 'Welcome to Baldos Decision Maker App!'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Click Here to Access the Questions'
        pos_hint: {'center_x':0.50, 'center_y':0.25}
        on_press: root.manager.current = 'questions'

<QuestionsScreen>:
    name: 'questions'
    MDLabel:
        text:  'Prepare for the following questions...'
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
        text:  'questao2'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Ótima'
        pos_hint: {'center_x':0.20, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

    MDRectangleFlatButton:
        text: 'Boa'
        pos_hint: {'center_x':0.35, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

    MDRectangleFlatButton:
        text: 'Média'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

    MDRectangleFlatButton:
        text: 'Ruim'
        pos_hint: {'center_x':0.65, 'center_y':0.2}
        on_press: root.manager.current = 'question3'
    
    MDRectangleFlatButton:
        text: 'Péssima'
        pos_hint: {'center_x':0.80, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

<Question3Screen>:
    name: 'question3'
    MDLabel:
        text:  'questao3'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Ótima'
        pos_hint: {'center_x':0.20, 'center_y':0.2}
        on_press: root.manager.current = 'question4'

    MDRectangleFlatButton:
        text: 'Boa'
        pos_hint: {'center_x':0.35, 'center_y':0.2}
        on_press: root.manager.current = 'question4'

    MDRectangleFlatButton:
        text: 'Média'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question4'

    MDRectangleFlatButton:
        text: 'Ruim'
        pos_hint: {'center_x':0.65, 'center_y':0.2}
        on_press: root.manager.current = 'question4'
    
    MDRectangleFlatButton:
        text: 'Péssima'
        pos_hint: {'center_x':0.80, 'center_y':0.2}
        on_press: root.manager.current = 'question4'


<Question4Screen>:
    name: 'question4'
    MDLabel:
        text:  'questao 4'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Ótima'
        pos_hint: {'center_x':0.20, 'center_y':0.2}
        on_press: root.manager.current = 'question5'

    MDRectangleFlatButton:
        text: 'Boa'
        pos_hint: {'center_x':0.35, 'center_y':0.2}
        on_press: root.manager.current = 'question5'

    MDRectangleFlatButton:
        text: 'Média'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question5'

    MDRectangleFlatButton:
        text: 'Ruim'
        pos_hint: {'center_x':0.65, 'center_y':0.2}
        on_press: root.manager.current = 'question5'
    
    MDRectangleFlatButton:
        text: 'Péssima'
        pos_hint: {'center_x':0.80, 'center_y':0.2}
        on_press: root.manager.current = 'question5'


<Question5Screen>:
    name: 'question5'
    MDLabel:
        text:  'questao 5'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Ótima'
        pos_hint: {'center_x':0.20, 'center_y':0.2}
        on_press: root.manager.current = 'question6'

    MDRectangleFlatButton:
        text: 'Boa'
        pos_hint: {'center_x':0.35, 'center_y':0.2}
        on_press: root.manager.current = 'question6'

    MDRectangleFlatButton:
        text: 'Média'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question6'

    MDRectangleFlatButton:
        text: 'Ruim'
        pos_hint: {'center_x':0.65, 'center_y':0.2}
        on_press: root.manager.current = 'question6'
    
    MDRectangleFlatButton:
        text: 'Péssima'
        pos_hint: {'center_x':0.80, 'center_y':0.2}
        on_press: root.manager.current = 'question6'


<Question6Screen>:
    name: 'question6'
    MDLabel:
        text:  'questao 6'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Ótima'
        pos_hint: {'center_x':0.20, 'center_y':0.2}
        on_press: root.manager.current = 'question7'

    MDRectangleFlatButton:
        text: 'Boa'
        pos_hint: {'center_x':0.35, 'center_y':0.2}
        on_press: root.manager.current = 'question7'

    MDRectangleFlatButton:
        text: 'Média'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question7'

    MDRectangleFlatButton:
        text: 'Ruim'
        pos_hint: {'center_x':0.65, 'center_y':0.2}
        on_press: root.manager.current = 'question7'
    
    MDRectangleFlatButton:
        text: 'Péssima'
        pos_hint: {'center_x':0.80, 'center_y':0.2}
        on_press: root.manager.current = 'question7'

<Question7Screen>:
    name: 'question7'
    MDLabel:
        text:  'questao 7'
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

'''