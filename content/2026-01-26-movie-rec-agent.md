Title: Link: Building a Movie Recommendation Agent via Rok
Date: 2026-01-26
Category: Link Blog
Status: published

To find movies to watch with his wife, Rok built [movieagent.io](movieagent.io) for movie recommendations using AI agents. He finds movies gathered from The Movie Database (TMDB) instead of letting the AI recommend movies directly because LLMs have a knowledge cutoff date and he's found they're bad at recommending diverse movies. He uses two agents working together to manage the conversation flow and search instead of a single agent because he found that a single agent struggles with both responsibilities. For the embeddings, he augmented the movie metadata with descriptions of how a movie feels and looks using LLMs and found that they captured the semantics of the movie well. For the movies that were not available during model training, he included user reviews from the TMDB data. To evaluate if the recommendations would generalize to different types of users he used another agent to emulate responses from different personas.

> When I'm talking about *the agent*, I'm really talking about two agents working together. First, I have the main movie agent working as the orchestrator, and a separate search agent working as a sub-agent.
>
> The movie agent is powered by Claude Sonnet 4.5. Its role is to drive the session and manage the conversation arc. It's ultimately responsible for delivering the recommendations to the user. It delegates searches as detailed plain-text tasks, and leaves them to the search agent to interpret and decompose.
>
> Movie agent can use the following tools:
> * ask_categorical_question: Presents the user with a multiple-choice question (e.g., "What's the mood tonight?" with options like "Something light," "Edge-of-my-seat tension," "Make me cry"). Used early in the conversation to establish broad direction.
> * ask_duel_question: Shows two movies side-by-side and asks the user to pick one. The choice signals preference direction without requiring the user to articulate why. Duel winners become concrete anchors for subsequent searches.
> * search_movies_task: Delegates a natural language search task to the search agent. The movie agent describes what it's looking for in plain English; the search agent figures out how to find it.
> * submit_candidates: Presents 10-15 candidate movies to the user for filtering. Users can veto films they've already seen or aren't in the mood for.
> * submit_recommendations: Ends the session with 3-5 final recommendations, each accompanied by a personalized note explaining why this film fits tonight's mood.
>
> The search agent, meanwhile, is powered by Haiku 4.5 which is fast, cheap, and good enough for search tasks in my experience.
>
> Search agent can use the following tools:
> * embeddings_search: Queries the movie embedding space with a text description and optional positive/negative movie anchors. Supports filtering by year, genre, rating, and runtime. Returns up to 10 results per query.
> * keyword_search: Looks up movies by exact metadata: director, actor, title fragments. Used sparingly when the task requires precise matching rather than semantic similarity.
> * submit_search_results: Returns the aggregated results to the movie agent, formatted with semantic IDs and brief explanations of why each film matches the task.

> Why not one monolithic agent? I found that a single agent struggles with the dual responsibility of managing the conversation flow and search. A monolithic agent would need to have all of the tools needed for asking questions and searching, and it has been established that more tools usually lead to worse overall agent performance.
>
> It's also difficult to tailor a single system prompt for both of those tasks because they are so distinct. The context window would grow rapidly if I mix orchestration with numerous searches. By keeping them separate, I can make the search agent focus on the task at hand with a clean context window. Not to mention the cost savings because I can outsource the search tasks to a cheaper model. Accumulating steps across sessions, I've found that the search agent takes 10x more steps compared to the movie agent.


Via: [https://rokn.io/posts/building-movie-recommendation-agent]](https://rokn.io/posts/building-movie-recommendation-agent)