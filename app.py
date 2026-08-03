from flask import Flask, abort, render_template

import data

app = Flask(__name__)

visit_count = 0


@app.route("/")
def home():
    global visit_count
    visit_count += 1
    return render_template("index.html", visits=visit_count)


@app.route("/about")
def about():
    # 화면에 필요한 이력/자격증 데이터를 data.py에서 가져와 템플릿에 전달합니다.
    # app.py에 내용을 직접 적지 않으면, 라우팅 코드와 포트폴리오 데이터가 분리되어 유지보수가 쉬워집니다.
    return render_template(
        "about.html",
        career=data.career,
        certificates=data.certificates,
    )


@app.route("/skills")
def skills():
    return render_template("skills.html", skills=data.skills)


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

    return render_template("project_detail.html", slug=slug, project=project)


if __name__ == "__main__":
    app.run(debug=True)
