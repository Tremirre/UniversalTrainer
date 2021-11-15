from question import Question, QuestionFactory
from random import shuffle
from time import sleep


class Trainer:
    def __init__(self):
        self.questions_pool: list[Question] = []
        self.import_questions()

    def run(self):
        shuffle(self.questions_pool)
        for question in self.questions_pool:
            question.process_question()
            sleep(1)

    def show_questions_and_answers(self):
        for question in self.questions_pool:
            question.print_question()
            question.print_answers()
            question.print_correct_answers()

    def import_questions(self, filename = "Questions.csv", csv_file_separator = ','):
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file):
                if line_number == 0:
                    continue
                line = line.split(csv_file_separator)
                parsed = []
                for index, record in enumerate(line):
                    if len(record) != 0 and record != "\n":
                        parsed.append(record.strip('\n').strip())
                self.questions_pool.append(QuestionFactory.create_question(parsed[0], parsed[1:]))