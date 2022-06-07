import os
from random import shuffle, sample
from time import sleep
from Trainer.question import QuestionFactory
from Trainer.input_parser import Mode, parse_input


class Trainer:
    PACKAGES_FOLDER = "AvailablePackages"

    def __init__(self):
        self.questions_pool = []
        self.mode, self.test_size = parse_input()
        self.import_questions()

    def run(self):
        mode_dict = {
            Mode.TEST: self.test,
            Mode.TRAIN: self.train,
            Mode.LIST: self.show_questions_and_answers,
            Mode.QUIT: lambda: None,
        }
        mode_dict[self.mode]()

    def test(self):
        adjusted_test_size = min(self.test_size, len(self.questions_pool))
        selected = sample(self.questions_pool, adjusted_test_size)
        score = 0
        for question in selected:
            score += question.process_question(test=True)
            sleep(1)
        print("\n========================================================\n")
        print(
            f"Test completed! Obtained score: {score}/{adjusted_test_size} correct answers"
        )

    def train(self):
        shuffle(self.questions_pool)
        for question in self.questions_pool:
            question.process_question()
            sleep(1)

    def show_questions_and_answers(self):
        for question in self.questions_pool:
            question.print_question()
            question.print_answers()
            question.print_correct_answers()
            print()

    def import_questions(self, csv_file_separator=","):
        for filename in os.listdir("AvailablePackages"):
            with open(f"{Trainer.PACKAGES_FOLDER}/{filename}", "r") as file:
                for line in file:
                    line = line.split(csv_file_separator)
                    parsed = []
                    for index, record in enumerate(line):
                        if len(record) != 0 and record != "\n":
                            parsed.append(record.strip("\n").strip())
                    self.questions_pool.append(
                        QuestionFactory.create_question(parsed[0], parsed[1:])
                    )
