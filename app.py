import streamlit as st

# 1. Title
st.title("🌿 Urban Gardening Helper")
st.subheader("Find plants suitable for your urban space 🌇")

# 2. JSON-like plant database
plants_data = [
    {
        "name": "Tulsi (Holy Basil)",
        "space": ["balcony", "window", "terrace"],
        "sunlight": ["partial", "full"],
        "water": ["low", "medium"],
        "care": "Water twice a week. Needs sunlight 3-4 hrs/day."
    },
    {
        "name": "Coriander",
        "space": ["balcony", "terrace", "window"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "care": "Grows fast. Harvest leaves regularly."
    },
    {
        "name": "Mint (Pudina)",
        "space": ["balcony", "window", "terrace"],
        "sunlight": ["partial", "shade"],
        "water": ["medium", "high"],
        "care": "Water regularly. Pinch tops to grow more leaves."
    },
    {
        "name": "Tomato",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["high"],
        "care": "Needs daily watering. Support plant with stick."
    },
    {
        "name": "Aloe Vera",
        "space": ["balcony", "window"],
        "sunlight": ["full", "partial"],
        "water": ["low"],
        "care": "Very low maintenance. Water weekly."
    },
    {
        "name": "Spinach",
        "space": ["terrace", "balcony"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "care": "Harvest in 30 days. Water every 2-3 days."
    },
    {
        "name": "Chili Plant",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "care": "Fertilize monthly. Keep in sunlight."
    },
    {
        "name": "Lemongrass",
        "space": ["terrace"],
        "sunlight": ["full"],
        "water": ["medium", "high"],
        "care": "Harvest leaves. Grows tall, so needs big pot."
    },
    {
        "name": "Curry Leaves (Kadi Patta)",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "care": "Needs sunlight. Prune regularly."
    },
    {
        "name": "Ginger",
        "space": ["balcony", "terrace"],
        "sunlight": ["partial"],
        "water": ["medium", "high"],
        "care": "Use grow bag. Keep soil moist."
    }
]

# 3. User Input
space = st.selectbox("Where do you want to grow?", ["Select", "balcony", "terrace", "window"])
sunlight = st.selectbox("How much sunlight do you get?", ["Select", "full", "partial", "shade"])
water = st.selectbox("How much water can you provide?", ["Select", "low", "medium", "high"])

# 4. Button and Matching Logic
if st.button("Suggest Plants 🌱"):
    if "Select" in [space, sunlight, water]:
        st.warning("Please choose all 3 options.")
    else:
        matched_plants = []
        for plant in plants_data:
            if space in plant["space"] and sunlight in plant["sunlight"] and water in plant["water"]:
                matched_plants.append(plant)

        if matched_plants:
            st.success(f"Found {len(matched_plants)} suitable plants!")
            for plant in matched_plants:
                st.markdown(f"### 🌿 {plant['name']}")
                st.write(f"**Space:** {', '.join(plant['space'])}")
                st.write(f"**Sunlight:** {', '.join(plant['sunlight'])}")
                st.write(f"**Water Needs:** {', '.join(plant['water'])}")
                st.write(f"**Care Instructions:** {plant['care']}")
                st.markdown("---")
        else:
            st.error("No matching plants found for this combination.")
