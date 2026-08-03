from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "딱!터",
        "award": None,
        "description": "AI 기반 창업 입지·업종 추천 및 상권 분석 플랫폼입니다. 서울시 상권 데이터를 활용한 입지 추천에, PDF 기반 상권 리포트를 RAG로 검색·응답하는 기능을 결합했습니다. LLM 기반 질의 라우팅을 설계해 수치 조회, 추천, 전략, RAG 응답을 상황에 맞게 분기하도록 구현했습니다.",
        "role": "RAG 기반 AI 챗봇 설계 및 구현",
        "tech": ["Python", "RAG", "LangChain", "FAISS", "GPT-4o", "AWS RDS"]
    },
    {
        "title": "FocusAI",
        "award": "캡스톤 우수 논문상 · 기초캡스톤 은상",
        "description": "카메라 영상에서 학습자의 비집중 행동(졸음, 고개 돌림, 휴대폰 사용, 자리 이탈, 하품)을 실시간으로 탐지해 집중도 점수를 제공하는 시스템입니다. YOLOv8로 휴대폰 객체를 탐지하고, MediaPipe와 CNN으로 얼굴·행동을 분석해 감지 이벤트를 점수로 환산하는 알고리즘을 설계했습니다.",
        "role": "5가지 비집중 행동 감지 기준 및 점수 산정 구조 설계",
        "tech": ["Python", "YOLOv8", "MediaPipe", "CNN", "OpenCV"]
    },
    {
        "title": "AI 기반 가짜 리뷰 탐지 및 클린 리뷰 플랫폼",
        "award": "캡스톤 우수상",
        "description": "쇼핑몰 리뷰의 광고성·AI 생성 패턴을 탐지해 신뢰할 수 있는 리뷰만 반영한 보정 평점을 제공하는 플랫폼입니다. Rule-based 필터링과 머신러닝(Logistic Regression, TF-IDF)을 결합하고, Claude·Gemini API로 정밀 분석을 수행했습니다. API 비용과 Rate Limit을 고려해 1차 필터링 후 2차 정밀 분석하는 2단계 전략을 설계했습니다.",
        "role": "AI 분석 로직 및 필터링 알고리즘 개발",
        "tech": ["Python", "Gemini API", "Claude API", "LangChain", "TF-IDF", "Logistic Regression"]
    },
    {
        "title": "#FRIDGE",
        "award": "2025 캡스톤 디자인 및 AI 해커톤 우수상",
        "description": "냉장고 내부 카메라로 식재료를 자동 인식하고 레시피 추천, 장보기까지 연결하는 AI 기반 재고 관리 서비스입니다. YOLO로 식재료 객체를 탐지한 뒤 해당 영역을 Crop하여 OCR로 제품명·유통기한을 추출하는 파이프라인을 구현했습니다.",
        "role": "YOLO 비전 모델 및 YOLO-OCR 통합 파이프라인 구현",
        "tech": ["Python", "YOLO", "OCR", "GPT-4o mini", "RAG"]
    },
]

visit_count = 0

@app.route("/")
def home():
    global visit_count
    visit_count += 1
    return render_template("index.html", visits=visit_count)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def project_list():
    return render_template("projects.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)