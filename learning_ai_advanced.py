# learning_ai_advanced.py
import json
from advanced_ai import call_gemini  # dùng chung call_gemini

def process_learning(content, title):
    prompt = f"""Bạn là một chuyên gia giáo dục. Hãy phân tích bài viết sau và trả lời bằng định dạng JSON (chỉ JSON, không giải thích thêm, không dùng markdown):

{{
    "summary": "Tóm tắt ngắn gọn nội dung bài viết (khoảng 3-4 câu).",
    "explain": "Giải thích các khái niệm phức tạp trong bài viết một cách dễ hiểu.",
    "suggestions": "Gợi ý các chủ đề nên học tiếp theo dựa trên nội dung bài viết.",
    "questions": [
        "Câu hỏi 1 (dạng hiểu)",
        "Câu hỏi 2 (dạng phân tích)",
        "Câu hỏi 3 (dạng ứng dụng)"
    ]
}}

Tiêu đề: {title}
Nội dung: {content}
"""
    response = call_gemini(prompt, temperature=0.5)
    response = response.strip('`').replace('json\n', '').strip()
    try:
        return json.loads(response)
    except:
        return {
            "summary": "Không thể tóm tắt do lỗi xử lý.",
            "explain": "Vui lòng thử lại sau.",
            "suggestions": "Hãy kiểm tra lại nội dung bài viết.",
            "questions": ["Câu hỏi 1?", "Câu hỏi 2?", "Câu hỏi 3?"]
        }