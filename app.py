
from __future__ import annotations

from datetime import datetime, timezone

from flask import Flask, render_template, request, redirect, url_for


def parse_tags(raw: str) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for tag in raw.split(","):
        tag = tag.strip().lower()
        if tag and tag not in seen:
            seen.add(tag)
            result.append(tag)
    return result


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "sandbox-not-a-real-secret"

    # In-memory store for the sandbox. Resets on every restart, which is
    # fine for practice. Real apps use a database.
    app.notes: list[dict] = []  # type: ignore[attr-defined]

    @app.route("/")
    def home():
        # Older in-memory notes (or tests) might not have created_at yet.
        for note in app.notes:
            if "created_at" not in note:
                note["created_at"] = None
        return render_template("home.html", notes=app.notes)

    @app.route("/notes/new", methods=["GET", "POST"])
    def new_note():
        if request.method == "POST":
            title = (request.form.get("title") or "").strip()
            body = (request.form.get("body") or "").strip()
            if not title:
                return render_template("new_note.html", error="Title is required", title=title, body=body)
            if not body:
                return render_template("new_note.html", error="Body is required", title=title, body=body)
            tags = parse_tags(request.form.get("tags") or "")
            created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            app.notes.append({"title": title, "body": body, "tags": tags, "created_at": created_at})
            return redirect(url_for("home"))
        return render_template("new_note.html")

    # TASK 02 will add a /notes/<idx>/delete route here.

    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=5000)
