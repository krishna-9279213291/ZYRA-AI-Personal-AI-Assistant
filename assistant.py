import ollama
from utils.command_router import execute_command
from agent.planner import plan_task
from agent.executor import run_plan


def process_command(user):

    user = user.lower().strip()

    # 1️⃣ automation commands
    result = execute_command(user)

    if result != "No automation found":
        return result


    # 2️⃣ complex automation planning
    if "create" in user or "build" in user or "make" in user:

        plan = plan_task(user)

        run_plan(plan)

        return f"Task plan:\n{plan}"


    # 3️⃣ AI conversation
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": user}]
    )

    return response["message"]["content"]