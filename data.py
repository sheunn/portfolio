# 포트폴리오에 표시할 내용을 한 곳에 모아둔 데이터 파일입니다.
# Flask 라우트(app.py)는 이 데이터를 import해서 템플릿으로 전달하고,
# 템플릿은 전달받은 데이터를 Jinja2 문법으로 반복/조건 렌더링합니다.

career = {
    "2025": [
        {
            "type": "Project",
            "title": "#FRIDGE",
            "award": "2025 캡스톤 디자인 및 AI 해커톤 우수상",
            "summary": "냉장고 내부 카메라 기반 식재료 인식, OCR, 레시피 추천을 연결한 AI 재고 관리 서비스를 구현했습니다.",
            "tech": ["Python", "YOLO", "OCR", "GPT-4o mini", "RAG"],
        },
        {
            "type": "Award",
            "title": "AI 기반 가짜 리뷰 탐지 및 클린 리뷰 플랫폼",
            "award": "캡스톤 우수상",
            "summary": "Rule-based 필터링과 머신러닝, LLM API를 결합해 리뷰 신뢰도 분석 구조를 설계했습니다.",
            "tech": ["Python", "Gemini API", "Claude API", "TF-IDF"],
        },
    ],
    "2024": [
        {
            "type": "Project",
            "title": "딱!터",
            "summary": "서울시 상권 데이터와 PDF 기반 상권 리포트 RAG를 결합한 창업 입지 추천 플랫폼을 개발했습니다.",
            "tech": ["Python", "RAG", "LangChain", "FAISS", "AWS RDS"],
        },
        {
            "type": "Award",
            "title": "FocusAI",
            "award": "캡스톤 우수 논문상 · 기초캡스톤 은상",
            "summary": "영상 기반 비집중 행동 탐지와 집중도 점수화 알고리즘을 설계했습니다.",
            "tech": ["Python", "YOLOv8", "MediaPipe", "CNN", "OpenCV"],
        },
    ],
    "2023": [
        {
            "type": "Education",
            "title": "경기대학교 인공지능전공",
            "summary": "머신러닝, 딥러닝, 컴퓨터비전, 자연어처리 중심으로 AI 서비스 구현 역량을 쌓았습니다.",
            "tech": ["Python", "PyTorch", "scikit-learn", "Flask"],
        },
    ],
}

certificates = [
    "정보처리기사 준비",
    "SQLD 준비",
]

skills = {
    "AI / ML": ["Python", "PyTorch", "scikit-learn", "CNN", "TF-IDF", "Logistic Regression"],
    "Computer Vision": ["YOLO", "YOLOv8", "OpenCV", "MediaPipe", "OCR"],
    "LLM / RAG": ["LangChain", "FAISS", "RAG", "GPT-4o", "GPT-4o mini", "Gemini API", "Claude API"],
    "Backend / Data": ["Flask", "Jinja2", "AWS RDS", "Gunicorn", "Nginx", "systemd"],
}

projects = {
    "ddak-teo": {
        "title": "딱!터",
        "subtitle": "AI 기반 창업 입지·업종 추천 및 상권 분석 플랫폼",
        "award": None,
        "overview": "서울시 상권 데이터를 활용한 입지 추천에 PDF 기반 상권 리포트를 RAG로 검색·응답하는 기능을 결합한 서비스입니다. LLM 기반 질의 라우팅을 설계해 수치 조회, 추천, 전략, RAG 응답을 상황에 맞게 분기하도록 구현했습니다.",
        "features": [
            "상권 데이터 기반 입지 및 업종 추천",
            "PDF 상권 리포트 검색을 위한 RAG 파이프라인",
            "질문 의도에 따라 분석 방식이 달라지는 LLM 라우팅 구조",
        ],
        "role_title": "RAG 기반 AI 챗봇 설계 및 구현",
        "role_detail": "LangChain, FAISS, GPT-4o를 활용해 상권 리포트 검색과 자연어 응답 흐름을 설계했습니다.",
        "tech": ["Python", "RAG", "LangChain", "FAISS", "GPT-4o", "AWS RDS"],
    },
    "focusai": {
        "title": "FocusAI",
        "subtitle": "실시간 학습 집중도 분석 시스템",
        "award": "캡스톤 우수 논문상 · 기초캡스톤 은상",
        "overview": "카메라 영상에서 학습자의 비집중 행동을 실시간으로 탐지해 집중도 점수를 제공하는 시스템입니다. 졸음, 고개 돌림, 휴대폰 사용, 자리 이탈, 하품을 감지 이벤트로 정의했습니다.",
        "features": [
            "YOLOv8 기반 휴대폰 객체 탐지",
            "MediaPipe와 CNN 기반 얼굴·행동 분석",
            "비집중 행동 이벤트를 집중도 점수로 환산하는 알고리즘",
        ],
        "role_title": "5가지 비집중 행동 감지 기준 및 점수 산정 구조 설계",
        "role_detail": "탐지 이벤트의 기준을 정의하고, 행동별 위험도를 반영해 집중도 점수로 변환하는 로직을 설계했습니다.",
        "tech": ["Python", "YOLOv8", "MediaPipe", "CNN", "OpenCV"],
    },
    "fake-review-detector": {
        "title": "AI 기반 가짜 리뷰 탐지 및 클린 리뷰 플랫폼",
        "subtitle": "신뢰 가능한 리뷰 선별과 보정 평점 제공 서비스",
        "award": "캡스톤 우수상",
        "overview": "쇼핑몰 리뷰의 광고성·AI 생성 패턴을 탐지해 신뢰할 수 있는 리뷰만 반영한 보정 평점을 제공하는 플랫폼입니다. 비용과 Rate Limit을 고려해 1차 필터링 후 2차 정밀 분석하는 전략을 설계했습니다.",
        "features": [
            "Rule-based 필터링과 ML 기반 1차 탐지",
            "Claude·Gemini API를 활용한 2차 정밀 분석",
            "보정 평점과 클린 리뷰 제공",
        ],
        "role_title": "AI 분석 로직 및 필터링 알고리즘 개발",
        "role_detail": "TF-IDF, Logistic Regression, LLM API를 조합해 비용 효율적인 리뷰 분석 파이프라인을 구성했습니다.",
        "tech": ["Python", "Gemini API", "Claude API", "LangChain", "TF-IDF", "Logistic Regression"],
    },
    "fridge": {
        "title": "#FRIDGE",
        "subtitle": "AI 기반 냉장고 식재료 인식 및 레시피 추천 서비스",
        "award": "2025 캡스톤 디자인 및 AI 해커톤 우수상",
        "overview": "냉장고 내부 카메라로 식재료를 자동 인식하고 레시피 추천, 장보기까지 연결하는 AI 기반 재고 관리 서비스입니다. 객체 탐지와 OCR을 연결해 제품명과 유통기한을 추출했습니다.",
        "features": [
            "YOLO 기반 식재료 객체 탐지",
            "탐지 영역 Crop 후 OCR 정보 추출",
            "보유 식재료 기반 레시피 추천 흐름",
        ],
        "role_title": "YOLO 비전 모델 및 YOLO-OCR 통합 파이프라인 구현",
        "role_detail": "YOLO 탐지 결과를 OCR 입력으로 연결하는 전처리 흐름을 만들고, 인식 결과를 서비스 데이터로 활용할 수 있게 정리했습니다.",
        "tech": ["Python", "YOLO", "OCR", "GPT-4o mini", "RAG"],
    },
}
