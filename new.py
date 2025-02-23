import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Open the webcam
cap = cv2.VideoCapture(0)

# Define coordinates for different gestures (modify these)
coordinates = {
    0: (689, 306),  # No fingers raised → Click at (200, 200)
    2: (474, 306),  # Two fingers raised → Click at (500, 300)
    5: (254, 308)   # Five fingers raised → Click at (800, 400)
}

def count_fingers(hand_landmarks):
    """Count the number of raised fingers based on hand landmarks."""
    finger_tips = [8, 12, 16, 20]  # Tip indexes for four fingers
    thumb_tip = 4  # Thumb tip index
    count = 0
    
    # Check each finger
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1

    # Check the thumb
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 2].x:
        count += 1

    return count

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count fingers
            num_fingers = count_fingers(hand_landmarks)
            cv2.putText(frame, f"Fingers: {num_fingers}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Check if the detected number of fingers is in our set
            if num_fingers in coordinates:
                x, y = coordinates[num_fingers]
                pyautogui.click(x, y)
                cv2.putText(frame, f"Click at ({x}, {y})", (x, y), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
