import ollama

from utils.command_router import execute_command

# ============================================
# ZYRA SYSTEM PROMPT
# ============================================

SYSTEM_PROMPT = """
You are ZYRA, a powerful AI assistant.

You can:

- answer questions
- explain concepts
- generate code
- plan tasks
- control computer automation

If the user asks to open apps, control the computer,
or run automation, respond briefly because the system
will execute the command.

Be clear and intelligent.
"""

# ============================================
# MEMORY
# ============================================

chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

MAX_HISTORY = 12


# ============================================
# AI CHAT
# ============================================

def ask_ai(user_input):

    global chat_history

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    if len(chat_history) > MAX_HISTORY:
        chat_history = chat_history[-MAX_HISTORY:]

    response = ollama.chat(
        model="llama3",
        messages=chat_history,
        options={
            "temperature": 0.7,
            "num_predict": 200
        }
    )

    ai_reply = response["message"]["content"]

    chat_history.append({
        "role": "assistant",
        "content": ai_reply
    })

    return ai_reply


# ============================================
# INTENT DETECTION
# ============================================

def detect_intent(command):

    prompt = f"""
Classify this request:

{command}

Categories:
automation
question
coding
planning

Return only the category.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip().lower()


# ============================================
# TASK PLANNER
# ============================================

def plan_task(task):

    prompt = f"""
Break this task into simple automation steps.

Task: {task}

Return numbered steps only.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# ============================================
# CODE GENERATOR
# ============================================

def generate_code(request):

    prompt = f"""
Write clean Python code for:

{request}

Provide working code.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


# ============================================
# MAIN BRAIN FUNCTION (IMPROVED)
# ============================================

def process_command(user_input):

    # 1️⃣ FIRST check automation directly
    automation_result = execute_command(user_input)

    if automation_result != "No automation found":
        return automation_result

    # 2️⃣ If not automation → detect intent
    intent = detect_intent(user_input)

    # ----------------------------
    # CODING
    # ----------------------------

    if intent == "coding":

        return generate_code(user_input)

    # ----------------------------
    # PLANNING
    # ----------------------------

    elif intent == "planning":

        return plan_task(user_input)

    # ----------------------------
    # NORMAL QUESTION
    # ----------------------------

    else:

        return ask_ai(user_input)


# ============================================
# MEMORY RESET
# ============================================

def reset_memory():

    global chat_history

    chat_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]