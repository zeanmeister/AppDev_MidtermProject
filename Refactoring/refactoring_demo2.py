# ======================================================
# Demonstration of: Rename → Extract Method → Change Signature →
# Inline → Code Cleanup → Safe Delete (Moderate Difficulty)
# ======================================================

# Sample program: Simple student grade processing system

students = [
    {"name": "Alice", "scores": [88, 92, 85]},
    {"name": "Bob", "scores": [75, 80, 70]},
    {"name": "Charlie", "scores": [90, 95, 93]},
]


# 1. RENAME (Shift + F6)
def calculateaverage(scores):
    total = sum(scores)
    return total / len(scores)

# Try renaming calculateaverage → calculate_average


# 2. EXTRACT METHOD (Ctrl + Alt + M)
def process_students(student_list):
    print("Processing students...\n")
    for s in student_list:
        avg = calculateaverage(s["scores"])
        status = "Passed" if avg >= 75 else "Failed"
        print(f"{s['name']}: {avg:.2f} - {status}")

# Try extracting the code inside the loop into a new function, e.g., "evaluate_student(student)"


# 3. CHANGE SIGNATURE (Ctrl + F6)
def print_summary(students, include_details):
    print("\nSummary Report")
    if include_details:
        for s in students:
            print(f"Student: {s['name']}, Avg: {calculateaverage(s['scores']):.2f}")

# Try changing signature to include an optional "threshold" argument
# e.g., def print_summary(students, include_details, threshold=75)
# Then use it inside the loop for filtering


# 4. INLINE VARIABLE / METHOD (Ctrl + Alt + N)
def get_highest_score(scores):
    top = max(scores)
    return top

# Try inlining variable 'top' or even the entire get_highest_score() call inside the print


# 5. REFORMAT / CODE CLEANUP (Ctrl + Alt + L)
def messyfunction(x,y):return x*y+ (x/y)
print("Result:",messyfunction(10,5))
# Try running Code Cleanup to fix spacing and layout automatically


# 6. SAFE DELETE (Alt + Delete)
def old_feature():
    print("This function is no longer needed.")
# Try safely deleting this function and see if PyCharm warns about usage


# Program Execution
if __name__ == "__main__":
    process_students(students)
    print_summary(students, include_details=True)
    print("Highest score of Alice:", get_highest_score(students[0]["scores"]))
