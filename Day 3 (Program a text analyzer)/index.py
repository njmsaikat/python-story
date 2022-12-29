my_text = "This is my test text"
search_letter = my_text.index("x")
r_result = my_text.rindex("x")  # searches right to left

print(search_letter)
print(r_result)

search_letter_limit = my_text.index("t", 5, 12)
print(search_letter_limit)
