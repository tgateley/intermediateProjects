quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
    ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1),
]

for item in quiz_questions:
    print(item[0])
    answer_list = item[1]
    correct_choice = item[2] - 1

    for index, answer in enumerate(item[1]):
        index = index + 1
        print(index, ". ", answer)
    a = int(input("Enter your choice: "))
    if a == item[2]:
        print("Correct!")
    else:
        print(f"Incorrect, the correct answer was {item[2]}. {answer_list[correct_choice]}")



