from abc import ABC, abstractmethod
from random import shuffle
from string import ascii_uppercase


class Question(ABC):
    @abstractmethod
    def __init__(self, question_content: str, answers: list[str]) -> None:
        self._question_content: str = question_content
        self._answers = answers

    @abstractmethod
    def check_answer(self, answer: str):
        ...

    def print_question(self):
        print(self._question_content, '\n')

    def print_answers(self):
        shuffle(self._answers)
        for index, answer in enumerate(self._answers):
            print(f"{ascii_uppercase[index]}: {answer}")
        print()

    @abstractmethod
    def ask_for_answers(self):
        ...

    @abstractmethod
    def print_correct_answers(self):
        ...

    def process_question(self, test=False) -> bool:
        print()
        self.print_question()
        self.print_answers()
        user_answers = self.ask_for_answers()
        correct = self.check_answer(user_answers)
        if not test:
            if not correct:
                print("Incorrect answer!")
                self.print_correct_answers()
            else:
                print("Answer correct!")
        print("\n========================================================")
        return correct


class SingleChoice(Question):
    def __init__(self, question_content: str, answers: list[str], correct_index: int) -> None:
        super().__init__(question_content, answers)
        self._correct = answers[correct_index]

    def check_answer(self, letter: str) -> bool:
        if len(letter) != 1:
            return False
        index = ord(letter.upper()) - ord('A')
        return index < len(self._answers) and self._answers[index] == self._correct

    def ask_for_answers(self) -> str:
        answer = input("Provide letter (or letters separated by spaces) as your answer/s\n")
        return answer

    def print_correct_answers(self) -> None:
        print(f"Correct answer:\n\t({ascii_uppercase[self._answers.index(self._correct)]}) {self._correct}")


class MultipleChoice(Question):
    def __init__(self, question_content: str, answers: list[str], correct_indices: list[int]) -> None:
        super().__init__(question_content, answers)
        self._correct = set([answers[i] for i in correct_indices])

    def check_answer(self, letters: list[str]) -> bool:
        if len(letters) != len(self._correct):
            return False
        for letter in letters:
            if (answer_id := ascii_uppercase.index((letter.upper()))) >= len(self._answers):
                return False
            if self._answers[answer_id] not in self._correct:
                return False
        return True

    def ask_for_answers(self) -> list[str]:
        answer = input("Provide letter (or letters separated by spaces) as your answer/s\n")
        return answer.split()

    def print_correct_answers(self) -> None:
        answers_with_ids = [(correct_answer, self._answers.index(correct_answer)) for correct_answer in self._correct]
        answers_with_ids.sort(key=lambda pair: pair[1])
        print("Correct answers:")
        for answer, answer_id in answers_with_ids:
            print(f"\t({ascii_uppercase[answer_id]}) {answer}")


class BooleanQuestion(Question):
    def __init__(self, question_content: str, correct: bool) -> None:
        super().__init__(question_content, ["True", "False"])
        self._correct = correct

    def check_answer(self, letter: str) -> bool:
        if letter not in {'t', 'T', 'f', 'F'}:
            return False
        answer = letter.lower() == 't'
        return answer == self._correct

    def ask_for_answers(self) -> str:
        answer = input("Provide true or false answer [input T/F]\n")
        return answer[0]

    def print_correct_answers(self) -> None:
        print(f"Correct answer:\n\t{self._correct}")

    def print_answers(self):
        print()


class QuestionFactory:
    @staticmethod
    def create_question(question_content: str, answers: list[str]) -> Question:
        if (options := len(answers)) < 2:
            raise Exception(f"Invalid number of numbers ({options}) for question {question_content}")
        correct_indices = []
        boolean_flag = False
        for index, answer in enumerate(answers):
            if answer.strip()[0] == '#':
                correct_indices.append(index)
                answers[index] = answer.strip()[1:]
            if not boolean_flag and answer.strip().lower() in {"true", "false"}:
                boolean_flag = True
        if boolean_flag and len(correct_indices) == 1:
            return BooleanQuestion(question_content, answers[correct_indices[0]].lower() == "true")
        elif not boolean_flag and len(correct_indices) == 1:
            return SingleChoice(question_content, answers, correct_indices[0])
        elif not boolean_flag and len(correct_indices) > 1:
            return MultipleChoice(question_content, answers, correct_indices)
        else:
            raise Exception(f"Invalid parameters: number of correct answers = {len(correct_indices)}",
                            f"for question {question_content}")
