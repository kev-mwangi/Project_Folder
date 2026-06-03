from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not (validate_task_title(title) and 
            validate_task_description(description) and 
            validate_due_date(due_date)):
        
        new_task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
        return True
    
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
        return True
    print("Invalid task index.")
    return False

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]
    if pending_tasks:
        print("Pending Tasks:")
        for idx, task in enumerate(pending_tasks):
            print(f"{idx + 1}. {task['title']} - Due: {task['due_date']}")
    else:
        print("No pending tasks.")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
   total_tasks = len(tasks)
   if total_tasks == 0:
        print("No tasks available to calculate progress.")
        return 0
   completed_tasks = sum(1 for task in tasks if task["completed"])
   progress = (completed_tasks / total_tasks) * 100
   print(f"Progress: {progress:.2f}%")
   return progress