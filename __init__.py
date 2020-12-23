from mycroft import MycroftSkill, intent_file_handler


class Farmvoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('farmvoice.intent')
    def handle_farmvoice(self, message):
        self.speak_dialog('farmvoice')


def create_skill():
    return Farmvoice()

