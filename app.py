import streamlit as st

# Title
st.title("Urban Gardening – Plant Recommender 🌱")

# User Inputs
space = st.selectbox("Select your available space:", ["Balcony", "Terrace", "Window"])
sunlight = st.selectbox("How much sunlight does your space get?", ["High", "Medium", "Low"])
watering = st.selectbox("How often can you water the plants?", ["Daily", "Every 2 Days", "Weekly"])

# Sample plant dataset
plant_data = [
    {
        "name": "Mint",
        "space": ["Balcony", "Window"],
        "sunlight": ["Medium", "High"],
        "water": ["Medium"],
        "details": "Grows well in pots. Keep moist. Harvest frequently.",
    },
    {
        "name": "Coriander",
        "space": ["Window", "Balcony"],
        "sunlight": ["Medium"],
        "water": ["Low", "Medium"],
        "details": "Easy to grow. Water every other day. Use fresh leaves.",
    },
    {
        "name": "Spinach",
        "space": ["Balcony", "Terrace"],
        "sunlight": ["Low", "Medium"],
        "water": ["Medium"],
        "details": "Grows quickly. Keep soil moist and partial sunlight.",
    },
    {
        "name": "Aloe Vera",
        "space": ["Window", "Terrace"],
        "sunlight": ["High"],
        "water": ["Low"],
        "details": "Medicinal plant. Needs full sun. Water weekly.",
    },
    {
        "name": "Tomato",
        "space": ["Balcony", "Terrace"],
        "sunlight": ["High"],
        "water": ["High"],
        "details": "Requires strong sunlight. Regular watering. Use deep pots.",
    },
    {
        "name": "Chili",
        "space": ["Terrace", "Balcony"],
        "sunlight": ["High"],
        "water": ["Medium"],
        "details": "Spicy plant. Needs sunlight. Avoid overwatering.",
    },
    {
        "name": "Tulsi (Basil)",
        "space": ["Window", "Balcony"],
        "sunlight": ["Medium", "High"],
        "water": ["Medium"],
        "details": "Sacred and medicinal. Easy to grow. Daily watering.",
    },
    {
        "name": "Fenugreek (Methi)",
        "space": ["Balcony"],
        "sunlight": ["Medium"],
        "water": ["Medium"],
        "details": "Short growth cycle. Good for indoor pots.",
    },
    {
        "name": "Lettuce",
        "space": ["Window", "Balcony"],
        "sunlight": ["Low", "Medium"],
        "water": ["High"],
        "details": "Cool weather crop. Needs frequent watering.",
    },
    {
        "name": "Curry Leaves",
        "space": ["Terrace"],
        "sunlight": ["High"],
        "water": ["Medium"],
        "details": "Aromatic leaves. Needs full sun and weekly watering.",
    },
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

