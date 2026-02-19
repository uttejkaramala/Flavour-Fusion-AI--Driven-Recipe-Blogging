# Flavour-Fusion-AI--Driven-Recipe-Blogging

**RecepieMaster** (a.k.a. _Flavour Fusion_) is a small Streamlit web app that uses Google's Generative AI (Gemini) to generate recipe blog posts, suggest dishes from ingredients, and (optionally) analyze an uploaded dish image and create a recipe from it. The project demonstrates a simple, user-friendly interface for creating recipe content powered by the `google-generativeai` package.

---

## Video Demo Link: https://drive.google.com/file/d/1xikmaWcQ48I4k0b82-MsdoVWq1kTuWIg/view?usp=drive_link

---

## Documentation Link: https://drive.google.com/drive/folders/1BUNe1uwNNmuzzOxjaUhqzTqDCXdRhUMR?usp=drive_link

## 🚀 Features

- Generate full recipe blog posts with: Title, Serves, Prep/Cook time, Ingredients, and Instructions.
- Suggest 3–5 dish ideas from a list of ingredients.
- Identify a dish from an uploaded photo and generate a recipe blog for it.
- Lighthearted UI touches (random programmer jokes) to keep users entertained.
- Simple configuration via `.env` for the Gemini API key.

---

## 🔧 Tech Stack

- Python
- Streamlit (UI)
- google-generativeai (Gemini client)
- Pillow (image handling)
- python-dotenv (load environment variables)

---

## 📁 Repository Structure

```
/ (project root)
├─ app.py                # Streamlit app UI and mode routing
├─ ai_service.py         # Core helpers that call the Gemini model
├─ jokes_data.py         # Random programming jokes for UI
├─ requirements.txt      # Python dependencies
├─ README.md             # This file
└─ __pycache__/          # Compiled Python files
```

---

## ✅ Requirements

- Python 3.10+ (recommended)

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# Windows (PowerShell): .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

Contents of `requirements.txt` used in this project:

```
streamlit==1.53.1
python-dotenv==1.2.1
google-generativeai==0.8.6
pillow==12.1.0
```

---

## 🔐 Configuration / Environment Variables

Create a `.env` file in the project root with the following variable:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Notes:

- The app uses `python-dotenv` to load `GEMINI_API_KEY` at startup.
- If the key is not set, the app will be unable to call the Gemini API.

---

## ▶️ Running Locally

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal (typically http://localhost:8501).

---

## 🧭 How to Use

1. Create a Recipe Blog
   - Choose "Create a Recipe Blog" in the sidebar.
   - Enter a dish name (e.g., "Malai Kofta") and desired word count.
   - Click "Generate Recipe" to create a blog post-style recipe.

2. Suggest Dishes from Ingredients
   - Choose "Suggest Dishes from Ingredients".
   - Enter a list like `Bread, Milk, Egg`.
   - Click "Get Suggestions" to receive 3–5 dish ideas.
   - You can request a full recipe for a chosen dish from the suggestions.

3. Identify Dish from Photo
   - Choose "Identify Dish from Photo".
   - Upload a JPG/PNG image and pick a word count.
   - Click "Analyze & Generate" to identify the dish and generate a recipe blog.

---

## 🧩 Implementation Details

- `ai_service.py`:
  - Configures `generation_config` (temperature, top_p, top_k, max_output_tokens, mime type).
  - Creates a `GenerativeModel` with `model_name="gemini-2.5-flash-lite"` and a strict `system_instruction` that mandates the model only generate recipes.
  - `recipe_generation()` builds a text prompt (two modes: "Direct" and "Suggest") and calls `model.generate_content()`.
  - `recipe_from_image()` sends `[prompt, image_data]` to `model.generate_content()` to allow multimodal input. (Depending on SDK & image format, you may need to pass bytes or a proper multimodal payload.)

- `jokes_data.py`:
  - `get_joke()` returns a random programming joke displayed in the UI.

- UI (Streamlit): Uses session state to preserve results and prevent duplicate UI inputs.

---

## ⚠️ Troubleshooting & Tips

- If the app shows an error about missing credentials, confirm `GEMINI_API_KEY` is set and valid.
- API rate limits may return HTTP 429 errors. Implement backoff or re-try later.
- If image analysis fails, ensure the uploaded image is a supported format and size. You may need to convert the `PIL.Image` to bytes or supported form for your specific `google-generativeai` SDK version.
- If model output is unexpected, update the `system_instruction` and `generation_config` in `ai_service.py`.

---

## 🧪 Testing

This project has no formal tests yet. For manual testing:

- Try different dish names and ingredients to verify the app correctly accepts or declines non-food inputs (per the strict system instruction).
- Upload sample dish photos and verify the response is coherent.

Suggested test additions:

- Unit tests for `jokes_data.get_joke()`.
- Integration tests that mock `genai` responses for `ai_service.py`.

---
