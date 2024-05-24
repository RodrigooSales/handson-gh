def getIncompleteTasks():
    tasks = fetchTasksFromDatabase()
    incompleteTasks = []
 
    for task in tasks:
        if not task.completed:
            incompleteTasks.append(task)
 
    return incompleteTasks 

# Refactor the above code to use list comprehension