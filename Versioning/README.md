# Git & Versioning Anki Decks

Flashcard decks covering Git, version control concepts, and collaboration workflows — classified by difficulty level.

## Format

```
Front (question or term)[TAB]Back (answer or definition)
```

---

## Available Decks

| File | Description |
|------|-------------|
| `git_beginner.txt` | Basics: init, add, commit, push, pull, branches, merge, terminology |
| `git_intermediate.txt` | Rebase, stash, cherry-pick, reflog, hooks, submodules, worktrees, collaboration workflows |
| `git_pro.txt` | Internals (objects, packfiles, refs), custom merge drivers, filter-branch/filter-repo, performance, security, large-scale Git |

---

## Topic Index

### Beginner

#### 1. Version Control Fundamentals
- What is version control and why use it
- Centralized vs distributed version control (SVN vs Git)
- Repository, working tree, staging area (index), commit
- Git vs other DVCS (Mercurial, Bazaar)

#### 2. Git Basics
- git init, git clone
- git add, git status, git diff
- git commit, commit messages (conventional commits)
- git log, git show
- .gitignore patterns and syntax
- git rm, git mv
- HEAD, detached HEAD

#### 3. Branching & Merging Basics
- Creating and switching branches (git branch, git switch, git checkout)
- Fast-forward merge vs three-way merge
- Merge conflicts: detection, resolution, completing the merge
- git merge --abort
- Branch naming conventions (main, develop, feature/*, bugfix/*, release/*)

#### 4. Remote Repositories
- git remote add, git remote -v
- git push, git pull, git fetch
- Tracking branches (origin/main)
- upstream vs origin
- git clone --depth (shallow clone)

#### 5. Undoing Changes
- git restore (unstage, discard changes)
- git reset (soft, mixed, hard)
- git revert (creating an undo commit)
- git commit --amend
- Recovering deleted branches

---

### Intermediate

#### 6. Rebase & History Rewriting
- git rebase vs merge — when to use each
- Interactive rebase: squash, fixup, reword, edit, drop
- git rebase --onto
- Rebase conflicts and resolution
- Dangers of rewriting published history

#### 7. Stash, Cherry-Pick & Advanced Branching
- git stash push, pop, list, apply, drop
- git stash -p (partial stash)
- git cherry-pick — single commit and ranges
- git worktree — multiple working trees
- Orphan branches (git checkout --orphan)

#### 8. Collaboration Workflows
- Feature branch workflow
- Gitflow (develop, feature, release, hotfix branches)
- Trunk-based development
- Forking workflow (open source)
- Pull requests / Merge requests — review, approval, CI checks
- Code review best practices in Git

#### 9. Git Hooks
- Client-side hooks: pre-commit, commit-msg, pre-push, post-checkout
- Server-side hooks: pre-receive, update, post-receive
- Hook scripts: bash, Python, Node.js
- Sharing hooks via .githooks/ or tools (Husky, pre-commit framework)

#### 10. Submodules & Subtrees
- git submodule add, init, update, sync
- Submodule pinning (specific commit)
- git subtree add, pull, push, split
- Submodules vs subtrees — trade-offs
- Monorepo vs multi-repo strategies

#### 11. Tagging & Releases
- Lightweight vs annotated tags
- git tag -a, git push --tags
- Semantic versioning (SemVer) and Git tags
- Signing tags with GPG/SSH
- GitHub/GitLab releases and changelogs

#### 12. Reflog & Recovery
- git reflog — what it tracks, expiry
- Recovering lost commits with reflog
- Recovering from bad rebase/reset
- git fsck — finding dangling objects
- Garbage collection (git gc) and its effects

---

### Pro

#### 13. Git Internals
- Object model: blob, tree, commit, tag objects
- Content-addressable storage (SHA-1/SHA-256 hashing)
- The .git directory structure: objects/, refs/, HEAD, index, config
- Packfiles and deltification (git pack-objects, git verify-pack)
- Loose objects vs packed objects
- Index (staging area) binary format
- Ref storage: loose refs vs packed-refs

#### 14. Advanced History Manipulation
- git filter-repo (replacing filter-branch)
- Removing sensitive data from history (BFG Repo-Cleaner, filter-repo)
- Grafts and replace objects (git replace)
- Rerere (reuse recorded resolution)
- Custom merge drivers and merge strategies
- Octopus merges

#### 15. Git at Scale
- Monorepo tooling: sparse-checkout, partial clone, filesystem monitor
- git sparse-checkout set, cone mode
- Partial clone (--filter=blob:none, --filter=tree:0)
- Scalar / VFS for Git (Microsoft's large-repo solutions)
- Commit-graph, multi-pack-index, reachability bitmaps
- Git LFS (Large File Storage): track, push, pull, locking
- Shallow clones, treeless clones, blobless clones

#### 16. Git Security
- Commit signing with GPG and SSH keys
- Vigilant mode (unverified commit warnings)
- git bundle — offline repository transfer
- Transfer protocols: SSH, HTTPS, Git protocol, security considerations
- Preventing force-push: branch protection rules
- Secret scanning and pre-commit checks
- SHA-1 collision concerns and SHA-256 transition (git hash object)

#### 17. Git Server Administration
- Bare repositories (git init --bare)
- Git hosting internals: receive-pack, upload-pack
- Server-side hooks for CI/CD enforcement
- Repository mirroring (git clone --mirror, push --mirror)
- Repository maintenance: gc, prune, repack, maintenance run
- Alternates and shared object stores

#### 18. Broader Concepts & Theory Behind Git
- Data structures: DAGs, Merkle trees, fanout tables
- Graph theory: topological sorting, reachability, lowest common ancestor
- Cryptographic hashing: SHA-1/SHA-256 properties, collision resistance
- Content-addressable storage (CAS)
- Snapshot vs delta storage model
- Diff algorithms: Myers, patience, histogram
- Merge algorithms: three-way merge, recursive, ORT
- Compression: zlib/DEFLATE, delta encoding in packfiles
- Distributed systems: optimistic concurrency, eventual consistency, CAP theorem
- Immutability, garbage collection (mark-and-sweep), generation numbers
- Binary search in bisect and packfile index
- Software engineering principles: idempotency, referential transparency, single-writer principle

---

## Deck File Plan

| Level | File | Topics Covered |
|---|---|---|
| Beginner | `git_beginner.txt` | Fundamentals, basics, branching, remotes, undoing (1–5) |
| Intermediate | `git_intermediate.txt` | Rebase, stash, workflows, hooks, submodules, tags, reflog (6–12) |
| Pro | `git_pro.txt` | Internals, history manipulation, scale, security, server admin, broader concepts (13–18) |
