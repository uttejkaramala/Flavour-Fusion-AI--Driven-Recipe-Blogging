import streamlit as st
from PIL import Image  
from Code.ai_service import recipe_generation, recipe_from_image 

st.set_page_config(page_title="Flavour Fusion", page_icon="🍳", layout="wide")
st.title("RecepieMaster: AI-Powered Blog Generation")

# --- INITIALIZE SEPARATE SESSION STATES ---
if "blog_content" not in st.session_state:
    st.session_state.blog_content = None
if "ingredient_suggestions" not in st.session_state:
    st.session_state.ingredient_suggestions = None
if "image_analysis_result" not in st.session_state:
    st.session_state.image_analysis_result = None
if "final_recipe_result" not in st.session_state:
    st.session_state.final_recipe_result = None
# Sidebar Navigation
with st.sidebar:
    st.header("⚙️ Options")
    mode = st.radio(
        "**Choose your method:**",
        ["Create a Recipe Blog", "Suggest Dishes from Ingredients", "Identify Dish from Photo"]
    )
    
    if st.button("🗑️ Clear All History"):
        keys_to_clear = [
            "blog_content", 
            "ingredient_suggestions", 
            "final_recipe_result", 
            "image_analysis_result"
        ]
    
        for key in keys_to_clear:
            if key in st.session_state:
                st.session_state[key] = None
    
        st.rerun()

# --- MODE 1: CREATE A RECIPE BLOG ---
if mode == "Create a Recipe Blog":
    topic = st.text_input("Topic", placeholder="e.g., Malai Kofta")
    word_count = st.number_input("Number of words", 100, 2000, 555, key="dir_wc")
    
    if st.button("Generate Recipe"):
        if not topic.strip():
            st.warning("⚠️ Please enter a dish name!")
        else:
            with st.status("⌛ Generating...", expanded=True) as status:
                result = recipe_generation(topic, word_count, mode="Direct")
                st.session_state.blog_content = result
                status.update(label="✅ Ready!", state="complete")

    if st.session_state.blog_content:
        st.markdown("---")
        st.markdown(st.session_state.blog_content)
        st.download_button("📥 Download Blog", st.session_state.blog_content, "blog.txt")

# --- MODE 2: SUGGEST DISHES FROM INGREDIENTS ---
elif mode == "Suggest Dishes from Ingredients":
    ingredients = st.text_area("List your ingredients", placeholder="e.g., Bread, Milk, Egg")
    
    if st.button("Get Suggestions"):
        if not ingredients.strip():
            st.warning("⚠️ Please enter ingredients!")
        else:
            with st.status("⌛ AI Chef is thinking...", expanded=True) as status:
                result = recipe_generation(ingredients, 300, mode="Suggest")
                # Save suggestions to one variable
                st.session_state.ingredient_suggestions = result
                # Reset the final recipe so old one doesn't show for new ingredients
                st.session_state.final_recipe_result = None 
                status.update(label="✅ Ideas ready!", state="complete")

    # 1. ALWAYS show the suggestions if they exist
    if st.session_state.ingredient_suggestions:
        st.markdown("---")
        st.markdown("### 💡 Suggested Dishes")
        st.info(st.session_state.ingredient_suggestions)
        
        # 2. Show the input form ONLY if the final recipe hasn't been generated yet
        # This prevents the "Two Input Blocks" or "Duplicate UI" issue
        if not st.session_state.final_recipe_result:
            st.subheader("👨‍🍳 Get the Full Recipe")
            with st.form("recipe_request_form"):
                chosen_dish = st.text_input("Which dish would you like the full recipe for?")
                submitted = st.form_submit_button("Generate Full Recipe")
                
                if submitted and chosen_dish:
                    with st.status("⌛ Cooking the full blog post...", expanded=True):
                        full_recipe = recipe_generation(chosen_dish, 800, mode="Direct")
                        
                        # Save the recipe to a SECOND variable to keep both on screen
                        if full_recipe:
                            st.session_state.final_recipe_result = full_recipe
                            st.rerun()
                        else:
                            # Handle potential rate limit errors (429) gracefully
                            st.error("Too many requests! Please wait 30 seconds.")

    # 3. Display the Final Recipe at the bottom
    if st.session_state.final_recipe_result:
        st.markdown("---")
        st.markdown("## 📖 Full Recipe Blog")
        st.markdown(st.session_state.final_recipe_result)
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("📥 Download Recipe", st.session_state.final_recipe_result, "recipe.txt")
        with col2:
            # Allow user to go back to the list and pick something else
            if st.button("⬅️ Pick a different dish"):
                st.session_state.final_recipe_result = None
                st.rerun()
                

# --- MODE 3: IDENTIFY DISH FROM PHOTO ---
elif mode == "Identify Dish from Photo":
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
    word_count = st.number_input("Desired Word Count", 100, 2000, 500, key="img_wc")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Your Uploaded Dish', width=400)
        
        if st.button("Analyze & Generate"):
            with st.status("⌛ Analyzing image...", expanded=True):
                result = recipe_from_image(image, word_count)
                st.session_state.image_analysis_result = result

    if st.session_state.image_analysis_result:
        st.markdown("---")
        st.markdown(st.session_state.image_analysis_result)
        st.download_button("📥 Download Analysis", st.session_state.image_analysis_result, "analysis.txt")