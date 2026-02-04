Title: Link: Vibing a non-trivial Ghostty feature via Mitchell Hashimoto
Date: 2025-10-10
Category: Link Blog
Status: published

To make Ghostty update notifications unobtrusive, Mitchell Hashimoto built a feature that shows them within the terminal window using Amp (an agentic coding tool). He shares all 16 of his agentic coding sessions (totaling $15.98 in token spend) and provides context about his process and reasoning. 

His agentic coding techinques include creating a plan before writing any code, guiding the agent to clean up and document code, creating a file with a scaffold of incomplete functions and TODOs and asking the agent to complete it, and asking the agent what else he might be missing. 

>So I pulled out my AI tooling. Absolutely not. I began by coming up with a rough plan of how I wanted this to work. Ghostty uses Sparkle, an extremely popular macOS update framework. I poked around their docs and found that they support custom UI through Obj-C protocols. You have to reimplement a ton of stuff from scratch, but it is possible. Okay, so I had a rough idea of backend.


> Another thing to notice is that I ask it to only create a plan and not to write any code. Since this is a relatively vague request, it's important that I review a plan before it goes off and does a ton of work (and spends a ton of tokens doing it). Tip: Creating a comprehensive plan interactively with an agent is a really important first-step for anything non-trivial. I usually also save it out (via the agent) to something like spec.md and in future sessions I can say "Consult the @spec.md and work on some task".


>I spend the next few sessions guiding the agent to clean up the code. The cleanup step is really important. To cleanup effectively you have to have a pretty good understanding of the code, so this forces me to not blindly accept AI-written code. Subsequently, better organized and documented code helps future agentic sessions perform better. I sometimes tongue-in-cheek refer to this as the "anti-slop session".


>I manually created a file with a scaffold of incomplete functions and various TODO comments. I then started a session to complete that work for me: Tip: AI is very good at fill-in-the-blank or draw-the-rest-of-the-owl. My pattern here of creating scaffolding with descriptive function names, parameters, todo comments, etc. is a really common one for me and it works very well. 


>My last prompt to an agent is always to ask what else I might be missing. I do this regardless of if I manually wrote the code myself or not. This highlighted some real issues, so I went ahead and asked it to implement them. I find its easier to tell the agent "okay just do it all" rather than ask it specific things to do, since I can always easily clean it up in selective commits later.

Via: [https://mitchellh.com/writing/non-trivial-vibing](https://mitchellh.com/writing/non-trivial-vibing)