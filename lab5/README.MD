# Lab 5: Python Dictionary Programs

This lab contains Python programs and written answers based on dictionaries. The programs cover storing and managing records, processing text, searching data, and using common dictionary operations.

## Folder Structure

```text
Lab5/
├── PartA/
│   ├── student_database.py
│   ├── employee_database.py
│   ├── library_record_system.py
│   ├── word_frequency_counter.py
│   └── phone_directory.py
├── PartB/
│   └── predict_output.txt
├── PartC/
│   └── short_reasoning.txt
└── README.md
```

## Part A: Dictionary Programs

This section contains five programs that use dictionaries to store and process information.

1. **Student Database**  
   Stores student details and subject marks. It allows users to add, update, delete, and view student records. It also provides reports such as student averages, toppers, subject-wise highest marks, and grades.

2. **Employee Database**  
   Stores employee details such as employee ID, name, department, and salary. It supports adding, updating, deleting, and searching employee records. It also generates department-wise reports and salary summaries.

3. **Library Record System**  
   Stores book details and borrowing information. It supports adding books, issuing and returning books, searching for books, and generating library reports.

4. **Word Frequency Counter**  
   Counts how many times each word appears in a given text. It also displays frequently used words, words that appear only once, and groups words by length.

5. **Phone Directory**  
   Stores contact details such as names, phone numbers, email addresses, and cities. It supports adding and updating contacts, searching by name or number, deleting contacts, and displaying directory reports.

## Part B: Predict the Output

This section contains eight Python dictionary code snippets. Each question includes the expected output and an explanation.

The questions cover:

- Dictionary aliasing
- Shallow copying
- Dictionary comprehensions and conditions
- The `setdefault()` method
- Keys that compare equal
- Deleting dictionary items during iteration
- The `pop()` and `popitem()` methods
- Reversing keys and values in a dictionary

File: `PartB/predict_output.txt`

## Part C: Short Reasoning Questions

This section contains answers to eight questions about Python dictionaries.

The topics include:

- Assignment, shallow copy, and deep copy
- Hashable dictionary keys
- Accessing values using `d[key]` and `get()`
- The difference between `update()` and direct assignment
- Creating a new dictionary instead of modifying data in place
- Safe ways to delete dictionary entries
- Inverting a dictionary relationship
- Dictionary lookup time complexity

File: `PartC/short_reasoning.txt`

## How to Run the Programs

Open a terminal in the `PartA` folder and run the required program using Python 3.

For example:

```bash
python3 student_database.py
```

Replace the filename with the program you want to run.

The files in Part B and Part C contain written answers, so they do not need to be executed.

## Concepts Practised

- Creating, accessing, updating, and deleting dictionary entries
- Using nested dictionaries
- Managing records with dictionaries
- Dictionary methods such as `get()`, `update()`, `setdefault()`, `pop()`, and `popitem()`
- Dictionary comprehensions
- Counting and grouping data
- Searching records using dictionary keys
- Shallow and deep copying
- Hashable keys and duplicate-key behaviour
- Safe dictionary iteration and deletion
- Average-case dictionary lookup complexity