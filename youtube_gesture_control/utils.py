import cv2
import numpy as np
import os

class GestureSmoother:
    def __init__(self, max_len=3):
        self.history = []
        self.max_len = max_len

    def smooth(self, gesture):
        if not gesture or gesture == "Unknown":
            return "None"
            
        self.history.append(gesture)
        if len(self.history) > self.max_len:
            self.history.pop(0)

        # Return gesture that occurs most in history
        return max(set(self.history), key=self.history.count)

def overlay_icon(frame, icon_path, x=10, y=10, size=(100, 100)):
    """
    Overlays a transparent PNG icon onto the frame.
    """
    if not os.path.exists(icon_path):
        return frame

    try:
        icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)
        if icon is None:
            return frame
            
        icon = cv2.resize(icon, size)
        
        # Split channels
        if icon.shape[2] == 4:
            # Icon has alpha channel
            icon_rgb = icon[:, :, :3]
            alpha_mask = icon[:, :, 3] / 255.0
            
            # Area to overlay
            h, w = size
            if y + h > frame.shape[0] or x + w > frame.shape[1]:
                return frame
            
            roi = frame[y:y+h, x:x+w]
            
            for c in range(3):
                roi[:, :, c] = (alpha_mask * icon_rgb[:, :, c] + (1 - alpha_mask) * roi[:, :, c])
                
            frame[y:y+h, x:x+w] = roi
    except Exception as e:
        print(f"Overlay error: {e}")
        
    return frame
