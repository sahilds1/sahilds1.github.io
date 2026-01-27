Title: Building a tool to copy-paste share terminal sessions using Claude Code for web via https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/
Date: 2025-10-23
Category: Link Blog
Tags: linkblog
Status: published

To share Claude Code CLI sessions, Simon Willison built [an app](https://tools.simonwillison.net/terminal-to-html) for sharing terminal sessions using GitHub Gists. The app implements a GitHub authentication flow using Cloudflare as an alternative to requiring users to paste in a GitHub Personal Access Token (PAT). He combined the functionality of previous tools for converting rich formatted text to HTML and saving GitHub Gists and implemented the app using Claude Code for web.

> Here’s the full prompt I used on claude.ai/code, pointed at my simonw/tools repo, to build the tool:
>
> Build a new tool called `terminal-to-html` which lets the user copy RTF directly from their terminal and paste it into a paste area, it then produces the HTML version of that in a textarea with a copy button, below is a button that says "Save this to a Gist", and below that is a full preview. It will be very similar to the existing `rtf-to-html.html` tool but it doesn't show the raw RTF and it has that Save this to a Gist button.
>
> That button should do the same trick that `openai-audio-output.html` does, with the same use of `localStorage` and the same flow to get users signed in with a token if they are not already.
>
> So click the button, it asks the user to sign in if necessary, then it saves that HTML to a Gist in a file called `index.html`, gets back the Gist ID and shows the user the URL `https://gistpreview.github.io/?6d778a8f9c4c2c005a189ff308c3bc47` - but with their gist ID in it.
>
> They can see the URL, they can click it (do not use `target="_blank"`) and there is also a "Copy URL" button to copy it to their clipboard.
>
> Make the UI mobile friendly but also have it be courier green-text-on-black themed to reflect what it does.
>
> If the user pastes and the pasted data is available as HTML but not as RTF skip the RTF step and process the HTML directly.
>
> If the user pastes and it's only available as plain text then generate HTML that is just an open `<pre>` tag and their text and a closing `</pre>` tag.


> I [figured out](https://gist.github.com/simonw/975b8934066417fe771561a1b672ad4f) the minimal Cloudflare worker necessary to implement the server-side portion of GitHub’s authentication flow. That code [lives here](https://github.com/simonw/tools/blob/main/cloudflare-workers/github-auth.js) and means that any of the HTML+JavaScript tools in my collection can implement a GitHub authentication flow if they need to save Gists.
