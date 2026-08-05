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
    "AI · Computer Vision": ["Python", "PyTorch", "TensorFlow", "scikit-learn", "YOLO", "MediaPipe", "OpenCV", "ONNX"],
    "Data · Machine Learning": ["Pandas", "NumPy", "FAISS", "LangChain", "Graph Neural Network", "RAG"],
    "Backend · Database": ["FastAPI", "Spring Boot", "PostgreSQL", "MySQL", "SQLite", "Redis"],
    "Tools": ["Git", "GitHub", "Docker", "VS Code", "IntelliJ IDEA", "Google Colab", "Notion"],
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
        "period": "2024.08.12 ~ 08.22",
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
    "focusai": {
        "title": "FocusAI",
        "subtitle": "실시간 학습 집중도 분석 시스템",
        "award": "캡스톤 우수 논문상 · 기초캡스톤 은상 (2025)",
        "overview": "비대면 학습·업무 환경에서 집중도를 객관적으로 측정할 수단이 없다는 문제를 해결하기 위해 개발한 AI 기반 실시간 집중도 분석 시스템입니다. 카메라 영상에서 졸음·고개 돌림·휴대폰 사용·자리 이탈·하품 등 5가지 비집중 행동을 감지해 집중도 점수(0~100)를 실시간으로 산출하고 시각적 피드백을 제공합니다. 기존 타이머 기반 앱과 달리 AI 행동 인식을 통해 실질적 몰입 상태를 정량화하는 것이 핵심 차별점입니다.",
        "features": [
            "졸음 감지: 눈 감김 비율을 CNN이 학습하여 예측",
            "고개 돌림 감지: 눈·코 상대 위치 변화로 판단, 2초 이상 시선 이탈 시 집중 저하 처리",
            "휴대폰 사용 감지: YOLOv8로 객체 탐지 후 위치·시간 기록",
            "자리 이탈 감지: 5초 이상 얼굴 미감지 시 판단",
            "하품 감지: 입 영역 크롭 후 CNN 입력",
        ],
        "role_title": "5가지 비집중 행동 감지 기준 및 점수 산정 구조 설계",
        "role_detail": "각 행동의 특성에 맞는 탐지 기준(임계값·시간 조건)을 정의하고, 감지 이벤트가 집중도 점수에 반영되는 방식(시간 기반 차감 + 이벤트 페널티)을 설계했습니다. 세션 종료 후 레이더 차트와 시간별 그래프로 분석 리포트를 출력하는 구조까지 설계했습니다.",
        "tech": ["Python", "YOLOv8", "MediaPipe", "CNN", "Computer Vision", "실시간 행동 인식"],
    },
    "trenddo": {
        "title": "TrendDo",
        "subtitle": "보는 유행을, 함께 해보는 문화로 바꾸는 플랫폼",
        "award": "AI·SW 해커톤 Khuthon 2026 우수상",
        "overview": "숏폼과 알고리즘 속에서 빠르게 소비되고 사라지는 유행을 세대별 언어로 번역하고, 실제로 해볼 수 있는 ToDo 챌린지와 지역·전통문화 경험으로 전환하는 AI 문화 순환 플랫폼입니다. 단순히 유행을 보여주는 데 그치지 않고, 유행을 발견-이해-행동-지역 연결-재생산까지 이어지는 순환 구조로 설계했습니다.",
        "features": [
            "Trend Radar: YouTube·Naver·공공데이터 기반 유행 자동 수집",
            "Generation Guide: 10대부터 5060세대까지 연령대별 맞춤 유행 설명",
            "Trend-Do Card: 유행을 준비물·시간·비용·난이도가 포함된 ToDo 챌린지로 변환",
            "K-Culture Map: 지역 자산·전통문화와 유행을 연결해 문화 순환을 시각화",
            "관리자 콘솔: 트렌드 수집부터 AI 카드 생성, 안전성 검수, 지자체 제안까지 관리하는 AI 운영 파이프라인",
        ],
        "role_title": "서비스 기획 및 AI 문화 순환 구조 설계",
        "role_detail": "'알고리즘은 사람을 더 오래 보게 만들지만, 문화는 더 깊게 경험되게 만들지 못한다'는 문제의식에서 출발해 서비스 전체를 기획했습니다. 유행을 발견-이해-행동-지역 연결-재생산으로 이어지는 4단계 순환 구조(Trend Radar, Generation Guide, Trend-Do Card, K-Culture Map)를 설계하고, 단순히 '유행+지역'을 조합하는 것이 아니라 실제로 수행 가능한 문화 경험으로 융합하는 방향성을 정의했습니다. AI 판단 결과를 근거와 함께 설명하는 XAI 카드, 관리자 검수를 거치는 안전성 검증 흐름 등 서비스의 신뢰성을 담보하는 설계 원칙도 함께 세웠습니다.",
        "tech": ["React", "TypeScript", "Node.js", "Express", "OpenAI API", "Structured Output", "Zod", "SQLite"],
    },
    "ddak-teo": {
        "title": "딱!터",
        "subtitle": "AI 기반 창업 입지·업종 추천 및 상권 분석 플랫폼",
        "award": None,
        "overview": "국내 창업 5년 차 폐업률 66.2%라는 현실과 '데이터는 있는데 해석이 안 된다'는 예비 창업자의 어려움을 해결하기 위해 개발한 AI 창업 지원 플랫폼입니다. 서울시 상권 데이터(임대 시세·유동인구·매출·생존율)를 기반으로 맞춤형 입지·업종을 추천하고, LLM이 전문가 수준의 분석 리포트를 자동 생성하며, RAG 기반 챗봇이 실시간 컨설팅을 제공합니다.",
        "features": [
            "입지·업종 추천: 다지표 스코어링 + Gemini 1.5-flash 기반 자연어 추천 이유 생성",
            "자동 분석 리포트: 2단계 프롬프팅(요약→본문)으로 전문가 수준 리포트 생성",
            "AI 챗봇 컨설팅: 리포트 PDF를 벡터 DB로 구축한 RAG + 정형/비정형 데이터 하이브리드 처리",
        ],
        "role_title": "RAG 기반 챗봇 구현",
        "role_detail": "리포트 PDF를 벡터 DB로 색인하는 RAG 파이프라인(PyMuPDF → OpenAI Embeddings → FAISS → LLMChain)을 구축하고, 정형(CSV/JSON)·비정형(PDF) 데이터를 통합 처리하는 하이브리드 챗봇을 설계·구현했습니다. LLM 기반 질의 라우팅으로 질문 유형별 최적 처리 경로를 자동 분류하고, LangChain으로 멀티턴 대화를 지원했습니다.",
        "tech": ["Python", "RAG", "LangChain", "FAISS", "OpenAI Embeddings", "GPT-4o", "Gemini 1.5-flash", "PyMuPDF", "Pandas", "AWS RDS"],
    },
    "trusteye": {
        "title": "TrustEYE",
        "subtitle": "AI 기반 가짜 리뷰 탐지 및 클린 리뷰 플랫폼",
        "award": "우수상 수상",
        "overview": "쇼핑몰 리뷰 조작 문제를 해결하기 위해 개발한 AI 기반 가짜 리뷰 탐지 플랫폼입니다. 상품 URL을 입력하면 Playwright로 리뷰 데이터를 수집하고, AI 모델이 광고성·AI 생성 리뷰 등 가짜 패턴을 탐지해 보정 평점을 제공합니다. 신뢰도 기반 브랜드 랭킹과 브라우저 확장 프로그램 오버레이 기능도 포함합니다.",
        "features": [
            "가짜 리뷰 필터링 및 보정 평점 산출",
            "신뢰도 기반 브랜드 랭킹 (매일 자정 자동 업데이트)",
            "Chrome/Edge 확장 프로그램 실시간 오버레이",
        ],
        "role_title": "AI 분석 로직 및 필터링 알고리즘 개발",
        "role_detail": "Claude·Gemini API를 연동해 리뷰 텍스트의 의심 패턴을 탐지하는 판별 알고리즘을 개발했습니다. 광고성 리뷰는 Rule-based 필터링 후 TF-IDF+Logistic Regression으로, AI 생성 리뷰는 Copyleaks API로 탐지했습니다. API 비용과 Rate Limit을 고려해 대량 분석(Gemini Flash)과 정밀 판단(Gemini Pro)을 나누는 2단계 전략을 설계했습니다.",
        "tech": ["Python", "Claude API", "Gemini 2.5 Flash/Pro", "LangChain", "Copyleaks API", "TF-IDF", "Logistic Regression", "Pandas", "Spring Boot", "PostgreSQL", "Redis", "Playwright"],
    },
    "isbomb": {
        "title": "ISBOMB",
        "subtitle": "블록체인 기반 AI 보안 명세 플랫폼",
        "award": "장려상 수상",
        "overview": "EU AI Act·NIST Framework 등 글로벌 AI 규제 강화와 AI 보안 위협 증가를 배경으로 기획된 분산형 AI 보안 플랫폼입니다. AI 구성 요소를 Hyperledger Fabric 블록체인에 불변 저장하고, AI 기반 자동 위협 탐지와 ZKP(영지식 증명)를 결합해 무결성·투명성·프라이버시를 동시에 확보하는 AIBOM 시스템입니다.",
        "features": [
            "블록체인 모듈: Hyperledger Fabric + Merkle Tree 기반 불변 저장 및 무결성 검증",
            "AI 분석 모듈: 보안 사고 데이터 기반 위협 예측, NLP 기반 컴플라이언스 진단",
            "ZKP 모듈: 민감 정보 비공개 상태로 검증 완료만 증명",
        ],
        "role_title": "의료기기 인허가 문서 자동 생성 모델",
        "role_detail": "식약처 「생성형 인공지능 의료기기 허가·심사 가이드라인」을 기준으로, LLM이 단계별 질문을 통해 정보를 수집하고 가이드라인에 부합하는 인허가 문서 초안을 자동 생성해 PDF로 제공하는 파이프라인을 설계·구현했습니다. JSON+Markdown 구조화 출력으로 DB 연동과 문서 재사용성을 확보했습니다.",
        "tech": ["Python", "LLM API", "프롬프트 엔지니어링", "Structured Output", "PDF 변환", "Hyperledger Fabric", "ZKP"],
    },
    "bing-go": {
        "title": "BING GO",
        "subtitle": "겨울철 빙판길 실시간 안전 지도 서비스",
        "award": None,
        "overview": "2018~2022년 5년간 4,609건에 달하는 도로 결빙 사고를 배경으로 기획된 서비스입니다. 기상청 제설 데이터, 시민 제보, 도로 정보를 AI로 통합 분석해 빙판 위험 구간을 예측하고 제설 상태를 실시간으로 알려주는 모바일 앱입니다.",
        "features": [
            "위험도 4개 요인 가중합산 기반 '위험 빙판 Top10' 랭킹",
            "위치 기반 시민 빙판 제보 및 피드 공유",
            "제설 데이터 기반 RAG 챗봇 'Snow'로 빙판길 질의응답",
        ],
        "role_title": "RAG 서버 구축 및 AI 챗봇 구현",
        "role_detail": "제설·결빙 관련 공공데이터와 기상 정보를 벡터 DB에 색인하는 RAG 파이프라인을 구축하고, LLM과 연결해 맥락 있는 안전 정보를 제공하는 챗봇을 완성했습니다. 플렉스튜디오(로우코드) 환경 제약 안에서 외부 RAG 서버와의 API 통신 구조를 설계해 챗봇 UI와 백엔드 간 데이터 흐름을 연결했습니다.",
        "tech": ["FlexStudio", "RAG Server", "LLM API", "기상청 공공데이터", "위치 기반 서비스"],
    },
    "fridge": {
        "title": "#FRIDGE",
        "subtitle": "YOLO 기반 냉장고 재고 관리 및 AI 장보기 앱",
        "award": "2025 캡스톤 디자인 및 AI 해커톤 우수상",
        "overview": "가정 내 식재료 낭비(연간 폐기 비용 약 9,500억 원) 문제를 해결하기 위한 AI 기반 스마트 냉장고 관리 앱입니다. 냉장고 문이 닫힐 때 내부 카메라가 자동 촬영하고, YOLO+OCR로 식재료를 인식·분류해 재고를 자동 관리합니다. LLM 기반 레시피 추천과 LSTM 기반 자동 장보기까지 이어지는 엔드투엔드 파이프라인입니다.",
        "features": [
            "AI 재고 인식: YOLO+OCR로 식재료 탐지, 브랜드명·유통기한 추출",
            "AI 레시피 추천: GPT-4o mini + RAG로 유통기한 임박 재료 우선 활용",
            "자동 장보기: LSTM 기반 소비 패턴 예측 및 커머스 API 연동 최저가 구매",
        ],
        "role_title": "YOLO 비전 모델 및 YOLO-OCR 통합 파이프라인 구현",
        "role_detail": "냉장고 내부 이미지에서 식재료를 실시간 탐지·분류하는 YOLO 기반 객체 탐지 알고리즘을 개발했습니다. 탐지된 객체 영역을 크롭해 OCR로 전달하는 파이프라인을 설계하고, 재고 추가/꺼냄 등 상태 변화 감지 로직을 구현했습니다.",
        "tech": ["Python", "YOLO", "OCR", "Computer Vision", "GPT-4o mini", "RAG", "LSTM"],
    },
}
