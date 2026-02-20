import os
import google.generativeai as genai
from dotenv import load_dotenv
from jokes_data import get_joke
import streamlit as st

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-lite",
    generation_config=generation_config,
    system_instruction=(
        "You are a specialized Recipe AI. Your ONLY job is to generate food recipes. "
        "If a user provides a name of a person, a random object, or a topic unrelated "
        "to food or cooking, you must politely decline and say: "
        "'I am a Recipe Assistant. Please provide a dish name or ingredients to proceed.'"
    )
)

def recipe_generation(user_input, word_count, mode="Direct"):
    try:
        st.info(f"**Random Programmer Joke:** {get_joke()}")
        
        if mode == "Suggest":
            prompt = (
                f"The user has these ingredients: {user_input}. "
                "Suggest 3-5 specific dish names and briefly describe each. "
                "--- NEGATIVE CONSTRAINTS ---\n"
                "- ONLY suggest edible food items.\n"
                "- If the input contains non-food items or names, do not suggest a dish for them.\n"
                "- DO NOT make up imaginary ingredients."
            )
        else:
            prompt = (
                f"Write a recipe blog about '{user_input}' (~{word_count} words). "
                "Include: Catchy Title, Serves, Prep/Cook time, Ingredients, and Instructions.\n"
                "--- STRICT RULES ---\n"
                f"- If '{user_input}' is a person's name, a famous figure, or not a food item, "
                "DO NOT generate a recipe.\n"
                "- Instead, politely say: 'I am sorry, but I can only generate recipes for food items.'\n"
                "- DO NOT hallucinate or invent dishes for non-edible topics."
            )

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    
def recipe_from_image(image_data, word_count):
    try:
        st.info(f"**Random Programmer Joke:** {get_joke()}")
        prompt = (
            f"Identify this dish and write a {word_count} word recipe blog. "
            "Include: Title, Serves, Prep/Cook time, Ingredients, and Instructions."
        )
        # Pass both prompt and image to the model
        response = model.generate_content([prompt, image_data])
        return response.text
    except Exception as e:
        st.error(f"Could not analyze image: {e}")
        return None