from data import question_data


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_1 = Question(question_data[0]["text"], question_data[1]["answer"])
