# leetcode-list-builder

Add a list of questions to a favourite list of yours

# How to run

## Get your leetcode session id
Initialize session id variable. You can get it directly from your browser (if you're using chrome, cookies can be found here chrome://settings/cookies/detail?site=leetcode.com)

Linux/Macos
```
export LEETCODE_SESSION_ID="yyy"
```

Windows
```
set LEETCODE_SESSION_ID="yyy"
```

## Run it

Clone this repo. And go to the directory in command line window.

Then,
```
  python3 -m venv ./venv
  source venv/bin/activate
  pip install -r requirements.txt
  python build.py 
```

# Extra tools
* Chrome add-on [copy-selected-links](https://chrome.google.com/webstore/detail/copy-selected-links/kddpiojgkjnpmgiegglncafdpnigcbij?hl=en) . With it you can easily select multiple leetcode links from a web page
* [leetcode-anki](https://github.com/prius/leetcode-anki) can generate Anki decks based on a leetcode list id 


# Credits
* The project heavily relies on [python-leetcode](https://github.com/prius/python-leetcode)
* The project copied some code and doc from [leetcode-anki](https://github.com/prius/leetcode-anki)
