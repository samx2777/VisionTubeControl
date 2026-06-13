# 🎥 YouTube Hand Gesture Controller (V2)

An AI-powered gesture control system that enables users to control YouTube videos using hand gestures in real time. Built with Computer Vision, MediaPipe, OpenCV, and PyAutoGUI for a seamless hands-free experience.

---

## 🚀 Demo Preview

<img width="1536" height="1024" alt="ChatGPT Image Jun 13, 2026, 01_07_04 PM" src="https://github.com/user-attachments/assets/20e56cdc-aa22-4ac3-8019-ed825b99f285" />


### 🎬 Full Video Demonstration

[▶ Watch Demo Video](./demo/demo.mp4)

---

## ✨ Features

### 🎮 Gesture Controls

| Gesture | Action |
|----------|----------|
| 👍 Thumb Up | Volume Up |
| 👎 Thumb Down | Volume Down |
| ✌️ Index + Middle Finger | Play / Pause |
| 🖐️ Three Fingers | Scroll Up |
| ✋ Four Fingers | Scroll Down |
| 🖐️ Open Palm | Fullscreen |
| ☝️ Index Finger Point | Mute / Unmute |

---

## 🧠 Key Highlights

- Real-time Hand Tracking
- AI-powered Gesture Recognition
- Dynamic HUD Interface
- Action Feedback Icons
- Gesture Smoothing for Stability
- Hands-Free YouTube Navigation
- Lightweight & Efficient

---

## 📸 Project Showcase

The system tracks hand landmarks using MediaPipe and translates gestures into YouTube actions.

Supported Actions:

✅ Play / Pause

✅ Volume Up

✅ Volume Down

✅ Mute / Unmute

✅ Fullscreen

✅ Scroll Up

✅ Scroll Down

---

## 📁 Project Structure

```text
YouTube-Hand-Gesture-Controller/
│
├── main.py
├── gestures.py
├── youtube_control.py
├── utils.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── thumbnail.png
│
└── demo/
    └── demo.mp4
```

### File Descriptions

- **main.py** → Main application loop
- **gestures.py** → Hand landmark and gesture detection
- **youtube_control.py** → YouTube control actions using PyAutoGUI
- **utils.py** → Helper functions and gesture smoothing
- **assets/** → UI assets and project visuals
- **demo/** → Project demonstration videos

---

## 🛠️ Installation

Clone Repository:

```bash
git clone https://github.com/YOUR_USERNAME/YouTube-Hand-Gesture-Controller.git
cd YouTube-Hand-Gesture-Controller
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

Run Application:

```bash
python main.py
```

---

## 🎮 Usage

1. Open YouTube in your browser.
2. Launch the application.
3. Position your hand clearly in front of the webcam.
4. Perform supported gestures.
5. The HUD displays detected gestures and actions.
6. Press **ESC** to exit.

---

## 🧰 Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

---

## 🔮 Future Improvements

- Custom Gesture Mapping
- Browser Extension Integration
- Multi-Hand Support
- Gesture Calibration Mode
- Netflix & VLC Support
- Voice + Gesture Controls

---

## 🤝 Contributing

Contributions are welcome.

1. Fork Repository
2. Create Feature Branch
3. Commit Changes
4. Open Pull Request

---

## ⭐ Support

If you found this project useful, please consider starring the repository.

Made with ❤️ using Computer Vision and AI.
