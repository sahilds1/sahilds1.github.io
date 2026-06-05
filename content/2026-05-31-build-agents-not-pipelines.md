Title: Link: Build agents, not pipelines via Sean Goedecke
Date: 2026-05-31
Category: Link Blog
Status: published

Sean Goedecke describes two ways of using an LLM in a program — agents and "pipelines" — and advocates for agents while discussing the tradeoffs between them in terms of predictability, intelligence, context-gathering, multi-model pipelines, small contexts, safety and legibility.

> Here's how you might structure a trivial "summarize a bunch of information and email it to me" program as a pipeline:
> ```
> context = gather_context(various, data, sources)
> llm_response = llm_summarize(context)
> summary = parse(llm_response)
> email_me(summary, my_email)
> ```
> And here's how you'd do it as an agent:
> ```
> read_data_tool = build_read_data_tool(various, data, sources)
> email_tool = build_email_tool(my_email)
> run_agent(tools: [read_data_tool, email_tool])
> ```
> Overall, I'd suggest following these guidelines:
> 1. Use pipelines when you have strict requirements around context size
> 2. Use pipelines when you need to be able to accurately predict (or limit) GPU cost
> 3. Use pipelines when you have to use local models
> 4. Use agents when you're not confident you'll be able to assemble all of the relevant context in one shot
> 5. Use agents when the problem is hard enough that you're not sure a pipeline will be able to solve it
>
> When in doubt, use agents. I am aware of several AI projects that have migrated from pipelines to agents in the last year, but none that have gone the other way around. As a general point about software design, if you're not sure what to do, pick the solution that's easier to build and more likely to be able to solve your actual problem. If you want to change to a cheaper, pipeline-based system later on, at least you'll be able to compare it to a working agentic design and make an informed decision.



Via: [https://www.seangoedecke.com/build-agents-not-pipelines/](https://www.seangoedecke.com/build-agents-not-pipelines/)