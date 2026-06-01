# advanced_ai.py
import os
from google import genai
from google.genai import types

# Khởi tạo client với API key
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyB3my4v6G9nMB8PB4Vx0zRQzmTeoJ3fnJ0")  # thay YOUR_API_KEY_HERE bằng key thật
client = genai.Client(api_key=API_KEY)

def call_gemini(prompt, temperature=0.7):
    """Gọi Gemini API và trả về văn bản"""
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",  # hoặc "gemini-1.5-flash" nếu thích
        contents=prompt,
        config=types.GenerateContentConfig(temperature=temperature)
    )
    return response.text

def smart_answer(question, context):
    """Trả lời câu hỏi dựa trên context, dùng Gemini"""
    prompt = f"""Bạn là trợ lý ảo thông minh của Trường Đại học Tôn Đức Thắng (TDTU). Hãy trả lời câu hỏi dưới đây một cách tự nhiên, thân thiện, dựa trên thông tin được cung cấp.

Yêu cầu:
- Chỉ sử dụng thông tin trong tài liệu.
- Nếu không có thông tin, hãy nói "Theo tài liệu hiện có, tôi chưa tìm thấy câu trả lời cho câu hỏi này."
- Câu trả lời nên rõ ràng, có cấu trúc, và có thể đưa ra ví dụ minh họa nếu có.
- Giọng điệu thân thiện, gần gũi như một người bạn đồng hành.

Tài liệu tham khảo:
{context}

Câu hỏi: {question}
"""
    return call_gemini(prompt, temperature=0.7)