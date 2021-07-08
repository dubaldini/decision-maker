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
    RulesScreen2:
    ResultsScreen:  

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
        text:  'Uma situação igual ou parecida a essa já aconteceu no passado? Avalie como foi de ótima a péssima:'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Ótima'
        pos_hint: {'center_x':0.1, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

    MDRectangleFlatButton:
        text: 'Boa'
        pos_hint: {'center_x':0.25, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

    MDRectangleFlatButton:
        text: 'Média'
        pos_hint: {'center_x':0.4, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

    MDRectangleFlatButton:
        text: 'Ruim'
        pos_hint: {'center_x':0.575, 'center_y':0.2}
        on_press: root.manager.current = 'question3'
    
    MDRectangleFlatButton:
        text: 'Péssima'
        pos_hint: {'center_x':0.725, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

    MDRectangleFlatButton:
        text: 'Não se aplica'
        pos_hint: {'center_x':0.9, 'center_y':0.2}
        on_press: root.manager.current = 'question3'

<Question3Screen>:
    name: 'question3'
    MDLabel:
        text:  'Uma situação igual ou parecida a essa já te machucou no passado?'
        halign: 'center'
         
    MDRectangleFlatButton:
        text: 'Sim'
        pos_hint: {'center_x':0.25, 'center_y':0.2}
        on_press: root.manager.current = 'question4'

    MDRectangleFlatButton:
        text: 'Não se aplica'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question4'

    MDRectangleFlatButton:
        text: 'Não'
        pos_hint: {'center_x':0.75, 'center_y':0.2}
        on_press: root.manager.current = 'question4'

<Question4Screen>:
    name: 'question4'
    MDLabel:
        text:  'Você terá outra oportunidade de fazer o que essa decisão implica num futuro próximo?'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Sim'
        pos_hint: {'center_x':0.25, 'center_y':0.2}
        on_press: root.manager.current = 'question5'

    MDRectangleFlatButton:
        text: 'Não se aplica'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question5'

    MDRectangleFlatButton:
        text: 'Não'
        pos_hint: {'center_x':0.75, 'center_y':0.2}
        on_press: root.manager.current = 'question5'

<Question5Screen>:
    name: 'question5'
    MDLabel:
        text:  'Você sente que existe a possibilidade de você se arrepender caso não faça o que essa decisão implica?'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Sim'
        pos_hint: {'center_x':0.25, 'center_y':0.2}
        on_press: root.manager.current = 'question6'

    MDRectangleFlatButton:
        text: 'Não se aplica'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question6'

    MDRectangleFlatButton:
        text: 'Não'
        pos_hint: {'center_x':0.75, 'center_y':0.2}
        on_press: root.manager.current = 'question6'

<Question6Screen>:
    name: 'question6'
    MDLabel:
        text:  'A situação envolve questões que podem te prejudicar ou prejudicar alguém que você ama?'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Sim'
        pos_hint: {'center_x':0.25, 'center_y':0.2}
        on_press: root.manager.current = 'question7'

    MDRectangleFlatButton:
        text: 'Não se aplica'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'question7'

    MDRectangleFlatButton:
        text: 'Não'
        pos_hint: {'center_x':0.75, 'center_y':0.2}
        on_press: root.manager.current = 'question7'

<Question7Screen>:
    name: 'question7'
    MDLabel:
        text:  'Pense na situação de maneira inversa, caso se aplique, você gostaria que a decisão afirmativa (positiva, sim) fosse tomada?'
        halign: 'center'
         

    MDRectangleFlatButton:
        text: 'Sim'
        pos_hint: {'center_x':0.25, 'center_y':0.2}
        on_press: root.manager.current = 'rules2'

    MDRectangleFlatButton:
        text: 'Não se aplica'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'rules2'

    MDRectangleFlatButton:
        text: 'Não'
        pos_hint: {'center_x':0.75, 'center_y':0.2}
        on_press: root.manager.current = 'rules2'

<RulesScreen2>:
    name: 'rules2'
    MDLabel:
        text:  'rules2'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Obtenha seu resultado'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'results'

<ResultsScreen>:
    name: 'results'
    MDLabel:
        text:  'results'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Voltar para o menu'
        pos_hint: {'center_x':0.50, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

'''