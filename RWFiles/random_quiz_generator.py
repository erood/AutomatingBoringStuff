#! python3
# random_quiz_generator.py - creates quizzes with questions and answers in random order, along with the answer key.

import random

NUMBER_OF_QUIZZES = 35

CAPITALS = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


def main():
    for quiz_number in range(NUMBER_OF_QUIZZES):
        generate_quiz(quiz_number)


def generate_quiz(quiz_number):
    number = quiz_number + 1
    quiz = create_quiz("capitalquiz%s.txt", number)
    answer_key = create_answer_key("capitalquiz_answers%s.txt", number)
    write_header(quiz, number)
    states = list(CAPITALS.keys())
    random.shuffle(states)

    for question_number in range(len(CAPITALS)):
        correct_answer, answer_options = get_answer_options(states, question_number, 3)
        random.shuffle(answer_options)
        write_question(answer_options, question_number, quiz, states)
        write_answer_key(answer_key, question_number, answer_options, correct_answer)

    quiz.close()
    answer_key.close()


def create_quiz(name, number):
    return open(name % number, "w")


def create_answer_key(name, number):
    return open(name % number, "w")


def write_header(file, number):
    file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    file.write((' ' * 20) + "State Capitals Quiz (Form %s)" % number)
    file.write("\n\n")


def get_answer_options(states, question_number, options):
    correct_answer = CAPITALS[states[question_number]]
    wrong_answers = list(CAPITALS.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, options)

    return correct_answer, wrong_answers + [correct_answer]


def write_question(answer_options, question_number, quiz, states):
    quiz.write("%s. What is the capital of %s?\n" % (question_number + 1, states[question_number]))
    for i in range(len(answer_options)):
        quiz.write("\t%s. %s\n" % ("ABCD"[i], answer_options[i]))
    quiz.write("\n")


def write_answer_key(file, question_number, answer_options, correct_answer):
    file.write("%s. %s\n" % (question_number + 1, "ABCD"[answer_options.index(correct_answer)]))


if __name__ == "__main__":
    main()
