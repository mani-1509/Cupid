# Cupid 💖

Welcome to the **Cupid** project! This collection of apps is designed to bring fun, romance, and creativity to your life. Whether you're exploring your love aura, playing mini-games to unlock confession messages, or discovering your love language, these apps have something for everyone!

## Apps Overview 🎉

### 1️⃣ AI Love Detector (Face or Voice Analysis) ❤️🎤
- **Description**: Upload a voice note or an image, and AI analyzes it to predict your **love aura**.
- **Example Outputs**: "Hopeless Romantic," "Secret Admirer," "Flirt Master," etc.
- **Features**:
  - Fun Valentine’s message + GIF based on your result.
  - Voice and image analysis powered by AI.

### 2️⃣ Love Confession Arcade 🎮💕
- **Description**: A mini web game where users play fun challenges to unlock cute confession messages.
- **Example Games**:
  - **Break the Ice**: Smash virtual ice blocks to reveal sweet messages.
  - **Catch the Hearts**: Collect hearts while dodging obstacles to unlock confessions.
- **Features**:
  - Interactive and engaging gameplay.
  - Unlockable romantic messages.

### 3️⃣ AI Love Language Matcher 🧩💌
- **Description**: Take a fun quiz to determine your **love language**.
- **Example Outputs**: "Words of Affirmation," "Acts of Service," "Quality Time," etc.
- **Features**:
  - Customized date ideas and gift suggestions based on your result.
  - Interactive quiz with instant results.

## Technologies Used 🛠️

- **OpenAI API**: For AI-powered analysis and responses.
- **Cloudinary**: For image and voice uploads.
- **Flask**: Backend framework for handling requests.
- **HTML/CSS/JavaScript**: Frontend for user interaction.
- **Phaser.js**: For building the Love Confession Arcade games.
- **Marked.js**: For rendering Markdown content.

## Setup Instructions 🚀

### Prerequisites

- Python 3.8+
- OpenAI API Key
- Cloudinary Account (for image/voice uploads)
- Flask

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/love-themed-apps.git
   cd love-themed-apps
2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Set up environment variables:**
   Create a .env file in the root directory and add the following:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_api_secret
5. **Run the Flask app:**
   ```bash
   python app.py or flask run
6. **Access the apps:**
   Open your browser and go to http://127.0.0.1:5000.

### Usage 🎮

AI Love Detector ❤️🎤
- Upload an image or voice note.
- Get your Love Aura Personality and a fun Valentine’s message + GIF.

Love Confession Arcade 🎮💕
- Play mini-games like Break the Ice or Catch the Hearts.
- Unlock cute confession messages as you progress.

AI Love Language Matcher 🧩💌
- Take the Love Language Quiz.
- Discover your love language and get customized date ideas or gift suggestions.

### Contributing 🤝

Contributions are welcome! If you'd like to contribute, please follow these steps:
- Fork the repository.
- Create a new branch (git checkout -b feature/YourFeatureName).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/YourFeatureName).
- Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Made with ❤️ by Mani1509.
