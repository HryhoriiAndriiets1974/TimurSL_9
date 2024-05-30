
class Answer:
    def __init__(self, text, on_answer, next_question=None):
        self.text = text
        self.on_answer = on_answer
        self.next_question = next_question

class Question:
    def __init__(self, title, image, answers):
        self.title = title
        self.image = image
        self.answers = answers

class TestEndData:
    def __init__(self, title, desc, image):
        self.title = title
        self.desc = desc
        self.image = image