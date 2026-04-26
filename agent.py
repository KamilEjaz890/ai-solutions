import os
import time
from groq import Groq
from github import Github, Auth
from dotenv import load_dotenv
import datetime

load_dotenv()

GROQ_API_KEY   = os.getenv("GROQ_API_KEY")
GITHUB_TOKEN   = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_REPO_NAME = os.getenv("GITHUB_REPO_NAME")

# Free Groq client - no region restrictions
groq_client = Groq(api_key=GROQ_API_KEY)

AI_PROBLEMS = [
    "Write a Python function that implements linear regression from scratch using only numpy. Include comments.",
    "Write a Python implementation of K-Means clustering from scratch with a simple example.",
    "Write a Python script that builds a simple chatbot using if/else logic and a dictionary of responses.",
    "Write a Python function that implements bubble sort and explains how it works step by step.",
    "Write a Python script that reads a list of numbers and plots a bar chart using matplotlib.",
    "Write a Python implementation of a binary search algorithm with clear comments.",
    "Write a Python function that counts word frequency in a text and shows the top 10 words.",
    "Write a Python script that generates a simple quiz game with 5 AI-related questions.",
    "Write a Python function that implements the Fibonacci sequence three different ways.",
    "Write a Python script that simulates a basic neural network forward pass using only numpy.",
]

def solve_with_groq(problem):
    print(f"\n AI is solving: {problem[:60]}...")

    prompt = f"""You are an expert Python developer. Solve this problem:

{problem}

Rules:
- Write complete, runnable Python code only
- Add clear comments explaining each part
- Include a working example at the bottom
- Keep it beginner-friendly

Return ONLY Python code. No explanations outside the code."""

    for attempt in range(3):
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",   # free, very capable 
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000,
            )

            code = response.choices[0].message.content

            # Clean markdown fences if model adds them
            if "```python" in code:
                code = code.split("```python")[1].split("```")[0].strip()
            elif "```" in code:
                code = code.split("```")[1].split("```")[0].strip()

            return code

        except Exception as e:
            if "429" in str(e) or "rate" in str(e).lower():
                wait = 30 * (attempt + 1)
                print(f"Rate limit hit. Waiting {wait} seconds...")
                time.sleep(wait)
            else:
                raise e

    raise Exception("Failed after 3 attempts. Try again in a few minutes.")

def push_to_github(code, problem, problem_number):
    print("Pushing to GitHub...")
    g = Github(auth=Auth.Token(GITHUB_TOKEN))
    user = g.get_user(GITHUB_USERNAME)
    repo = user.get_repo(GITHUB_REPO_NAME)

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"solutions/problem_{problem_number:03d}_{today}.py"

    file_content = f'''"""
Problem #{problem_number}
Date: {today}
Task: {problem}


{code}
'''

    try:
        existing = repo.get_contents(filename)
        repo.update_file(
            filename,
            f"Update solution #{problem_number}",
            file_content,
            existing.sha
        )
        print(f"Updated: {filename}")
    except Exception:
        repo.create_file(
            filename,
            f"Add solution #{problem_number} - {today}",
            file_content
        )
        print(f"Created: {filename}")

    return filename

def update_readme(problem_number, problem, filename):
    print("Updating README...")
    g = Github(GITHUB_TOKEN)
    user = g.get_user(GITHUB_USERNAME)
    repo = user.get_repo(GITHUB_REPO_NAME)

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    new_entry = f"| #{problem_number} | {today} | {problem[:55]}... | [View]({filename}) |\n"

    try:
        readme = repo.get_contents("README.md")
        content = readme.decoded_content.decode("utf-8")

        if "| # | Date |" not in content:
            content += "\n\n## AI Solutions Log\n\n| # | Date | Problem | Code |\n|---|------|---------|------|\n"

        content += new_entry
        repo.update_file(
            "README.md",
            f"Log solution #{problem_number}",
            content,
            readme.sha
        )
        print("README updated!")
    except Exception as e:
        print(f"README update skipped: {e}")

def run_agent():
    print("\n" + "="*50)
    print("Free AI GitHub Agent Running!")
    print("="*50)

    day_of_year = datetime.datetime.now().timetuple().tm_yday
    problem_number = (day_of_year % len(AI_PROBLEMS)) + 1
    problem = AI_PROBLEMS[problem_number - 1]

    print(f"Today's problem #{problem_number}: {problem[:70]}...")

    try:
        # Step 1: Solve with Groq (free LLaMA3)
        code = solve_with_groq(problem)
        print("Code generated!")

        # Step 2: Push to GitHub
        filename = push_to_github(code, problem, problem_number)

        # Step 3: Update README
        update_readme(problem_number, problem, filename)

        print(f"\nDone! View at: https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_agent()