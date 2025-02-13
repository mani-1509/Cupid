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
        """Analyzes the image URL using OpenAI's vision model to determine Love Aura and create a poem."""
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
                                    "You are the Love Aura AI Detector and a Poetic Genius! "
                                    "Your task is to analyze the image and perform two steps:\n\n"
                                    "Determine the Love Aura\n"
                                    "1. Identify the mood of the person in the image based on their facial expression.\n"
                                    "2. Assign them a Love Aura Personality based on the mood.\n"
                                    "3. Write a short, fun description of their Love Aura Personality.\n\n"
                                    "Poem\n"
                                    "1. Describe the person: What do they look like? What emotions are they expressing?\n"
                                    "2. Describe the environment: What is around them? What is the mood of the setting?\n"
                                    "3. Weave a story: Connect the person and their environment into a cohesive narrative.\n"
                                    "4. Use poetic language: Be creative with metaphors, similes, and imagery.\n"
                                    "5. Keep it positive and uplifting: Even if the mood seems somber, find beauty in it.\n\n"
                                    "Format:\n"
                                    "1. Start with the Love Aura Personality and description.\n"
                                    "2. Follow with the poem.\n"
                                    "3. Use Markdown for formatting.\n\n"
                                    "Now, analyze the image and create your response!"
                                )
                            },
                            {
                                "type": "image_url", 
                                "image_url": {"url": image_url}
                            }
                        ]
                    }
                ],
                max_tokens=1000,  # Increased tokens for longer responses
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Image analysis failed: {str(e)}")