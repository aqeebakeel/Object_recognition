import pandas as pd
import random
from datetime import datetime

# Data Generation
data = []
gestures = ["Standing", "Hand Raised", "Aiming", "Walking"]
actions = ["Fire", "Ignore", "Alert"]
lighting = ["Bright", "Dim", "Night"]

for _ in range(1000):  # Generating 1000 detections
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detected_object = "Human" if random.random() > 0.1 else "No Human"
    classification = random.choice(["Friendly", "Enemy"]) if detected_object == "Human" else None
    confidence_score = round(random.uniform(0.7, 1.0), 2) if detected_object == "Human" else 0
    gesture = random.choice(gestures) if detected_object == "Human" else None
    action_triggered = random.choice(actions) if classification == "Enemy" else "Ignore"
    accuracy = "Yes" if random.random() > 0.9 else "No"
    response_time = random.randint(150, 300) if detected_object == "Human" else None
    lighting_condition = random.choice(lighting)
    obstacle_presence = "Yes" if random.random() > 0.2 else "No"

    data.append([timestamp, detected_object, classification, confidence_score, gesture, action_triggered, accuracy, response_time, lighting_condition, obstacle_presence])

# Convert to DataFrame and Save
df = pd.DataFrame(data, columns=["Timestamp", "Detected Object", "Classification", "Confidence Score", "Gesture", "Action Triggered", "Accuracy", "Response Time", "Lighting Condition", "Obstacle Presence"])
df.to_csv("rover_detection_data.csv", index=False)

print("Dataset generated successfully!")
