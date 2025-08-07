import streamlit as st # type: ignore
import datetime

st.set_page_config(page_title="🐶 Pet Dog Care App", layout="centered")

st.title("🐾 Pet Dog Care Web App")
st.markdown("Welcome to your dog's personal care assistant!")

st.header("📅 Dog Health Tracker")

st.subheader("🩺 Vaccination Reminder")
last_vaccine_date = st.date_input("Last Vaccination Date", value=None)

if last_vaccine_date:
    next_vaccine_date = last_vaccine_date + datetime.timedelta(days=365)
    st.success(f"Next vaccination is due on: {next_vaccine_date.strftime('%d %B %Y')}")
else:
    st.info("Please select the last vaccination date.")

st.subheader("💊 Deworming Schedule")
last_deworm_date = st.date_input("Last Deworming Date", value=None)

if last_deworm_date:
    next_deworm_date = last_deworm_date + datetime.timedelta(days=90)
    st.success(f"Next deworming is due on: {next_deworm_date.strftime('%d %B %Y')}")
else:
    st.info("Please select the last deworming date.")


st.header("🍖 Custom Diet Planner")

age = st.slider("Dog's Age (in years)", 0, 20, 2)
weight = st.number_input("Dog's Weight (in kg)", min_value=1, max_value=100, value=15)
breed_input = st.text_input("Enter Your Dog's Breed (e.g., Labrador, Shih Tzu)").strip().lower()
activity = st.selectbox("Activity Level", ["Lazy", "Moderate", "Active", "Working Dog"])

breed_size_map = {
    "golden retriever": "Large",
    "labrador": "Large",
    "german shepherd": "Large",
    "rottweiler": "Large",
    "great dane": "Large",
    "husky": "Large",
    "doberman": "Large",
    "boxer": "Large",
    "pug": "Small",
    "shihtzu": "Small",
    "shih tzu": "Small",
    "chihuahua": "Small",
    "pomeranian": "Small",
    "dachshund": "Small",
    "beagle": "Medium",
    "bulldog": "Medium",
    "cocker spaniel": "Medium",
    "border collie": "Medium",
    "spaniel": "Medium"
}

if breed_input:
    breed_size = breed_size_map.get(breed_input)
    if breed_size:
        st.info(f"✅ Detected breed size: {breed_size}")
    else:
        st.warning("⚠️ Breed not recognized. Defaulting to 'Medium'")
        breed_size = "Medium"
else:
    breed_size = None

if st.button("🦴 Show Diet Plan"):
    if not breed_size:
        st.error("❗ Please enter your dog's breed to continue.")
    else:
        st.subheader("🏠 Home-Cooked Food Suggestions")

        if weight < 10:
            st.markdown("- Cooked rice with chicken & carrots")
            st.markdown("- Mashed pumpkin & boiled eggs")
        elif weight < 25:
            st.markdown("- Chicken + sweet potatoes + spinach")
            st.markdown("- Lentils with rice and minced meat")
        else:
            st.markdown("- Brown rice + beef + broccoli")
            st.markdown("- Oatmeal with eggs and vegetables")

        st.subheader("🛒 Branded Dog Food Suggestions")
        if breed_size == "Small":
            st.markdown("- Royal Canin Mini Adult")
            st.markdown("- Pedigree Small Breed")
        elif breed_size == "Medium":
            st.markdown("- Drools Chicken & Egg")
            st.markdown("- Royal Canin Medium Adult")
        else:
            st.markdown("- Farmina N&D Large Breed")
            st.markdown("- Purina Pro Plan Large Breed")

        st.info("💡 Tip: Always consult a vet before changing your dog's diet.")

st.markdown("---")
st.caption("🐶 Built with ❤️ using Python and Streamlit")
