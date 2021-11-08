from question import Question, QuestionFactory
from time import sleep
from os import system


class Trainer:
    def __init__(self):
        self.questions_pool: list[Question] = []
        self.import_questions()

    def run(self):
        for question in self.questions_pool:
            question.process_question()
            sleep(0.5)

    def import_questions(self, filename = "Questions.csv", csv_file_separator = ';'):
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file):
                if line_number == 0:
                    continue
                line = line.split(',')
                parsed = []
                for index, record in enumerate(line):
                    if len(record) != 0 and record != "\n":
                        parsed.append(record.strip('\n').strip())
                self.questions_pool.append(QuestionFactory.create_question(parsed[0], parsed[1:]))