
# Expert System for Medical Diagnosis

# Step 1: Take symptoms from user
symptoms = input("Enter symptoms separated by commas: ").lower().split(",")

# Remove extra spaces
symptoms = [s.strip() for s in symptoms]

# Step 2: Check symptoms using if-elif rules

if "runny nose" in symptoms and "sneezing" in symptoms and "sore throat" in symptoms:
    disease = "Common Cold"

elif "fever" in symptoms and "cough" in symptoms and "body ache" in symptoms:
    disease = "Influenza"

elif "fever" in symptoms and "chills" in symptoms and "sweating" in symptoms:
    disease = "Malaria"

elif "fever" in symptoms and "joint pain" in symptoms and "rash" in symptoms:
    disease = "Dengue"

elif "headache" in symptoms and "nausea" in symptoms and "light sensitivity" in symptoms:
    disease = "Migraine"

elif "wheezing" in symptoms and "breathlessness" in symptoms and "cough" in symptoms:
    disease = "Asthma"

elif "fever" in symptoms and "rash" in symptoms and "itchy blisters" in symptoms:
    disease = "Chickenpox"

elif "vomiting" in symptoms and "diarrhea" in symptoms and "stomach cramps" in symptoms:
    disease = "Gastroenteritis"

elif "sneezing" in symptoms and "itchy eyes" in symptoms and "runny nose" in symptoms:
    disease = "Allergic Rhinitis"

elif "burning urination" in symptoms and "frequent urination" in symptoms and "lower belly pain" in symptoms:
    disease = "Urinary Tract Infection"

else:
    disease = "No matching disease found"

# Step 3: Display result
print("Possible Disease:", disease)
print("Note: This is not a medical diagnosis.")
