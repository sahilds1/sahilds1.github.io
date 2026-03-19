Title: Link: Building a C compiler with a team of parallel Claudes via Engineering at Anthropic
Date: 2026-02-05
Category: Link Blog
Status: published

To stress test the limits of LLMs today, Nicholas Carlini used a team of Claude Opus 4.6 agents to build a Rust-based C compiler. The "agent team" approach (multiple Claude instances working in parallel) required him to design and build a harness of scaffolding, tests, environment, and feedback so they could work on a shared codebase without his intervention. 

He tasked 16 agents with the project, and they built a C compiler for just under $20,000 in API costs. The compiler can build a bootable Linux 6.9 kernel and compile SQLite, Postgres, and Redis, but has limitations he wasn't able to fix without breaking existing functionality.

> The compiler, however, is not without limitations. These include:
>
> * It lacks the 16-bit x86 compiler that is necessary to boot Linux out of real mode. For this, it calls out to GCC (the x86_32 and x86_64 compilers are its own).
> * It does not have its own assembler and linker; these are the very last bits that Claude started automating and are still somewhat buggy. The demo video was produced with a GCC assembler and linker.
> * The compiler successfully builds many projects, but not all. It's not yet a drop-in replacement for a real compiler.
> * The generated code is not very efficient. Even with all optimizations enabled, it outputs less efficient code than GCC with all optimizations disabled.
> * The Rust code quality is reasonable, but is nowhere near the quality of what an expert Rust programmer might produce.
>
> The resulting compiler has nearly reached the limits of Opus's abilities. I tried (hard!) to fix several of the above limitations but wasn't fully successful. New features and bugfixes frequently broke existing functionality.

Via: [https://www.anthropic.com/engineering/building-c-compiler](https://www.anthropic.com/engineering/building-c-compiler)