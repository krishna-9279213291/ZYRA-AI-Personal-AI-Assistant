import ollama

def plan_task(task):

    prompt = f"""
    Break the following task into simple computer actions.

    Task: {task}

    Only return steps like:
    open browser
    search google
    open vscode
    create file
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
    )

    plan = response["message"]["content"]

    return plan