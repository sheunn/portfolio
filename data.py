# 포트폴리오에 표시할 내용을 한 곳에 모아둔 데이터 파일입니다.
# Flask 라우트(app.py)는 이 데이터를 import해서 템플릿으로 전달하고,
# 템플릿은 전달받은 데이터를 Jinja2 문법으로 반복/조건 렌더링합니다.

# profile은 홈/About처럼 여러 페이지에서 반복해서 쓰는 기본 소개 정보입니다.
# 이름, 연락처, 학력 같은 내용을 data.py에 두면 템플릿 문구를 직접 찾아 고치지 않아도 됩니다.
profile = {
    "name": "김시은",
    "tagline": "AI Engineer",
    "about_short": "AI와 데이터를 활용해 현실의 문제를 해결하는 서비스를 개발합니다.",
    "education": "경기대학교 인공지능전공",
    "email": "sieun4507@gmail.com",
    "github": "github.com/sheunn/sheunn.github.io",
    "linkedin": "LinkedIn URL 입력 예정"
}

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
    "ADsP",
    "SQLD",
    "CSTS",
    "TOPCIT Lv.3",
    "빅데이터분석기사"
]

skills = {
    "AI / ML": ["Python", "PyTorch", "scikit-learn", "CNN", "TF-IDF", "Logistic Regression"],
    "Computer Vision": ["YOLO", "YOLOv8", "OpenCV", "MediaPipe", "OCR"],
    "LLM / RAG": ["LangChain", "FAISS", "RAG", "GPT-4o", "GPT-4o mini", "Gemini API", "Claude API"],
    "Backend / Data": ["Flask", "Jinja2", "AWS RDS", "Gunicorn", "Nginx", "systemd"],
}

# experiences는 projects처럼 slug를 key로 쓰는 상세 페이지용 데이터입니다.
# career는 기존 연도별 요약 타임라인으로 남겨두고, 실제 활동 상세는 이 딕셔너리에서 관리합니다.
experiences = {
    "swat": {
        "title": "SWAT 봉사단",
        "period": "2023",
        "category": "봉사활동",
        "summary": "보육원, 초중고등학교 대상 AI-SW(IT-kit) 실습 교육을 진행하며 청소년 대상 AI 교육 콘텐츠 기획 및 전달 경험을 쌓았습니다.",
        "highlights": [
            "보육원·초중고 학생 대상 AI-SW 실습 키트 운영",
            "눈높이에 맞춘 AI 개념 설명 및 실습 진행",
        ],
    },
    "digital-saessak": {
        "title": "디지털 새싹 강사활동",
        "period": "2024",
        "category": "교육/강사",
        "summary": "수원 내 고등학교를 대상으로 IoT 관련 교육을 직접 기획하고 진행했습니다.",
        "highlights": [
            "고등학생 대상 IoT 개념 및 실습 커리큘럼 구성",
            "현장 강의 진행 및 실습 지도",
        ],
    },
    "singapore-secure-coding": {
        "title": "싱가포르 시큐어코딩 연수",
        "period": "2025.08.12 ~ 08.22",
        "category": "해외연수",
        "summary": "경기대학교 SW중심대학사업단 주관 싱가포르 시큐어코딩 개발 프로젝트에 선발되어 참가했습니다. 글로벌 사이버보안 선진국인 싱가포르에서 보안 취약점 분석·방어 코딩 실습을 진행하고, 현지 사이버보안 기관을 방문해 AI 기반 보안 실무 역량을 강화했습니다.",
        "highlights": [
            "보안 취약점 분석 및 방어 코딩 실습",
            "AWS, Google 오피스 방문",
            "웁살라 보안회사 방문 — 블록체인/보안 실무 학습",
        ],
    },
    "vice-president": {
        "title": "AI컴퓨터공학부 부학생회장",
        "period": "2025",
        "category": "학생 활동",
        "summary": "AI컴퓨터공학부 부학생회장을 역임하며 학과 내 행사를 기획·진행하고, 교수진과 학우 간 소통을 촉진하는 역할을 맡았습니다.",
        "highlights": [
            "학과 행사 기획 및 운영",
            "교수-학생 간 소통 채널 활성화",
        ],
    },
    "k-primus": {
        "title": "K-PRIMUS 서포터즈 활동",
        "period": "2025",
        "category": "학생 활동",
        "summary": "자유전공학부 신입생의 대학생활 적응을 지원하는 재학생 서포터즈로 활동했습니다. 다양한 전공의 선배들과의 만남을 기획하고, 신입생 대학생활 적응에 필요한 정보를 정리해 발표했습니다.",
        "highlights": [
            "전공별 선배 매칭 프로그램 기획",
            "신입생 대상 대학생활 정보 정리 및 발표",
        ],
    },
    "ceo-forum": {
        "title": "CEO 포럼 장학생 선발",
        "period": "2025",
        "category": "장학/선발",
        "summary": "경기대학교 CEO 포럼 장학생으로 선정되었습니다.",
        "highlights": [],
    },
    "ces-2026": {
        "title": "미국 실리콘밸리 CES 연수",
        "period": "2026.01.04 ~ 01.13",
        "category": "해외연수",
        "summary": "경기대학교 SW중심대학사업단 주관 SW상상기업 프로그램의 우수 참여자로 선발되어 미국 실리콘밸리 연수에 참가했습니다. CES 2026을 참관하며 글로벌 AI·SW 기술 트렌드를 직접 탐색하고, Google·NVIDIA·Tesla 등 빅테크 기업을 탐방했습니다.",
        "highlights": [
            "CES 2026 참관 — 글로벌 AI·SW 트렌드 탐색",
            "Google, NVIDIA, Tesla 등 빅테크 기업 탐방",
            "UC 버클리·스탠퍼드 특강 참여",
        ],
    },
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
