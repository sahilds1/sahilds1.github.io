Title: Open URLs in Python Using `webbrowser`
Date: 2025-02-05  
Tags: python
Slug: python-webbrowser
Summary: Open URLs in Python Using `webbrowser`
Status: published

# TIL: The Python Standard Library’s webbrowser Module

The `webbrowser` module can open URLs in a web browser from a script:

```
webbrowser.open("https://www.python.org")
```

It selects the default browser can open URLs in a new window or a new tab:

``` 
webbrowser.open_new("https://www.python.org")
webbrowser.open_new_tab("https://www.python.org")
```

The `webbrowser` module can also be used from the command line

```
python -m webbrowser "https://www.python.org"
python -m webbrowser --new-window "https://www.python.org"
python -m webbrowser --new-tab "https://www.python.org"
```