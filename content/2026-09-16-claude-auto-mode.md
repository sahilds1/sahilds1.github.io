Title: TIL: Claude Code Auto Mode Permissions and Docker Sandboxes
Date: 2026-09-16
Category: Today I Learned
Status: published

I mostly use Claude Code for projects right now and when Anthropic made "auto mode" the default I wanted to learn more about it.

## Auto Mode Blog Posts:

[Auto mode is now the default via Claude Blog](https://claude.com/blog/auto-mode-default-in-claude-code)

>Auto mode is designed to balance users’ desire not to be interrupted with a system that helps avoid harmful actions: instead of prompts, it routes each tool call through a classifier targeted at blocking actions that are irreversible, destructive, or aimed outside your environment. When the classifier blocks something, Claude usually finds a safer way to proceed on its own or asks you directly for the go-ahead; if it can't make progress—three blocks in a row, or twenty across a session—Claude Code falls back to manual approvals.

>We spent the last several months testing whether auto mode is as safe or safer than an average user clicking through prompts. We ran internal red-teaming, third-party red-teaming and prompt-injection evaluations, a controlled study with 1,053 paid testers, and analysis of real production sessions. On every measure we tested, auto mode matched or outperformed manual review.

>Auto mode also lets Claude work autonomously for longer stretches. This makes models built for long-running work, like Claude Opus 5, more practical to leave running for hours on large tasks. Reducing overhead for users also increases output. Among Teams & Enterprise adopters, auto mode users ship about 25% more PRs. 

[Breaking Claude Code Opus 5 Auto Mode via Simon Willison](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/)

> Johann Rehberger is one of the most credible prompt injection researchers active today. He found an attack against auto mode which he claims works 80% of the time, by tricking Claude Code into downloading and uncompressing a zip archive, then executing code that imports base64 without noticing that this will import and execute a local struct.py file extracted from the archive

> I agree with Johann's conclusion here: the only safe way to run agents if there's any risk of attracting the attention of an adversarial attack is with a sandbox: Run unattended coding agents in a container, VM or OS sandbox, Restrict network egress., Monitor your agents., Do not expose home directories, SSH keys, cloud credentials,… to the agent runtime.

## Auto Mode Claude Docs

[Configuration: Permissions and sandboxing via Claude Code Docs](https://code.claude.com/docs/en/permissions)

Permissions: How permissions interact with sandboxing
> Permissions and sandboxing are complementary security layers:
> - Permissions control which tools Claude Code can use and which files or domains it can access. They apply to Bash, Read, Edit, WebFetch, MCP, and every other tool, except that a deny or ask rule can’t block EndConversation while any other tool remains.
> - Sandboxing provides OS-level enforcement that restricts shell commands’ filesystem and network access. It applies only to Bash, PowerShell, and Monitor commands and their child processes.

Sandbox environments: 
> Choose an approach: You want to: Let Claude work unattended with --dangerously-skip-permissions or auto mode	Start with: The preconfigured dev container, any container or VM, or the sandbox runtime

Sandbox runtime: 
> The @anthropic-ai/sandbox-runtime package wraps an entire process in the same Seatbelt or bubblewrap isolation that the built-in Bash sandbox uses. Running Claude Code through the runtime constrains every tool, hook, and MCP server in the session, not only shell commands. The runtime is a beta research preview, and its configuration format may change as the package evolves.

Virutal machine:
> A dedicated virtual machine provides the strongest separation, with its own kernel and, in cloud or microVM deployments, its own virtualized hardware. Options include cloud instances, local hypervisors, and microVMs such as Firecracker. Use this approach when you are evaluating untrusted code, when your security policy requires kernel-level separation between the agent and the host, or when no host-level approach meets your compliance requirements.

>Docker Sandboxes provides a microVM with its own Docker daemon and workspace sync, which can run Claude Code on any host with Docker Sandboxes installed. It is a free, standalone product from Docker that does not require Docker Desktop.


## Docker Sandboxes Docs and Cheat Sheet 

Docker Docs: [Get started with local Docker Sandboxes](https://docs.docker.com/ai/sandboxes/get-started/)

Docker Docs: [Docker Sandboxes FAQ](https://docs.docker.com/ai/sandboxes/faq/)