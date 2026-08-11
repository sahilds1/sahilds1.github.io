Title: Link: Context engineering with Dex Horthy via The Pragmatic Engineer
Date: 2026-07-15
Category: Link Blog
Status: published


>It's kind of like de-abstracting a lot of the abstractions that have been layered on top. So you have a rag, you have memory, you have agentic history, you have structured output. You have all these things that are like different ideas in the frame of agentic programming. And at the end of the day,
they're all like different ways to pass tokens into a model and ask it to produce usually some structured output. And on. And understanding this. That is a lot more powerful than trying to learn memory and trying to pick some agent framework off the shelf and some memory framework off the shelf.
I mean, these things are all really good if you want to get to like 80%, you want to get a really good demo. But when you have to go from 80% 90 % to 95%. 95% or 99%, you need to go down a level and think about what's everything we're putting into
the context window, what order is it going in, depending on which model we're doing. And all of this stuff matters. You have all of these levers that you can pull. And it just felt like the right abstraction for thinking about how do I get AI to do the thing I want as accurately as possible.


>I was talking about this with someone this morning Um, about like when. you're working with LLM. LLMs, one of the things I like to say is kind of like make it run, make it right, make it fast. See if the world's best LLM at the time,
I think we did a podcast episode that at the time was like 03. See if 03 can solve your problem. And then give it to people and see if they want that. And then if people want it and use it a lot, then go do a bunch of context engineering because your engineering time is always the bottleneck.
Like humans trying to figure out and solve problems and build evals and improve and try different dimensions or set up JEPA or whatever it is, is always going to be more expensive than just using a smarter model. Until you have millions of requests a day. And then it's like, okay,
we're going to do a bunch of context engineering, break this up into three calls and get it to work on GPT-40. And then we're going to take two of those and make those two work on GPT-40. I'm using old model names. But the point is like for a certain task in your workflow,
can you get GPT-OSS-120B, which is like one one thousandth of the cost of Opus? Can you get it to solve parts of the problem so that the tokens and the things you're using the smartest frontier models for are just the thing. Things that you really need that level of intelligence?
But you shouldn't go build all of that and overengineer it until you've proved that you need it, that it's valuable, that it's like, OK, this is now I'm going to get to Eli Goldratt. And like, what is the he had this book, The Goal, right? It was about how to model your factory.
And I'm sure we'll get to that when we talk about software factories. It was like, what is the bottleneck in your system? And one day it will be latency and cost. But it's probably not that when you first start out. And context engineering is how you move from the you add human effort to
the equation to improve the efficiency, the speed, the price, the cost efficiency of your system. Interesting.


>Oh, these are actually like tactical execution docs. I do the research and do the plan. I do The Implementation. I throw the docs out. And the next time I need research,
I just do it from scratch because tokens are cheap and my time is expensive. And the amount of time I might waste if I reuse a research that is no longer in sync with this real state of the code base. So we just create it live every time. This is why context engineering still matters.
Creating artifacts that compress the state of the code base and compress the intent of the builder into small things that can be reused in the future for the scope of a task is a very powerful tactical approach. But it's not a thing. I have very few opinions on what sorts of docs
that you should leave lying around your code base that are evergreen. I've seen people try to maintain parity between documentation or specs and the code itself. And I don't think anyone actually found it very useful. You can do it and it works, but it's the ratio of the effort it takes to keep them up to date.


>But designing the end state of the software, the architecture and the program design. Models are not great at.
They make a lot of like, they make decisions and sometimes they're right and sometimes
they're wrong. so we want to have a human in the loop there. And then the steps to get there, we talked about this before, but models love making what I call like horizontal plans. If you ask a model, like build a plan of steps to go build this app, It's like cool,
we're going to do the database and then we're gonna do the services layer. Then we're going to do the API and then we're going to do the front end. I was like, well, that actually kind of sucks because we're going to be on the other side of 2000 lines of code.
And let's imagine this is an existing code base, right? We're going to make changes to all these different parts of the system. I can't test it till the end. And so what I would do is like, OK, how would I have built this if I were building my hand? Well, OK,
I would probably create a mock API endpoint with fake data and then I would go kind of get the front end kind of how I want it to look. And then I would actually go like build a services layer and actually wire the data through. And then I would make a database migration and make my new table.
And then I would actually add a lot of business logic. And then I would add a bunch of air. Error handling. And it's completely orthogonal to how models will write the database layer and all the error handling without Like anyone's ever touched. Touched or seen the code or whatever it is.
And so this is another place where we like to have humans involved because humans have really good taste and judgment and like I would rather read five separate little mini-diffs of like things that. That I can manually verify and explore than read 2,000 lines of code and be like, well, it's not working. I don't know where.


Via: [https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy](https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy)