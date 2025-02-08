Title: Building a Personal Website using a Static Site Generator
Date: 2024-11-15
Tags: python, static site generator
Summary: Static site hosted on GitHub Pages: [https://github.com/sahilds1/sahilds1.github.io](https://github.com/sahilds1/sahilds1.github.io)
Status: published

To start blogging about software projects, I built this site using Pelican, Sidecar, and GitHub

- [Pelican](https://github.com/getpelican/pelican): A static site generator tool that builds these web pages from content in text files and templatized HTML
- [Sidecar](https://github.com/seanh/sidecar): A Pelican "theme" of CSS stylesheets and HTML templates used by Pelican during the building of this site
- [GitHub](https://github.com/): A platform to host this site on GitHub Pages and build the web pages using Pelican and GitHub Actions

## Static Site Generator: `Pelican` 

Pelican's a Python based static site generator that has built-in blogging features and a variety  of community-created themes. 

Alternatives in other languages are: 

- [Jekyll](https://github.com/jekyll/jekyll): Ruby-based, notable for its integration with GitHub Pages
- [Hugo](https://github.com/gohugoio/hugo): Go-based, notable for its speed at building large sites
- [Eleventy](https://github.com/11ty/eleventy/): JavaScript-based, notable for its flexible HTML templating system

I chose Pelican because I wanted to use my site to blog and already had a Python development environment. 

After installing Pelican, you can set up a skeleton project using Pelican's `pelican-quickstart` tool. 

## Pelican Theme: `Sidecar`

Pelican has built in "simple" HTML templates that can be modified and styled using  CSS.

A variety of community created themes are available on GitHub

I chose to use the community created `Sidecar` theme  because I don't have experience with CSS.

## Hosting: `GitHub`

To have GitHub run `pelican` for you and build your site, you can use a GitHub Actions workflow  