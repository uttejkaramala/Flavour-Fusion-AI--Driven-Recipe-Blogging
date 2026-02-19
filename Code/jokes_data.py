import random

# Milestone 3: Joke Generation (get_joke() Function)
# This list stores a variety of programming jokes to entertain the user

jokes = [
    "Why do programmers wear glasses? Because they don't C#!",
    "A SQL query walks into a bar, walks up to two tables, and asks... 'Can I join you?'",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why did the programmer quit his job? Because he didn't get arrays (a raise).",
    "['hip', 'hip'] (hip hip array!)",
    "To understand what recursion is, you must first understand what recursion is.",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "A programmer is told to 'go to hell'. He finds the instructions unclear and returns with a syntax error.",
    "Why do Java developers wear glasses? Because they don't C#!",
    "Real programmers count from 0.",
    "What is the most used language in programming? Profanity.",
    "An optimist says: 'The glass is half-full.' A pessimist says: 'The glass is half-empty.' A programmer says: 'The glass is twice as large as it needs to be.'",
    "Why don't programmers like nature? It has too many bugs.",
  "Why do Java developers wear glasses? Because they don't see sharp.",
  "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
  "Why don't programmers like nature? It has too many bugs.",
  "Why do programmers prefer dark mode? Because light attracts bugs!",
  "Why do Java developers wear glasses? Because they don't see sharp.",
  "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
  "Why do Python programmers prefer using snake_case? Because it's easier to read!",
  "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
  "Why did the developer go broke? Because he used up all his cache.",
  "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
  "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
  "Why was the computer cold? It left its Windows open."
]

def get_joke():
    """Selects and returns a random programming joke from the list."""
    return random.choice(jokes)