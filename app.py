import streamlit as st
import random
from datetime import date
#from streamlit_autorefresh import st_autorefresh
import time

# Title
st.title("🌿 Urban Gardening Helper")
st.subheader("Find plants suitable for your urban space 🌇")


# List of rotating gardening tips
gardening_tips = [
    "🌱 Water early in the morning to reduce evaporation.",
    "🌿 Prune dead leaves regularly for healthy growth.",
    "☀️ Give plants enough sunlight, but avoid midday heat.",
    "🐛 Watch out for pests – neem oil works great!",
    "🍃 Mulch helps retain soil moisture and reduce weeds.",
    "📅 Create a care calendar – consistency is key!",
    "🚿 Don’t overwater – soggy roots are harmful!",
    "🪴 Rotate indoor plants weekly for even growth.",
    "🌼 Use compost to enrich your soil naturally.",
    "🔍 Check soil moisture before watering again."
]
# Sidebar selection
selected_option = st.sidebar.radio(
    "Navigate",
    ("Home", "Add Plant", "Favorites", "Care Guide", "Cost Estimator", 
     "Plant Journal", "Quiz", "Community Tips", "Gamification", "Daily Activity")
)

# Select a new random gardening tip each time user changes sidebar option
if "last_selected_option" not in st.session_state:
    st.session_state.last_selected_option = None

if selected_option != st.session_state.last_selected_option:
    st.session_state.random_tip = random.choice(gardening_tips)
    st.session_state.last_selected_option = selected_option

# Display the tip
st.markdown("### 🌻 Gardening Tip")
st.success(st.session_state.random_tip)


#tip = random.choice(gardening_tips)
#st.sidebar.success(f"🌿 Gardening Tips: {tip}")
#selected_option = st.sidebar.radio("Navigation", ["Home", "Favorites", "Care Guide", "Daily Care"])



# Updated Plant Database with 'beginner_friendly' and 'estimated_growth_days'
plants_data = [
    {
        "name": "Tulsi (Holy Basil)",
        "space": ["balcony", "window", "terrace"],
        "sunlight": ["partial", "full"],
        "water": ["low", "medium"],
        "image": "https://media.gettyimages.com/id/1359257193/photo/lush-green-aromatic-holy-basil-plant-looking-magnificent-ocimum-tenuiflorum-lamiaceae-family.jpg?s=1024x1024&w=gi&k=20&c=Oi-lKtpWM_QqLP1-8C8BaxUJPohjkMktZjBRKk62EvM=",
        "care": "Water twice a week. Needs sunlight 3-4 hrs/day.",
        "uses": "Boosts immunity, reduces stress, supports respiratory health.",
        "growth_process": "Germinate seeds indoors, transplant after 4 weeks, water every alternate day, prune regularly to promote bushy growth.",
        "beginner_friendly": True,
        "estimated_growth_days": 60
    },
    {
        "name": "Coriander",
        "space": ["balcony", "terrace", "window"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/1264427026/photo/growing-parsley-in-the-garden.jpg?s=1024x1024&w=gi&k=20&c=bAH7eFAQpOQZy5FXcUZiUB6Ifzc3avvv-V4Nk28r5W4=",
        "care": "Grows fast. Harvest leaves regularly.",
        "uses": "Rich in antioxidants, lowers blood sugar, good for skin.",
        "growth_process": "Sow seeds directly in soil, keep moist till germination, thin seedlings, harvest leaves after 3–4 weeks.",
        "beginner_friendly": True,
        "estimated_growth_days": 30
    },
    {
        "name": "Mint (Pudina)",
        "space": ["balcony", "window", "terrace"],
        "sunlight": ["partial", "shade"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/1216984727/photo/fresh-mint-plant-ayurveda-herb-organic.jpg?s=1024x1024&w=gi&k=20&c=n3pRwE6JoR_OuyWajGZhAdFf1PGedmRgGtx2UYrhUh0=",
        "care": "Water regularly. Pinch tops to grow more leaves.",
        "uses": "Aids digestion, freshens breath, soothes headaches.",
        "growth_process": "Plant stem cuttings in moist soil, keep soil damp, trim often to prevent overgrowth and encourage new shoots.",
        "beginner_friendly": True,
        "estimated_growth_days": 40
    },
    {
        "name": "Tomato",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["high"],
        "image": "https://media.gettyimages.com/id/171579643/photo/tomato-greenhouse.jpg?s=1024x1024&w=gi&k=20&c=TUr8artCrHjk5XzhuVJJ-USZwG9jljF8wsnEWjtJ4oQ=",
        "care": "Needs daily watering. Support plant with stick.",
        "uses": "Rich in Vitamin C, heart-healthy, improves skin health.",
        "growth_process": "Start seeds indoors 6-8 weeks before last frost, transplant outdoors in full sun, water regularly, support with stakes or cages, harvest when fruits are firm and red.",
        "beginner_friendly": False,
        "estimated_growth_days": 90
    },
    {
        "name": "Aloe Vera",
        "space": ["balcony", "window"],
        "sunlight": ["full", "partial"],
        "water": ["low"],
        "image": "https://media.gettyimages.com/id/182784203/photo/aloe-vera-plant.jpg?s=1024x1024&w=gi&k=20&c=G6kbUDlYoHnKT-tURnC-5cYL6bkJBd5xA6dpOkTpM40=",
        "care": "Very low maintenance. Water weekly.",
        "uses": "Soothes skin, supports digestion, improves oral health.",
        "growth_process": "Use pups from mother plant, plant in sandy soil, water once a week, avoid overwatering to prevent root rot.",
        "beginner_friendly": True,
        "estimated_growth_days": 75
    },
    {
        "name": "Spinach",
        "space": ["terrace", "balcony"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/169983791/photo/spinach.jpg?s=1024x1024&w=gi&k=20&c=FMh28QJl8meUK-1VKwQGa5RpjsIovUzy6amDZmypPzA=",
        "care": "Harvest in 30 days. Water every 2-3 days.",
        "uses": "Rich in iron, improves eyesight, boosts energy.",
        "growth_process": "Sow seeds directly in cool weather, keep soil moist, thin seedlings after sprouting, harvest outer leaves regularly to encourage new growth.",
        "beginner_friendly": True,
        "estimated_growth_days": 30
    },
    {
        "name": "Chili Plant",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/154276389/photo/red-green-peppers.jpg?s=1024x1024&w=gi&k=20&c=hgbR1owIXqTNoviiA-EwSr3pW4Kap74ya-y-37o5ssU=",
        "care": "Fertilize monthly. Keep in sunlight.",
        "uses": "Not Available",
        "growth_process": "Start seeds indoors or directly in warm soil, transplant when 4–6 inches tall, water consistently, provide full sun, harvest when chilies turn bright red or green depending on variety.",
        "beginner_friendly": False,
        "estimated_growth_days": 80
    },
    {
        "name": "Lemongrass",
        "space": ["terrace"],
        "sunlight": ["full"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/2161967118/photo/lemongrass.jpg?s=1024x1024&w=gi&k=20&c=ntAwP5Zg0JJ4sCQ-blrd91rXw1qZ3VDHjlEe0Vek0x8=",
        "care": "Harvest leaves. Grows tall, so needs big pot.",
        "uses": "Relieves anxiety, boosts immunity, detoxifies the body.",
        "growth_process": "Plant stalks in well-draining soil with full sunlight, keep soil moist until roots develop, divide clumps annually, harvest by cutting mature stalks at the base.",
        "beginner_friendly": True,
        "estimated_growth_days": 100
    },
    {
        "name": "Curry Leaves (Kadi Patta)",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/1150140818/photo/curry-leaf-plant.jpg?s=1024x1024&w=gi&k=20&c=KFPSY-Dk686ho8NrSBg7yxPvliznuUnyBaavATbQWxU=",
        "care": "Needs sunlight. Prune regularly.",
        "uses": "Good for eyesight, supports hair growth, anti-inflammatory.",
        "growth_process": "Grow from seeds or stem cuttings, place in sunny area, water moderately, pinch top leaves to promote bushy growth, harvest regularly after plant matures (1–2 years).",
        "beginner_friendly": False,
        "estimated_growth_days": 120
    },
    {
        "name": "Ginger",
        "space": ["balcony", "terrace"],
        "sunlight": ["partial"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/128112512/photo/pile-of-ginger-root-on-green-placemat.jpg?s=1024x1024&w=gi&k=20&c=Lxbo7S7XuaGmfz0e3ECPDbeBB1_NzTFvuIP8qp9mXIE=",
        "care": "Use grow bag. Keep soil moist.",
        "uses": "Ginger is a fragrant kitchen spice.",
        "growth_process": "Plant ginger rhizomes in moist, well-drained soil with indirect sunlight, cover lightly with soil, water gently, shoots appear in 2–3 weeks, harvest after 8–10 months when leaves yellow.",
        "beginner_friendly": False,
        "estimated_growth_days": 150
    }
]

#care calendar
def care_caledar():
    # --- CARE CALENDAR FEATURE ---
    
    # Initialize care calendar in session state if not already
    if "care_calendar" not in st.session_state:
        st.session_state.care_calendar = {}
    
    # Unique key for each plant
    plant_key = plant['name']
    
    # Show calendar inputs for watering and fertilizing
    with st.expander("🗓️ Add to Care Calendar"):
        watering_date = st.date_input(
            f"💧 Next Watering Date for {plant_key}", key=f"{plant_key}_water"
        )
        fertilizing_date = st.date_input(
            f"🌿 Next Fertilizing Date for {plant_key}", key=f"{plant_key}_fertilizer"
        )
    
        # Save dates to session state
        st.session_state.care_calendar[plant_key] = {
            "watering": watering_date,
            "fertilizer": fertilizing_date
        }
    
    # Display selected dates
    if plant_key in st.session_state.care_calendar:
        st.info(f"📅 Care Schedule for {plant_key}:")
        st.write(f"💧 Water on: {st.session_state.care_calendar[plant_key]['watering']}")
        st.write(f"🌿 Fertilize on: {st.session_state.care_calendar[plant_key]['fertilizer']}")


#seed cost calculation 
def seed_cost():
    with st.expander("🌱 Cost Estimator"):
        seed_cost = st.number_input(f"Seed Cost for {plant['name']} (₹)", min_value=0.0, value=20.0, step=1.0, key=f"seed_{plant['name']}")
        water_cost = st.number_input("Monthly Water Cost (₹)", min_value=0.0, value=10.0, step=1.0, key=f"water_{plant['name']}")
        fertilizer_cost = st.number_input("Monthly Fertilizer Cost (₹)", min_value=0.0, value=15.0, step=1.0, key=f"fert_{plant['name']}")
        months = st.number_input("Growing Duration (in months)", min_value=1, max_value=24, value=3, step=1, key=f"months_{plant['name']}")
    
        total_cost = seed_cost + (water_cost + fertilizer_cost) * months
        st.success(f"💰 Estimated Total Cost: ₹{total_cost:.2f}")

#plant progress
def plant_progress():
    with st.expander("📸 Plant Growth Tracker / Journal"):
        if 'plant_journal' not in st.session_state:
            st.session_state.plant_journal = {}
    
        uploaded_img = st.file_uploader(f"Upload Progress Image for {plant['name']}", type=["png", "jpg", "jpeg"], key=f"upload_{plant['name']}")
        journal_note = st.text_area(f"Write today's note for {plant['name']}", key=f"note_{plant['name']}")
    
        if st.button(f"Save Entry for {plant['name']}", key=f"save_journal_{plant['name']}"):
            if plant['name'] not in st.session_state.plant_journal:
                st.session_state.plant_journal[plant['name']] = []
            st.session_state.plant_journal[plant['name']].append({
                "image": uploaded_img,
                "note": journal_note
            })
            st.success("Journal entry saved!")
    
        # Show previous journal entries (basic)
        entries = st.session_state.plant_journal.get(plant['name'], [])
        if entries:
            st.markdown("### 📅 Previous Entries")
            for idx, entry in enumerate(entries):
                if entry['image']:
                    st.image(entry['image'], width=150, caption=f"Entry {idx+1}")
                if entry['note']:
                    st.markdown(f"📝 {entry['note']}")
                st.markdown("---")


# --- Plant of the Day ---
random.seed(str(date.today()))  # Ensures same plant is shown throughout the day
plant_of_the_day = random.choice(plants_data)

st.markdown("## 🌟 Plant of the Day")
st.image(plant_of_the_day["image"], width=150)
st.write(f"**{plant_of_the_day['name']}**")
st.write(f"**Sunlight Needs:** {', '.join(plant_of_the_day['sunlight'])}")
st.write(f"**Water Needs:** {', '.join(plant_of_the_day['water'])}")
st.write(f"**Care Tip:** {plant_of_the_day['care']}")
st.markdown("---")



# User Input
space = st.selectbox("Where do you want to grow?", ["Select", "balcony", "terrace", "window"])
sunlight = st.selectbox("How much sunlight do you get?", ["Select", "full", "partial", "shade"])
water = st.selectbox("How much water can you provide?", ["Select", "low", "medium", "high"])
is_beginner = st.checkbox("Show only beginner-friendly plants 👶🌱")
max_days = st.slider("Maximum days to harvest 🌾", 20, 180, 90)


# Button and Matching Logic
if st.button("Suggest Plants 🌱"):
    if "Select" in [space, sunlight, water]:
        st.warning("Please choose all 3 options.")
    else:
        matched_plants = []
        for plant in plants_data:
            if (
                space in plant["space"] and
                sunlight in plant["sunlight"] and
                water in plant["water"] and
                (not is_beginner or plant.get("beginner_friendly", False)) and
                plant.get("estimated_growth_days", 999) <= max_days
            ):
                matched_plants.append(plant)

        if matched_plants:
            st.success(f"Found {len(matched_plants)} suitable plants!")
            for plant in matched_plants:
                st.image(plant["image"], width=300)
                st.markdown(f"### 🌿 {plant['name']}")
                st.write(f"**Space:** {', '.join(plant['space'])}")
                st.write(f"**Sunlight:** {', '.join(plant['sunlight'])}")
                st.write(f"**Water Needs:** {', '.join(plant['water'])}")
                st.write(f"**Health Uses:** {plant['uses']}")
                st.write(f"**Care Instructions:** {plant['care']}")
                st.write(f"**Growth Process:** {plant['growth_process']}")
                st.write(f"**⏳ Estimated Harvest Time:** {plant['estimated_growth_days']} days")
                seed_cost()
                care_caledar()
                plant_progress()
                
                
                # --- Inside your plant loop (after showing image, name, etc.) ---
                if st.button(f"⭐ Add to Favorites", key=f"fav_{plant['name']}"):
                    if plant["name"] not in st.session_state["favorites"]:
                        st.session_state["favorites"].append(plant["name"])
                        st.success(f"Added {plant['name']} to Favorites!")
        else:
            st.error("No matching plants found for this combination.")


#quiz session
def quiz_session():
    # --- Mini Quiz Section ---
    st.markdown("## 🧠 Quick Plant Quiz")
    quiz_question = "Which part of the plant makes food using sunlight?"
    options = ["Roots", "Stem", "Leaves", "Flowers"]
    correct_answer = "Leaves"
    
    user_answer = st.radio(quiz_question, options, key="quiz")
    
    if st.button("Submit Answer", key="submit_quiz"):
        if user_answer == correct_answer:
            st.success("✅ Correct! Leaves perform photosynthesis.")
        else:
            st.error("❌ Oops! The correct answer is Leaves.")


quiz_session()




# --- Feedback ---
st.markdown("## 💬 We'd Love Your Feedback")
feedback = st.text_area("Share your thoughts about this app:")
if st.button("Submit Feedback", key="feedback"):
    st.success("Thanks for your feedback! 🌼")


# Display saved favorites
if 'favorites' in st.session_state and st.session_state.favorites:
    st.markdown("## 💾 Your Saved Plants")
    for fav in st.session_state.favorites:
        st.image(fav["image"], width=200)
        st.write(f"**{fav['name']}** - Harvest in {fav['estimated_growth_days']} days")
        st.markdown("---")


