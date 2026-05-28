# Task 02 — Delete a note

## Goal
Add a "delete" button to each note on the homepage that removes that
note from the list. The route must accept a POST (not GET) so reloads
or browser pre-fetchers can't accidentally delete things.

## Acceptance criteria
- Each note rendered on `/` has a delete button (a `<form>` POST'ing to
  the new route is fine — no JavaScript required).
- A POST to `/notes/<idx>/delete` removes the note at that index from
  `app.notes` and redirects (302/303) to `/`.
- A GET to `/notes/<idx>/delete` returns **405 Method Not Allowed**.
- Deleting a non-existent index returns **404**.
- All tests in `tests/test_task_02.py` pass.

## Files you'll likely touch
- `app.py` — add the delete route
- `templates/home.html` — render a delete button per note

## Suggested workflow with Claude
1. `Read tasks/TASK_02.md and tests/test_task_02.py. Plan first.`
2. Confirm Claude understands that GET should 405, not 404.
3. Implement, then `pytest tests/test_task_02.py`.
4. Once green: `pytest` to make sure Task 01's tests still pass.

## Hints
- Restrict the route to `methods=["POST"]`; Flask will automatically
  return **405 Method Not Allowed** for any other verb (no extra code).
- For the 404 on a bad index, wrap the lookup in
  `try: ... except IndexError: abort(404)` — otherwise an out-of-range
  index becomes a 500.
- The homepage's delete button can be a tiny `<form method="POST"
  action="{{ url_for('delete_note', idx=loop.index0) }}">` — no
  JavaScript needed.
