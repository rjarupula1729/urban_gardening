import streamlit as st

# Title
st.title("Urban Gardening – Plant Recommender 🌱")

# User Inputs
space = st.selectbox("Select your available space:", ["Balcony", "Terrace", "Window"])
sunlight = st.selectbox("How much sunlight does your space get?", ["High", "Medium", "Low"])
watering = st.selectbox("How often can you water the plants?", ["Daily", "Every 2 Days", "Weekly"])
experience = st.selectbox("Gardening experience:", ["Beginner", "Intermediate", "Advanced"])
# Sample plant dataset
plant_data = [
    {
        "name": "Tulsi",
        "space": ["Balcony", "Window"],
        "sunlight": "High",
        "watering": "Daily",
        "how_to_grow": "Use a small pot with drainage holes and place in a sunny spot.",
        "when_to_grow": "Throughout the year",
        "care": "Water daily and trim regularly."
    },
    {
        "name": "Mint",
        "space": ["Balcony", "Terrace"],
        "sunlight": "Medium",
        "watering": "Every 2 Days",
        "how_to_grow": "Plant cuttings in a pot with moist soil. Keep partially shaded.",
        "when_to_grow": "Spring to Early Summer",
        "care": "Water when topsoil is dry."
    },
    {
        "name": "Coriander",
        "space": ["Balcony", "Window", "Terrace"],
        "sunlight": "Medium",
        "watering": "Daily",
        "how_to_grow": "Sow seeds in moist soil. Keep in semi-sunlight.",
        "when_to_grow": "October to March",
        "care": "Thin seedlings and water daily."
    },
    {
        "name": "Aloe Vera",
        "space": ["Terrace"],
        "sunlight": "High",
        "watering": "Weekly",
        "how_to_grow": "Use sandy soil and keep in direct sun.",
        "when_to_grow": "All year round",
        "care": "Do not overwater."
    }
]

st.button("Get Plant Suggestions")

# Filter logic
matched_plants = []
for plant in plant_data:
    if (space in plant["space"]) and (sunlight == plant["sunlight"]) and (watering == plant["watering"]):
        matched_plants.append(plant)

# Display results
st.subheader("Suggested Plants for You 🌿")

if matched_plants:
    for plant in matched_plants:
        st.markdown(f"### 🌼 {plant['name']}")
        st.markdown(f"**How to Grow:** {plant['how_to_grow']}")
        st.markdown(f"**Best Time to Grow:** {plant['when_to_grow']}")
        st.markdown(f"**Care Tips:** {plant['care']}")
        st.markdown("---")
else:
    st.warning("Sorry, we couldn't find a perfect match. Try changing your inputs.")

