import tkinter as tk
from tkinter import messagebox

# Rules for evaluation
rules = {
    "rule1": "If the employee meets all project deadlines, add 20 points.",
    "rule2": "If the employee consistently exceeds expectations, add 30 points.",
    "rule3": "If the employee shows initiative and takes on additional responsibilities, add 15 points.",
    "rule4": "If the employee collaborates well in a team, add 10 points.",
    "rule5": "If the employee is always punctual, add 10 points.",
    "rule6": "If the employee receives positive client feedback, add 15 points.",
    "rule7": "If the employee brings new ideas and innovations, add 20 points.",
    "rule8": "If the employee is frequently absent or misses deadlines, subtract 25 points.",
    "rule9": "If the employee consistently performs below expectations, subtract 35 points."
}

# Function to evaluate employee performance
def evaluate_employee():
    try:
        name = entry_name.get()
        if not name:
            raise ValueError("Please enter the employee's name.")

        # Get input values
        deadlines_met = var_deadlines.get()
        expectations_exceeded = var_expectations.get()
        initiative_taken = var_initiative.get()
        teamwork = var_teamwork.get()
        punctuality = var_punctuality.get()
        client_feedback = var_client_feedback.get()
        innovation = var_innovation.get()
        absences = var_absences.get()
        below_expectations = var_below_expectations.get()

        # Calculate score
        score = (20 * deadlines_met) + (30 * expectations_exceeded) + (15 * initiative_taken) + \
                (10 * teamwork) + (10 * punctuality) + (15 * client_feedback) + (20 * innovation) - \
                (25 * absences) - (35 * below_expectations)

        # Show result
        messagebox.showinfo("Performance Evaluation", f"Employee {name} scored {score} points.")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create GUI window
root = tk.Tk()
root.title("Employee Performance Evaluation System")
root.geometry("500x500")

# Employee Name
tk.Label(root, text="Employee Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Questions with checkboxes
var_deadlines = tk.IntVar()
var_expectations = tk.IntVar()
var_initiative = tk.IntVar()
var_teamwork = tk.IntVar()
var_punctuality = tk.IntVar()
var_client_feedback = tk.IntVar()
var_innovation = tk.IntVar()
var_absences = tk.IntVar()
var_below_expectations = tk.IntVar()

questions = [
    ("Did the employee meet all project deadlines?", var_deadlines),
    ("Did the employee exceed expectations?", var_expectations),
    ("Did the employee take initiative?", var_initiative),
    ("Is the employee a good team player?", var_teamwork),
    ("Is the employee punctual?", var_punctuality),
    ("Did the employee receive positive client feedback?", var_client_feedback),
    ("Did the employee bring new innovative ideas?", var_innovation),
    ("Was the employee frequently absent?", var_absences),
    ("Did the employee perform below expectations?", var_below_expectations)
]

for question, var in questions:
    tk.Checkbutton(root, text=question, variable=var).pack(anchor="w")

# Evaluate Button
tk.Button(root, text="Evaluate Performance", command=evaluate_employee).pack(pady=10)

# Run the GUI
root.mainloop()