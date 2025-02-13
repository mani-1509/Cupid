from openai import OpenAI
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
class VisionAPI:
    def __init__(self):
        # Configure Cloudinary
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET"),
        )
        
        # Configure OpenAI client
        self.client = OpenAI(
            base_url="https://api.studio.nebius.ai/v1/",
            api_key=os.getenv("NEBIUS_API_KEY"),
        )

    def upload_to_cloudinary(self, file):
        """Uploads an image file to Cloudinary and returns its URL."""
        try:
            upload_result = cloudinary.uploader.upload(file)
            return upload_result.get("url")
        except Exception as e:
            raise Exception(f"Image upload failed: {str(e)}")

    def analyze_image(self, image_url):
        """Analyzes the image URL using OpenAI's vision model."""
        try:
            response = self.client.chat.completions.create(
                model="Qwen/Qwen2-VL-72B-Instruct",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text", 
                                "text": (
                                    "Give text in english to describe the image\n\n"
                                    "Format your responses in Markdown.\n\n"
                                    "💖 You are the Love Aura AI Detector! 💖\n\n"
                                    "Your task is to analyze a person's facial expression and determine their **Love Aura Personality** "
                                    "based on their current mood. You will generate a playful, engaging, and Valentine’s-themed response "
                                    "based on the detected expression.\n\n"
                                    "### Mood-based Love Aura Interpretations:\n"
                                    "😊 **Happy** → **\"Hopeless Romantic 💘\"** – Love follows you like WiFi! You're always radiating affection.\n"
                                    "😲 **Surprised** → **\"Flirty Master 😉\"** – Your charm is a superpower! Sparks fly when you're around.\n"
                                    "😐 **Neutral** → **\"Mysterious Lover 🔮\"** – You’re the plot twist in every love story, keeping everyone intrigued.\n"
                                    "😠 **Angry** → **\"Chaotic Crush 🚀\"** – Love is a wild ride, and you're in the driver's seat! Fasten your seatbelt!\n"
                                    "😢 **Sad** → **\"Softhearted Dreamer 💜\"** – Love songs hit you differently. You wear your heart on your sleeve.\n"
                                    "😨 **Fearful** → **\"Shy Sweetheart 🌸\"** – Love makes your heart race! You believe in gentle connections.\n"
                                    "😖 **Disgusted** → **\"Cool & Chill 🕶️\"** – You vibe first, love later! Your love game is effortless.\n\n"
                                    "🔮 **Your response should:**\n"
                                    "1. **Identify the mood** from the facial expression.\n"
                                    "2. **Give them their Love Aura Personality** (title + emoji).\n"
                                    "3. **Provide a short, fun, and relatable Valentine’s-themed description** of their love energy.\n"
                                    "4. **Make it engaging and positive**, no matter the mood.\n\n"
                                    "💘 Let the magic begin! Analyze the image and unveil their **Love Aura**!"
                                )
                            },
                            {
                                "type": "image_url", 
                                "image_url": {"url": image_url}
                            }
                        ]
                    }
                ],
                max_tokens=800,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Image analysis failed: {str(e)}")
