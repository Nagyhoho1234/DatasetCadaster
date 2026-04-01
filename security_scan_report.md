# Security Scan Report -- Dataset Cadaster

**Scan date:** 2026-03-31
**Scanned by:** Claude Code (automated)
**Scope:** All files in `C:\DatasetCadaster` including git history
**Total files scanned:** ~80 files (HTML, JS, JSON, Python, YAML, MD, SVG, etc.)

---

## Summary

| Risk Level | Count |
|------------|-------|
| **HIGH**   | 2     |
| **MEDIUM** | 5     |
| **LOW**    | 4     |

---

## HIGH Risk Findings

### 1. Personal name and institutional email in ALL git commits

- **Location:** Git history (every commit)
- **What was found:** Every commit is authored by `Prof. Zsolt Zoltan Feher Dr. <feher.zsolt@agr.unideb.hu>` -- full academic name with title and institutional email address from the University of Debrecen.
- **Risk:** HIGH -- Pushing this repo to GitHub will expose the author's full name, academic title, and work email in the public git log. This cannot be removed by deleting files; it is embedded in every commit object.
- **Recommended action:** Before publishing, rewrite git history to replace the author info:
  ```bash
  git filter-branch --env-filter '
    export GIT_AUTHOR_NAME="nagyhoho1234"
    export GIT_AUTHOR_EMAIL="nagyhoho1234@users.noreply.github.com"
    export GIT_COMMITTER_NAME="nagyhoho1234"
    export GIT_COMMITTER_EMAIL="nagyhoho1234@users.noreply.github.com"
  ' --tag-name-filter cat -- --branches --tags
  ```
  Or use `git-filter-repo` (faster, recommended by Git):
  ```bash
  git filter-repo --name-callback 'return b"nagyhoho1234"' --email-callback 'return b"nagyhoho1234@users.noreply.github.com"'
  ```

### 2. Personal name in landing page HTML (visible to all visitors)

- **File:** `app/landing.html`, lines 10 and 273
- **What was found:**
  - Line 10: `<meta name="author" content="Feher Zsolt Zoltan">`
  - Line 273: `<div>&copy; 2026 Feher Zsolt Zoltan | Data sources verified as of March 2026</div>`
- **Risk:** HIGH -- Full real name displayed publicly in the page and HTML metadata.
- **Recommended action:** Replace with "Dataset Cadaster Contributors" or the GitHub username "nagyhoho1234", depending on preference.

---

## MEDIUM Risk Findings

### 3. `__pycache__` bytecode file tracked in git

- **File:** `scripts/__pycache__/check_health.cpython-313.pyc` (tracked in git)
- **What was found:** A compiled Python bytecode file is committed to the repository.
- **Risk:** MEDIUM -- `.pyc` files can sometimes contain file path information from the build machine (potentially revealing the local username `de8xh`). They are also unnecessary clutter in a public repo.
- **Recommended action:** Remove from git tracking and add to `.gitignore`:
  ```bash
  git rm -r --cached scripts/__pycache__
  echo "__pycache__/" >> .gitignore
  echo "*.pyc" >> .gitignore
  ```

### 4. No `.gitignore` file exists

- **File:** (missing) `.gitignore`
- **What was found:** The project has no `.gitignore` file at all.
- **Risk:** MEDIUM -- Future accidental commits of `.env` files, `__pycache__`, IDE configs, or other sensitive files are likely.
- **Recommended action:** Create a `.gitignore` with at minimum:
  ```
  __pycache__/
  *.pyc
  .env
  .env.*
  *.key
  *.pem
  node_modules/
  .vscode/
  .idea/
  ```

### 5. Placeholder text in `maintenance_plan.md` leaks template patterns

- **File:** `maintenance_plan.md`, line 775-776
- **What was found:**
  - `"maintainer": "Your Name"`
  - `"repository": "https://github.com/yourname/DatasetCadaster"`
- **Risk:** MEDIUM -- While not revealing actual personal info, the placeholder `yourname` looks unprofessional and might confuse users or contributors.
- **Recommended action:** Replace with the actual GitHub username or project org name (`nagyhoho1234` or `dataset-cadaster`).

### 6. Deleted files still recoverable in git history

- **Files:** `codex_prompt.txt`, `codex_map_review.txt` (deleted in commit `c67ac3f`)
- **What was found:** These files were added in commit `bb373f9` and deleted in `c67ac3f`. They contain debug prompts sent to a Codex AI. Content is purely technical (map bug debugging) with no personal info, but they reveal the AI-assisted development process.
- **Risk:** MEDIUM -- The content itself is harmless, but if you want to keep the AI-assisted development private, these remain accessible via `git show`.
- **Recommended action:** If the git history is being rewritten anyway (for Finding #1), these will be handled automatically. Otherwise, no action needed.

### 7. Gemini conversation content in `review.md`

- **File:** `review.md` (3343 lines)
- **What was found:** Contains full copy-pasted Gemini Deep Research conversations including the user's prompts (e.g., "lots of bullshit, very low factual information content", "i asked to collect websites and not to bullshit about them"). Also contains a reference to "the user's location in Hungary" (line 960).
- **Risk:** MEDIUM -- The conversational tone reveals the author's communication style and location. The Gemini privacy footer text appears multiple times. No personal identifiers beyond the Hungary reference.
- **Recommended action:** Either remove this file before publishing (it seems to be research notes, not part of the app), or redact the conversational prompts and keep only the factual data tables.

---

## LOW Risk Findings

### 8. Fake/bot email in GitHub Actions workflow

- **File:** `.github/workflows/price-monitor.yml`, lines 41 and 114
- **What was found:** `git config user.email "bot@dataset-cadaster.local"`
- **Risk:** LOW -- This is a `.local` domain (non-routable), clearly a bot identity. Not a real email. However, the domain `dataset-cadaster.local` is fictional.
- **Recommended action:** Consider using the GitHub no-reply format instead: `github-actions[bot]@users.noreply.github.com`. This is the standard convention.

### 9. Placeholder email in QGIS plugin metadata

- **File:** `qgis-plugin/dataset_cadaster/metadata.txt`, line 7
- **What was found:** `email=placeholder@example.com`
- **Risk:** LOW -- This is clearly a placeholder, not real. But it looks unprofessional.
- **Recommended action:** Replace with a project contact email or the GitHub no-reply address.

### 10. GitHub repo reference hardcoded in JavaScript

- **File:** `app/index.html`, line 1465
- **What was found:** `const GITHUB_REPO = "nagyhoho1234/DatasetCadaster";`
- **Risk:** LOW -- This is the public GitHub username the user intends to use. It powers the "Submit price update to GitHub Issues" feature. This is intentional and appropriate.
- **Recommended action:** No action needed. Confirm this is the correct repo path before publishing.

### 11. localStorage key names

- **Files:** `app/index.html`, `app/shared.js`, `app/landing.html`
- **What was found:** Keys used: `dc-theme`, `dc-bookmarks`, `dc-notes`, `dc-price-updates`, `dc-lang`
- **Risk:** LOW -- All key names are generic, prefixed with `dc-`, and contain no sensitive patterns. No PII is stored in the keys themselves. Values are user-generated (notes, bookmarks) stored only in the user's own browser.
- **Recommended action:** No action needed. This is standard practice.

---

## Items Checked -- No Issues Found

| Check | Result |
|-------|--------|
| API keys, tokens, secrets, passwords | None found |
| `.env` files or credential files | None present |
| Windows user paths (`C:\Users\de8xh\`) in code | Not found in any tracked file |
| Real IP addresses (private or public) | None found |
| `localhost` / `127.0.0.1` references in code | Only in `maintenance_plan.md` as an exclude pattern (appropriate) |
| Phone numbers | None found |
| Hungarian government IDs (TAJ, adoszam, szemelyi) | None found |
| Cadastral parcel numbers or real property data | None (all data is about dataset *catalogs*, not actual cadastral records) |
| `console.log` / debug statements | None found in any JS or HTML file |
| Internal network URLs | None found |
| Hardcoded credentials in Python scripts | None found |
| Sensitive TODO/FIXME/HACK comments | None found |

---

## Recommended Actions Before Publishing (Priority Order)

1. **MUST DO:** Rewrite git history to remove personal name and email from all commits (Finding #1)
2. **MUST DO:** Replace personal name in `app/landing.html` author meta and footer (Finding #2)
3. **SHOULD DO:** Create `.gitignore` and remove `__pycache__` from tracking (Findings #3, #4)
4. **SHOULD DO:** Clean up `maintenance_plan.md` placeholders (Finding #5)
5. **CONSIDER:** Remove or redact `review.md` before publishing (Finding #7)
6. **CONSIDER:** Update bot email in GitHub Actions to use standard `noreply` format (Finding #8)
7. **CONSIDER:** Update QGIS plugin placeholder email (Finding #9)
