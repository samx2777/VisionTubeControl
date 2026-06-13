import numpy as np

# Finger indices for Mediapipe
# Thumb: 4, Index: 8, Middle: 12, Ring: 16, Pinky: 20
TIP_IDS = [4, 8, 12, 16, 20]

def fingers_up(hand_landmarks):
    """
    Returns list of fingers that are up: [thumb, index, middle, ring, pinky]
    1 = finger up, 0 = finger down
    """
    fingers = []

    # Thumb: Use the distance between thumb tip and index MCP to determine if thumb is extended
    # This is more robust than simple X or Y comparison for different hand orientations
    thumb_tip = hand_landmarks.landmark[TIP_IDS[0]]
    index_mcp = hand_landmarks.landmark[5]
    
    # Distance in 2D space
    dist = np.hypot(thumb_tip.x - index_mcp.x, thumb_tip.y - index_mcp.y)
    
    # If the thumb tip is far enough from the index finger base, it's considered "up" (extended)
    if dist > 0.08: # Threshold adjusted for typical hand scale in frame
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers: remains the same (tip y < joint y)
    for id in range(1, 5):
        if hand_landmarks.landmark[TIP_IDS[id]].y < hand_landmarks.landmark[TIP_IDS[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

def recognize_gesture(hand_landmarks):
    fingers = fingers_up(hand_landmarks)
    
    # Landmark positions
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    thumb_mcp = hand_landmarks.landmark[2]
    
    # 1. Thumb Up: Thumb is extended and pointing UP
    if fingers == [1, 0, 0, 0, 0] and thumb_tip.y < thumb_ip.y:
        return "Thumb Up"
    
    # 2. Thumb Down: Thumb is extended and pointing DOWN
    if fingers == [1, 0, 0, 0, 0] and thumb_tip.y > thumb_ip.y:
        return "Thumb Down"
        
    # 3. Fist (All fingers closed)
    if fingers == [0, 0, 0, 0, 0]:
        return "Fist"
        
    # 4. Index + Middle (Peace sign)
    if fingers == [0, 1, 1, 0, 0]:
        return "Index + Middle"
        
    # 5. Palm Open (All fingers up)
    if fingers == [1, 1, 1, 1, 1]:
        return "Palm Open"
        
    # 6. Index Point (Only index up)
    if fingers == [0, 1, 0, 0, 0]:
        return "Index Point"

    # 7. Scroll Up (Index, Middle, Ring up)
    if fingers == [0, 1, 1, 1, 0]:
        return "Scroll Up"

    # 8. Scroll Down (Index, Middle, Ring, Pinky up)
    if fingers == [0, 1, 1, 1, 1]:
        return "Scroll Down"

    return "Unknown"
