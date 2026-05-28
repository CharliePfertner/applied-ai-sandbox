# Setting up the cohort sandbox repo on GitHub

These files are a template for the cohort's hands-on training repo.
To turn them into a live repo for interns to fork:

## 1. Create the repo on GitHub
Under the `Code2College-Content` org, create a public repo named **applied-ai-sandbox**.
Don't initialize it (no README, .gitignore, or license — we have those here).

## 2. Push these template files

```bash
cd scripts/applied_ai_sandbox_template
git init
git add .
git commit -m "Initial sandbox scaffold for Applied AI Cohort"
git branch -M main
git remote add origin git@github.com:Code2College-Content/applied-ai-sandbox.git
git push -u origin main
```

## 3. Verify it works

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest                    # Task 01 + Task 02 should be RED
python app.py             # http://localhost:5000 should show the homepage
```

The tests should be **failing** right now — that's the point. Interns fix
them as they work the tasks.

## 4. Settings (recommended)
- **Branch protection:** require pull request reviews on `main` so
  interns can't accidentally merge to upstream.
- **Issue templates:** optional, but a "Propose a task" template helps
  motivated interns suggest extra tasks.
- **Discussions:** enable so interns can ask questions on the repo
  itself instead of only in Slack.

## 5. Link from the hub
Update `app/templates/applied_ai/sandbox.html` and Module 2 step links
if the repo URL ever moves. (Both currently point at
`https://github.com/Code2College-Content/applied-ai-sandbox`.)
