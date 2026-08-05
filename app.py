import os

from flask import Flask, abort, render_template, url_for

import data

app = Flask(__name__)

visit_count = 0

# 일부 Experience 이미지 폴더명은 URL slug와 철자가 다릅니다.
# 상세 페이지는 URL 안정성을 위해 slug를 유지하고, 실제 파일 탐색만 이 매핑을 거칩니다.
EXPERIENCE_IMAGE_FOLDERS = {
    "digital-saessak": ["digital-seasak"],
    # 기존 배포 폴더명(presidnet)과 정정된 폴더명(president)을 둘 다 허용합니다.
    # 이미지 파일만 바꿔도 URL slug(/experience/vice-president)는 안정적으로 유지됩니다.
    "vice-president": ["president", "presidnet"],
    "ces-2026": ["ces"],
}


def find_experience_image_folder(slug):
    """Experience slug와 실제 이미지 폴더명이 다를 수 있어 후보 폴더를 순서대로 찾습니다."""
    folder_candidates = EXPERIENCE_IMAGE_FOLDERS.get(slug, [slug])
    folder_candidates = [*folder_candidates, slug]

    for folder in dict.fromkeys(folder_candidates):
        image_dir = os.path.join(app.static_folder, "images", "experience", folder)
        if os.path.isdir(image_dir):
            return folder, image_dir

    return slug, None


def list_static_images(folder_parts):
    """정적 이미지 폴더를 스캔해 Jinja 템플릿에서 쓸 URL 리스트로 변환합니다."""
    image_dir = os.path.join(app.static_folder, *folder_parts)

    if not os.path.isdir(image_dir):
        return []

    allowed_extensions = {".jpg", ".jpeg", ".png"}
    image_files = [
        filename
        for filename in os.listdir(image_dir)
        if os.path.splitext(filename.lower())[1] in allowed_extensions
    ]

    return [
        url_for("static", filename="/".join([*folder_parts, filename]))
        for filename in sorted(image_files)
    ]


@app.route("/")
def home():
    global visit_count
    visit_count += 1
    featured_skills = [
        "Python",
        "Flask",
        "RAG",
        "LangChain",
        "YOLO",
        "OpenCV",
    ]
    return render_template(
        "index.html",
        visits=visit_count,
        profile=data.profile,
        certificates=data.certificates,
        featured_skills=featured_skills,
    )


@app.route("/about")
def about():
    # 화면에 필요한 기본 소개/자격증 데이터를 data.py에서 가져와 템플릿에 전달합니다.
    # app.py에 내용을 직접 적지 않으면, 라우팅 코드와 포트폴리오 데이터가 분리되어 유지보수가 쉬워집니다.
    return render_template(
        "about.html",
        profile=data.profile,
        certificates=data.certificates,
    )


@app.route("/skills")
def skills():
    return render_template("skills.html", skills=data.skills)


@app.route("/experience")
def experience_list():
    # period의 앞 4자리를 연도로 보고 그룹핑합니다.
    # 템플릿은 화면 표현만 담당하고, 정렬/그룹핑 같은 데이터 준비는 라우트에서 처리합니다.
    grouped_experiences = {}
    for slug, experience in data.experiences.items():
        year = experience["period"][:4]
        grouped_experiences.setdefault(year, []).append((slug, experience))

    sorted_experiences = sorted(
        grouped_experiences.items(),
        key=lambda item: item[0],
        reverse=True,
    )

    return render_template("experience.html", grouped_experiences=sorted_experiences)


@app.route("/experience/<slug>")
def experience_detail(slug):
    experience = data.experiences.get(slug)

    if experience is None:
        abort(404)

    image_folder, image_dir = find_experience_image_folder(slug)
    image_urls = []

    if image_dir is not None:
        image_urls = list_static_images(["images", "experience", image_folder])

    return render_template(
        "experience_detail.html",
        experience=experience,
        image_urls=image_urls,
    )


@app.route("/projects")
def project_list():
    # projects는 slug를 key로 쓰는 딕셔너리입니다.
    # slug는 URL에 들어가는 짧고 안정적인 식별자로, 상세 페이지 링크를 만들 때 사용합니다.
    return render_template("projects.html", projects=data.projects)


@app.route("/projects/<slug>")
def project_detail(slug):
    # <slug>는 URL의 일부를 함수 인자로 받아오는 Flask의 동적 라우팅 문법입니다.
    # 예: /projects/focusai 로 접속하면 slug 값은 "focusai"가 됩니다.
    project = data.projects.get(slug)

    if project is None:
        # 존재하지 않는 slug로 들어온 경우 빈 화면 대신 HTTP 404를 반환합니다.
        # 배포 환경에서도 잘못된 주소임을 명확하게 알릴 수 있습니다.
        abort(404)

    image_urls = list_static_images(["images", "projects", slug])

    return render_template(
        "project_detail.html",
        slug=slug,
        project=project,
        image_urls=image_urls,
    )


if __name__ == "__main__":
    app.run(debug=True)
