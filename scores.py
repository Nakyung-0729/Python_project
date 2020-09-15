# display title
print()
print("You will be prompted to Enter 3 test scores below.")
print()
print("====================")

# Value
score_01 = 75
score_02 = 85
score_03 = 95

# display result
print()
print("Enter test score: ", score_01)
print("Enter test score: ", score_02)
print("Enter test score: ", score_03)
print()

# calculate total score and average score
total_score = score_01 + score_02 + score_03
average_score = round(total_score / 3)

# format and display the result
print("====================")
print("Your Scores:    ", score_01, score_02, score_03)
print(f'Total Score:\t {total_score}')
print(f'Average Score:\t {average_score}')
print()
