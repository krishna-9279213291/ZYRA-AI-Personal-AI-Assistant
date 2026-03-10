from utils.command_router import execute_command

def run_plan(plan):

    steps = plan.split("\n")

    for step in steps:

        step = step.strip()

        if step:
            print("Executing:", step)

            execute_command(step)