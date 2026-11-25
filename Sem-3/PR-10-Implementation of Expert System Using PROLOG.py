# Expert System for Medical Diagnosis

# Enter patient symptoms
symptoms = input("Enter symptoms separated by commas: ")
symptoms = symptoms.lower().replace(" ", "").split(",")

# Check diseases
if "sneezing" in symptoms and "runny_nose" in symptoms:
    print("Possible Disease: Common Cold")

if "fever" in symptoms and "cough" in symptoms and "body_ache" in symptoms:
    print("Possible Disease: Flu")

if "fever" in symptoms and "chills" in symptoms:
    print("Possible Disease: Malaria")

if "fever" in symptoms and "headache" in symptoms and "joint_pain" in symptoms:
    print("Possible Disease: Dengue")

if "fever" in symptoms and "stomach_pain" in symptoms:
    print("Possible Disease: Typhoid")

if "wheezing" in symptoms and "breathlessness" in symptoms:
    print("Possible Disease: Asthma")

if "sneezing" in symptoms and "itching" in symptoms:
    print("Possible Disease: Allergy")

if "severe_headache" in symptoms and "nausea" in symptoms:
    print("Possible Disease: Migraine")

if "vomiting" in symptoms and "diarrhea" in symptoms:
    print("Possible Disease: Gastroenteritis")

if "red_eyes" in symptoms and "itching" in symptoms:
    print("Possible Disease: Conjunctivitis")

print("Expert System Completed.")
