import cv2
import mediapipe as mp
import time
import os
from gestures import recognize_gesture
from youtube_control import execute_action, GESTURE_ACTIONS
from utils import GestureSmoother, overlay_icon

def main():
    # Initialize Mediapipe Hands
    try:
        import mediapipe.python.solutions.hands as mp_hands
        import mediapipe.python.solutions.drawing_utils as mp_draw
    except (ImportError, AttributeError):
        try:
            import mediapipe.solutions.hands as mp_hands
            import mediapipe.solutions.drawing_utils as mp_draw
        except (ImportError, AttributeError):
            # Final fallback to standard mp object
            mp_hands = mp.solutions.hands
            mp_draw = mp.solutions.drawing_utils

    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    
    # Gesture smoothing helper
    smoother = GestureSmoother(max_len=5)

    # Icon mapping for UI overlay
    ICON_MAPPING = {
        "Volume Up": "assets/volume_up.png",
        "Volume Down": "assets/volume_down.png",
        "Play/Pause": "assets/play_pause.png",
        "Mute": "assets/mute.png",
        "Fullscreen": "assets/fullscreen.png",
        "Scroll Up": "assets/scroll_up.png",
        "Scroll Down": "assets/scroll_down.png"
    }

    print("--- YouTube Gesture Controller Started ---")
    print("1. Open YouTube in your browser.")
    print("2. Use gestures to control playback.")
    print("3. Press ESC to exit.")

    # Window Management for Windows
    window_name = "YouTube Gesture Control"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL) # Use WINDOW_NORMAL for more flexibility
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    # Force window size
    cv2.resizeWindow(window_name, 640, 480)
    
    try:
        cv2.startWindowThread()
    except:
        pass

    last_action_time = 0
    COOLDOWN = 1.0 # 1 second cooldown between keyboard triggers

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Flip the frame for natural movement
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process hand landmarks
        results = hands.process(rgb_frame)

        gesture_text = "None"
        action_text = "None"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw skeleton
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Recognition logic
                raw_gesture = recognize_gesture(hand_landmarks)
                gesture_text = smoother.smooth(raw_gesture)
                
                # Execute action
                if gesture_text != "None":
                    action_text = GESTURE_ACTIONS.get(gesture_text, "None")
                    
                    # Trigger PyAutoGUI with cooldown
                    if action_text != "None" and (time.time() - last_action_time > COOLDOWN):
                        execute_action(gesture_text)
                        last_action_time = time.time()

        # --- PREMIUM UI OVERLAY ---
        # Dark HUD background
        cv2.rectangle(frame, (0, 0), (500, 110), (30, 30, 30), -1)
        # Border
        cv2.rectangle(frame, (0, 0), (500, 110), (100, 255, 100), 2)
        
        # Texts
        cv2.putText(frame, f"GESTURE: {gesture_text}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.putText(frame, f"ACTION : {action_text}", (20, 85), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # Show Action Icon (if action is scrolling, we show text if icon missing)
        if action_text in ICON_MAPPING:
            frame = overlay_icon(frame, ICON_MAPPING[action_text], x=380, y=5, size=(100, 100))
            if "Scroll" in action_text and not os.path.exists(ICON_MAPPING[action_text]):
                 cv2.putText(frame, "↑↑" if "Up" in action_text else "↓↓", (400, 70), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

        # Show frame
        cv2.imshow(window_name, frame)

        # Quit on ESC
        if cv2.waitKey(10) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
