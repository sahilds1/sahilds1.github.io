Title: Link: My AI Adoption Journey via Mitchell Hashimoto
Date: 2026-02-05
Category: Link Blog
Status: published

Mitchell Hashimoto wrote up his step by step journey of finding value in AI tooling. 

## Step 1: Drop the Chatbot

> Chatbots have real value and are a daily part of my AI workflow, but their utility in coding is highly limited because you're mostly hoping they come up with the right results based on their prior training, and correcting them involves a human (you) to tell them they're wrong repeatedly.

> To find value, you must use an agent. An agent is the industry-adopted term for an LLM that can chat and invoke external behavior in a loop1 At a bare minimum, the agent must have the ability to: read files, execute programs, and make HTTP requests.

## Step 2: Reproduce Your Own Work

> I quickly discovered for myself from first principles what others were already saying, but discovering it myself resulted in a stronger fundamental understanding.

> Break down sessions into separate clear, actionable tasks. Don't try to "draw the owl" in one mega session.
For vague requests, split the work into separate planning vs. execution sessions.
If you give an agent a way to verify its work, it more often than not fixes its own mistakes and prevents regressions.

## Step 3: End-of-Day Agents

> But, I once again quickly found different categories of work that were really helpful:

> Deep research sessions where I'd ask agents to survey some field, such as finding all libraries in a specific language with a specific license type and producing multi-page summaries for each on their pros, cons, development activity, social sentiment, etc.
Parallel agents attempting different vague ideas I had but didn't have time to get started on. I didn't expect them to produce something I'd ever ship here, but perhaps could illuminate some unknown unknowns when I got to the task the next day.
Issue and PR triage/review. Agents are good at using gh (GitHub CLI), so I manually scripted a quick way to spin up a bunch in parallel to triage issues. I would NOT allow agents to respond, I just wanted reports the next day to try to guide me towards high value or low effort tasks.
To be clear, I did not go as far as others went to have agents running in loops all night. In most cases, agents completed their tasks in less than half an hour. But, the latter part of the working day, I'm usually tired and coming out of flow and find myself too personally inefficient, so shifting my effort to spinning up these agents I found gave me a "warm start" the next morning that got me working more quickly than I would've otherwise.

## Step 4: Outsource the Slam Dunks

> More specifically, I would start each day by taking the results of my prior night's triage agents, filter them manually to find the issues that an agent will almost certainly solve well, and then keep them going in the background (one at a time, not in parallel).

> Meanwhile, I'd work on something else. I wasn't going to social media (any more than usual without AI), I wasn't watching videos, etc. I was in my own, normal, pre-AI deep thinking mode working on something I wanted to work on or had to work on.

## Step 5: Engineer the Harness

>This comes in two forms:

> Better implicit prompting (AGENTS.md). For simple things, like the agent repeatedly running the wrong commands or finding the wrong APIs, update the AGENTS.md (or equivalent). Here is an example from Ghostty. Each line in that file is based on a bad agent behavior, and it almost completely resolved them all.

> Actual, programmed tools. For example, scripts to take screenshots, run filtered tests, etc etc. This is usually paired with an AGENTS.md change to let it know about this existing.

> This is where I'm at today. I'm making an earnest effort whenever I see an agent do a Bad Thing to prevent it from ever doing that bad thing again. Or, conversely, I'm making an earnest effort for agents to be able to verify they're doing a Good Thing.


## Step 6: Always Have an Agent Running

>I'm not [yet?] running multiple agents, and currently don't really want to. I find having the one agent running is a good balance for me right now between being able to do deep, manual work I find enjoyable, and babysitting my kind of stupid and yet mysteriously productive robot friend.

> The "have an agent running at all times" goal is still just a goal. I'd say right now I'm maybe effective at having a background agent running 10 to 20% of a normal working day. But, I'm actively working to improve that.


Via: [https://mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey)