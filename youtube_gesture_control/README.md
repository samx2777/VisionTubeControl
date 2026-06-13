# YouTube Hand Gesture Controller (V2)

Control yofur YouTube experience using intuitive hand gestures with real-time HUD and icon overlays.

## 🚀 Features
- **Intuitive Gestures**:
  - 👍 **Thumb Up** → Volume Up
  - 👎 **Thumb Down** → Volume Down
  - ✌️ **Index + Middle** → Play/Pause
  - 🖐️ **Three Fingers** (Index + Middle + Ring) → Scroll Up
  - ✋ **Four Fingers** (Index + Middle + Ring + Pinky) → Scroll Down
  - 🖐️ **Palm Open** → Fullscreen
  - ☝️ **Index Point** → Mute
- **Advanced HUD**: Real-time gesture detection display with dynamic icon overlays.
- **Smoothing & Stability**: Integrated `GestureSmoother` to prevent jittery actions.

## 📁 Project Structure
- `main.py`: The central hub controlling webcam, hand tracking, and UI.
- `gestures.py`: Contains finger-tracking logic and gesture recognition.
- `youtube_control.py`: Executes PyAutoGUI commands for YouTube.
- `utils.py`: Helper utilities for icon overlay and signal smoothing.
- `assets/`: UI Icons for the visual feedback HUD.

## 🛠️ Setup
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Open YouTube**: Open the video you want to control in your browser.
3. **Execution**:
   ```bash
   python main.py
   ```

## 🎮 Usage
- Show your hand clearly to the webcam.
- A dark HUD will appear at the top showing the detected gesture.
- When an action is executed, the corresponding icon will appear in the HUD.
- **ESC** to exit the application.