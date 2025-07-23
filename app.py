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
        "image": "https://media.gettyimages.com/id/1359257193/photo/lush-green-aromatic-holy-basil-plant-looking-magnificent-ocimum-tenuiflorum-lamiaceae-family.jpg?s=1024x1024&w=gi&k=20&c=Oi-lKtpWM_QqLP1-8C8BaxUJPohjkMktZjBRKk62EvM=",
        "care": "Water twice a week. Needs sunlight 3-4 hrs/day.",
        "uses": "Boosts immunity, reduces stress, supports respiratory health."
    },
    {
        "name": "Coriander",
        "space": ["balcony", "terrace", "window"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/1264427026/photo/growing-parsley-in-the-garden.jpg?s=1024x1024&w=gi&k=20&c=bAH7eFAQpOQZy5FXcUZiUB6Ifzc3avvv-V4Nk28r5W4=",
        "care": "Grows fast. Harvest leaves regularly.",
        "uses": "Rich in antioxidants, lowers blood sugar, good for skin."
    },
    {
        "name": "Mint (Pudina)",
        "space": ["balcony", "window", "terrace"],
        "sunlight": ["partial", "shade"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/1216984727/photo/fresh-mint-plant-ayurveda-herb-organic.jpg?s=1024x1024&w=gi&k=20&c=n3pRwE6JoR_OuyWajGZhAdFf1PGedmRgGtx2UYrhUh0=",
        "care": "Water regularly. Pinch tops to grow more leaves.",
        "uses": "Aids digestion, freshens breath, soothes headaches."
    },
    {
        "name": "Tomato",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["high"],
        "image": "https://media.gettyimages.com/id/171579643/photo/tomato-greenhouse.jpg?s=1024x1024&w=gi&k=20&c=TUr8artCrHjk5XzhuVJJ-USZwG9jljF8wsnEWjtJ4oQ=",
        "care": "Needs daily watering. Support plant with stick.",
        "uses": "Rich in Vitamin C, heart-healthy, improves skin health."
    },
    {
        "name": "Aloe Vera",
        "space": ["balcony", "window"],
        "sunlight": ["full", "partial"],
        "water": ["low"],
        "image": "https://media.gettyimages.com/id/182784203/photo/aloe-vera-plant.jpg?s=1024x1024&w=gi&k=20&c=G6kbUDlYoHnKT-tURnC-5cYL6bkJBd5xA6dpOkTpM40=",
        "care": "Very low maintenance. Water weekly.",
        "uses": "Soothes skin, supports digestion, improves oral health."
    },
    {
        "name": "Spinach",
        "space": ["terrace", "balcony"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/169983791/photo/spinach.jpg?s=1024x1024&w=gi&k=20&c=FMh28QJl8meUK-1VKwQGa5RpjsIovUzy6amDZmypPzA=",
        "care": "Harvest in 30 days. Water every 2-3 days.",
        "uses": "Rich in iron, improves eyesight, boosts energy."
    },
    {
        "name": "Chili Plant",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/154276389/photo/red-green-peppers.jpg?s=1024x1024&w=gi&k=20&c=hgbR1owIXqTNoviiA-EwSr3pW4Kap74ya-y-37o5ssU=",
        "care": "Fertilize monthly. Keep in sunlight.",
        "uses": "Not Available"
    },
    {
        "name": "Lemongrass",
        "space": ["terrace"],
        "sunlight": ["full"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/2161967118/photo/lemongrass.jpg?s=1024x1024&w=gi&k=20&c=ntAwP5Zg0JJ4sCQ-blrd91rXw1qZ3VDHjlEe0Vek0x8=",
        "care": "Harvest leaves. Grows tall, so needs big pot.",
        "uses": "Relieves anxiety, boosts immunity, detoxifies the body."
    },
    {
        "name": "Curry Leaves (Kadi Patta)",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/1150140818/photo/curry-leaf-plant.jpg?s=1024x1024&w=gi&k=20&c=KFPSY-Dk686ho8NrSBg7yxPvliznuUnyBaavATbQWxU=",
        "care": "Needs sunlight. Prune regularly.",
        "uses": "Good for eyesight, supports hair growth, anti-inflammatory."
    },
    {
        "name": "Ginger",
        "space": ["balcony", "terrace"],
        "sunlight": ["partial"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/128112512/photo/pile-of-ginger-root-on-green-placemat.jpg?s=1024x1024&w=gi&k=20&c=Lxbo7S7XuaGmfz0e3ECPDbeBB1_NzTFvuIP8qp9mXIE=",
        "care": "Use grow bag. Keep soil moist.",
        "uses": "Ginger is a fragrant kitchen spice."
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
                st.image(plant["image"], width=300)
                st.markdown(f"### 🌿 {plant['name']}")
                st.write(f"**Space:** {', '.join(plant['space'])}")
                st.write(f"**Sunlight:** {', '.join(plant['sunlight'])}")
                st.write(f"**Water Needs:** {', '.join(plant['water'])}")
                st.markdown(f"**Health Uses:** {plant['uses']}")
                st.write(f"**Care Instructions:** {plant['care']}")
                st.markdown("---")
        else:
            st.error("No matching plants found for this combination.")
