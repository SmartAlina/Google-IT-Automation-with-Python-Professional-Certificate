def setup_gradebook(old_gradebook):
    new_gradebook = old_gradebook.copy() 
    for student, grade in new_gradebook.items():
        new_gradebook[student] = 0
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}
