
% EXPERIMENT 10: Medical Expert System

% Step 1: Define sample symptoms
% Change these facts to test different conditions

symptom(fever).
symptom(cough).
symptom(body_ache).
symptom(fatigue).

% Step 2: Define rules for 10 diseases

% 1. Common Cold
diagnosis(common_cold) :-
    symptom(sneezing),
    symptom(runny_nose),
    symptom(sore_throat).

% 2. Flu
diagnosis(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_ache).

% 3. Malaria
diagnosis(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating).

% 4. Dengue
diagnosis(dengue) :-
    symptom(fever),
    symptom(headache),
    symptom(joint_pain).

% 5. Typhoid
diagnosis(typhoid) :-
    symptom(fever),
    symptom(stomach_pain),
    symptom(weakness).

% 6. Asthma
diagnosis(asthma) :-
    symptom(wheezing),
    symptom(breathlessness),
    symptom(chest_tightness).

% 7. Allergy
diagnosis(allergy) :-
    symptom(sneezing),
    symptom(itching),
    symptom(watery_eyes).

% 8. Migraine
diagnosis(migraine) :-
    symptom(severe_headache),
    symptom(nausea),
    symptom(light_sensitivity).

% 9. Gastroenteritis
diagnosis(gastroenteritis) :-
    symptom(vomiting),
    symptom(diarrhea),
    symptom(stomach_pain).

% 10. Conjunctivitis
diagnosis(conjunctivitis) :-
    symptom(red_eyes),
    symptom(itching),
    symptom(eye_discharge).
