# Global Go Engineering Workflow

When the current task involves Go, use the following workflow.

For non-trivial Go implementation or refactoring work, consult the
`go_skills_advisor` custom subagent before modifying code when the task
materially involves one or more of:

- database access or transactions
- error handling or error classification
- context.Context, cancellation, or deadlines
- concurrency or goroutine lifecycle
- HTTP, API, gRPC, or GraphQL behavior
- testing strategy for non-trivial behavior
- security-sensitive code
- performance-sensitive code
- dependency injection
- package or application architecture
- significant refactoring
- unfamiliar Go patterns where the installed Go skills may materially
  affect the implementation

The `go_skills_advisor` is advisory and read-only.

For applicable tasks:

1. Understand the user request and enough repository context to formulate
   a focused delegation.
2. Delegate the relevant engineering analysis to `go_skills_advisor`.
3. Let the advisor select and load the minimum relevant globally installed
   cc-skills-golang skills.
4. Wait for its handoff.
5. Evaluate the recommendations against explicit user requirements,
   repository-specific AGENTS.md instructions, existing architecture,
   and repository conventions.
6. The main agent remains solely responsible for all file modifications
   and implementation.
7. Run the repository-appropriate validation after implementation.
8. For higher-risk changes involving transactions, concurrency, security,
   context propagation, shared error contracts, or significant refactoring,
   use `go_skills_advisor` again for a read-only post-implementation review
   before finalizing.

Do not consult `go_skills_advisor` for trivial or mechanical work such as:

- formatting-only changes
- typo fixes
- comment-only edits
- straightforward renames
- generated-code updates
- obvious one-line changes that do not require a Go engineering decision

Do not directly load cc-skills-golang SKILL.md files into the main agent
when `go_skills_advisor` can perform that analysis instead.

Do not blindly follow generic skill guidance.
Explicit user requirements and repository-specific instructions take
precedence.

If the current task is not related to Go, ignore this Go workflow.
