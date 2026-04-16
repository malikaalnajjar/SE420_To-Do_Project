tasks = []
next_id = 1


def add_task():
    global next_id
    d = input("Enter task description: ")
    t = {"id": next_id, "description": d, "status": "pending"}
    tasks.append(t)
    next_id += 1
    print("Task added.")


def add_urgent_task():
    global next_id
    d = input("Enter urgent task description: ")
    t = {"id": next_id, "description": d, "status": "pending"}
    tasks.append(t)
    next_id += 1
    print("Urgent task added.")


def do_everything():
    global next_id
    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. Complete task")
        print("4. List tasks")
        print("5. Quit")
        c = input("Choice: ")

        if c == "1":
            d = input("Enter task description: ")
            t = {"id": next_id, "description": d, "status": "pending"}
            tasks.append(t)
            next_id += 1
            print("Task added.")

        elif c == "2":
            i = int(input("Enter task ID to delete: "))
            for x in tasks:
                if x["id"] == i:
                    tasks.remove(x)
                    print("Task deleted.")
                    break
            else:
                print("Task not found.")

        elif c == "3":
            i = int(input("Enter task ID to complete: "))
            for x in tasks:
                if x["id"] == i:
                    x["status"] = "done"
                    print("Task marked as done.")
                    break
            else:
                print("Task not found.")

        elif c == "4":
            if not tasks:
                print("No tasks.")
            for x in tasks:
                print(x["id"], x["description"], x["status"])

        elif c == "5":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    do_everything()
