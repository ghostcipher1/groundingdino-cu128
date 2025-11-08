# GitHub Setup Instructions

## Repository is Ready for Publishing! 🚀

You have successfully initialized a Git repository with all files committed. Follow these steps to publish to GitHub.

## Step 1: Create GitHub Repository

### Option A: Via GitHub Website (Recommended)

1. Go to [GitHub](https://github.com/new)
2. **Repository name**: `groundingdino-cu128`
3. **Description**: `GroundingDINO upgraded for PyTorch 2.7+ and CUDA 12.8 - Maintained fork with dual import support`
4. **Visibility**: Public
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Option B: Via GitHub CLI

```bash
gh repo create groundingdino-cu128 \
  --public \
  --description "GroundingDINO upgraded for PyTorch 2.7+ and CUDA 12.8 - Maintained fork" \
  --source=. \
  --remote=origin
```

## Step 2: Add Remote and Push

Once you've created the repository on GitHub, run:

```bash
# Add the remote (replace YOUR-USERNAME with ghostcipher1)
git remote add origin https://github.com/ghostcipher1/groundingdino-cu128.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main
```

## Step 3: Verify Upload

Check that everything is on GitHub:

```bash
# Open repository in browser
gh repo view --web
# Or manually go to: https://github.com/ghostcipher1/groundingdino-cu128
```

You should see:
- ✅ All 63 files
- ✅ README.md with badges displayed
- ✅ LICENSE file visible
- ✅ .github/workflows/ directory with 4 workflows

## Step 4: Enable GitHub Actions

1. Go to repository **Settings → Actions → General**
2. Under "Actions permissions":
   - Select "Allow all actions and reusable workflows"
3. Under "Workflow permissions":
   - Select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"
4. Click "Save"

## Step 5: Configure Branch Protection (Optional but Recommended)

1. Go to **Settings → Branches**
2. Click "Add branch protection rule"
3. Branch name pattern: `main`
4. Enable:
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - Select status checks: `test`, `build-cpu`, `check-package`
   - ✅ Require conversation resolution before merging
5. Click "Create"

## Step 6: Set Up PyPI Publishing (For Releases)

### Option A: Trusted Publishing (Recommended - No Secrets Needed!)

1. Go to [PyPI](https://pypi.org/) and log in
2. Navigate to **Account settings → Publishing**
3. Scroll to "Add a new pending publisher"
4. Fill in:
   - **PyPI Project Name**: `groundingdino-cu128`
   - **Owner**: `ghostcipher1`
   - **Repository name**: `groundingdino-cu128`
   - **Workflow name**: `release.yml`
   - **Environment name**: (leave empty)
5. Click "Add"

Now when you create a GitHub Release, it will automatically publish to PyPI!

### Option B: API Token (Alternative)

1. Go to [PyPI](https://pypi.org/) → **Account settings → API tokens**
2. Click "Add API token"
3. Token name: `groundingdino-cu128-github-actions`
4. Scope: "Project: groundingdino-cu128" (create project first if needed)
5. Copy the token (starts with `pypi-`)
6. In your GitHub repo: **Settings → Secrets and variables → Actions**
7. Click "New repository secret"
8. Name: `PYPI_API_TOKEN`
9. Value: Paste the token
10. Click "Add secret"

Then update `.github/workflows/release.yml` to use the token instead of trusted publishing.

## Step 7: Create Your First Release

### Test on Test PyPI First (Optional)

```bash
# Trigger release workflow manually for Test PyPI
gh workflow run release.yml -f test_pypi=true

# Check workflow status
gh run watch
```

### Create Official Release

```bash
# Create and push tag
git tag -a v0.2.0 -m "Release v0.2.0: Initial CUDA 12.8 support"
git push origin v0.2.0

# Then create GitHub Release
gh release create v0.2.0 \
  --title "v0.2.0 - Initial Release" \
  --notes "$(cat CHANGELOG.md | sed -n '/## \[0.2.0\]/,/## /p' | sed '$ d')"
```

Or via GitHub UI:
1. Go to **Releases → Draft a new release**
2. Click "Choose a tag" → Type `v0.2.0` → "Create new tag"
3. Title: `v0.2.0 - Initial Release`
4. Description: Copy from CHANGELOG.md
5. Click "Publish release"

This will automatically:
- ✅ Run all CI tests
- ✅ Build wheels
- ✅ Publish to PyPI
- ✅ Verify installation

## Step 8: Add Repository Topics

Improve discoverability by adding topics:

1. Go to repository homepage
2. Click ⚙️ (gear icon) next to "About"
3. Add topics:
   - `grounding-dino`
   - `object-detection`
   - `pytorch`
   - `cuda`
   - `computer-vision`
   - `deep-learning`
   - `zero-shot-detection`
   - `cuda-12`
4. Add website: Leave empty or add docs URL
5. Click "Save changes"

## Step 9: Verify Everything Works

Run these checks:

```bash
# Check workflows are enabled
gh workflow list

# View repository
gh repo view

# Check latest commit
git log -1 --stat

# Verify CI will run
gh workflow view ci.yml
```

## Current Repository Status

**Commit:** `678dd8d`
**Files:** 63
**Lines:** 11,887+ insertions

**Key Files Present:**
- ✅ Source code (groundingdino/, shadow_dino/)
- ✅ Tests (tests/)
- ✅ Documentation (README.md, CONTRIBUTING.md, SECURITY.md)
- ✅ CI/CD (4 GitHub Actions workflows)
- ✅ Templates (PR template, 2 issue templates)
- ✅ License (Apache 2.0)
- ✅ Build config (pyproject.toml, setup.py)

## Troubleshooting

### "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/ghostcipher1/groundingdino-cu128.git
```

### "Permission denied (publickey)"
Use HTTPS instead of SSH, or set up SSH keys:
```bash
git remote set-url origin https://github.com/ghostcipher1/groundingdino-cu128.git
```

### Workflows not running
1. Check Settings → Actions is enabled
2. Verify workflow YAML syntax: `gh workflow view ci.yml`
3. Check workflow run logs: `gh run list`

## Next Steps After Publishing

1. **Star the original repo**: https://github.com/IDEA-Research/GroundingDINO
2. **Create announcement**: Consider posting on relevant forums/communities
3. **Monitor issues**: Set up notifications for new issues
4. **Plan v0.3.0**: Start planning next features

## Support

If you encounter issues:
- Check [CI/CD Setup Documentation](.github/CI_CD_SETUP.md)
- Review [Contributing Guidelines](CONTRIBUTING.md)
- Open an issue in your repository

---

**Ready to publish?** Follow Steps 1-3 above to push to GitHub! 🚀
