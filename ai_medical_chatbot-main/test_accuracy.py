from utils import process_image
# Define your test cases
test_cases = [
    # (image, question, diagnosis_keywords, treatment_keywords)
    ("test1.jpg", "What is this condition, how can it be treated, and why did it occur?", ["acne", "pimples","rashes"], ["benzoyl", "salicylic", "retinoid"]),
    ("test2.jpg", "What is this condition, how can it be treated, and why did it occur?", ["dandruff", "flakes", "scalp","sebaceous gland"], ["anti-dandruff", "shampoo"]),
    ("test3.webp", "What is this condition, how can it be treated, and why did it occur?", ["tinea", "pedis", "athlete"], ["antifungal", "clotrimazole"]),
    ("test4.webp", "What is this condition, how can it be treated, and why did it occur?", ["onychomycosis", "fungal", "nail"], ["terbinafine", "antifungal"]),
    ("test5.jpg", "What is this condition, how can it be treated, and why did it occur?", ["venous ulcer", "stasis dermatitis","infection"], ["compression therapy", "wound care", "caused by poor blood flow in leg veins"]),
    ("test6.jpg", "What is this condition, how can it be treated, and why did it occur?", ["rash", "skin irritation","itchy","bug bite"], ["apply cold compress", "antihistamine cream", "caused by insect sting or bite"]),
    ("test7.png", "What is this condition, how can it be treated, and why did it occur?", ["conjunctivitis", "pink", "eye"], ["antibiotic", "drops"]),
    ("test8.webp", "What is this condition, how can it be treated, and why did it occur?", ["eczema", "dermatitis","blisters"], ["moisturizer", "steroid", "cream"]),
    ("test9.jpeg", "What is this condition, how can it be treated, and why did it occur?", ["fibula fracture", "ankle fracture", "distal fibula", "transverse fracture", "oblique fracture", "displaced fracture"], ["immobilization", "cast", "surgery", "reduction", "rest", "pain management"]),
    ("test10.png", "What is this condition, how can it be treated, and why did it occur?", ["epistaxis", "nosebleed"], ["apply pressure", "lean forward", "refer if persistent"]),
]

results = {
    "llama11b": {"correct": 0, "total": 0},
    "llama90b": {"correct": 0, "total": 0}
}

reason_keywords = ["caused by", "due to", "because", "triggered by", "as a result of"]

for image_file, question, diagnosis_keywords, treatment_keywords in test_cases:
    print(f"\nTesting on: {image_file} | Question: {question}")
    response = process_image(image_file, question)

    for model_key in ["llama11b", "llama90b"]:
        output = response.get(model_key, "").lower()
        diagnosis_found = any(k in output for k in diagnosis_keywords)
        treatment_found = any(k in output for k in treatment_keywords)
        reason_found = any(k in output for k in reason_keywords)

        results[model_key]["total"] += 1
        if diagnosis_found and treatment_found and reason_found:
            results[model_key]["correct"] += 1
            print(f"[FULL PASS] {model_key}: Diagnosis, Treatment & Reason found.")
        elif diagnosis_found and treatment_found:
            results[model_key]["correct"] += 0.66
            print(f"[PARTIAL PASS] {model_key}: Diagnosis & Treatment found.")
        elif diagnosis_found or treatment_found:
            results[model_key]["correct"] += 0.33
            print(f"[MINIMAL PASS] {model_key}: Partial info found.")
        else:
            print(f"[FAIL] {model_key}: No relevant info found.")

        print(f"    Response: {output[:200]}...")

print("\n=== Accuracy Summary ===")
for model_key, score in results.items():
    accuracy = (score["correct"] / score["total"]) * 100 if score["total"] else 0
    print(f"{model_key} Accuracy: {accuracy:.2f}%")