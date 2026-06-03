from datetime import datetime

def validate_task_title(title):
    if isinstance(title, str) and title.strip():
        return True
    print("Invalid task title. It must be empty .")
    
def validate_task_description(description):
    if isinstance(description, str) :
        return True
    print("Invalid task description. It must be a text.") 
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid due date format. It must be in YYYY-MM-DD format.")