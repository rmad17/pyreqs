# PyReqs
Better manage requirements.txt

Recently there was a really nice dependency management library released by Kenneth Reitz called pipenv. I was very excited and still am about it(The very first issue was raised by me regarding managing dependencies of libraries I install). However the problem started because of pipfile writing this in their README. `WARNING: This project is under active design and development. Nothing is set in stone at this point of time.`. I knew I could not use pipenv in production right now.

I had the following pain points with regular pip. I am sure you guys have to face it too. 

1. When I am am cleaning up dependencies may be once in 5 months I dont remember if a certain library in requirements.txt was installed by me or a dependency of another library installed by me? Is it still required? Lets leave it lest the system breaks.
2. How do I specify if a package has to be pinned in requirements.txt or dev-requirements.txt? Then I started to use a friend's script which was still better but had its own flaws. It had to be better I felt.

I did a lot of research and could not find anything decent and decided to write my own. 


## Introducing PyReqs

Lets say you do `pyreqs install django`. It will create a requirements.txt file if it does not exist and pin only the django package and none of its dependencies. This makes it easy to know which packages I am using later. You do `pyreqs remove django` and requirements.txt is updated as well. 
Its not done yet. `pyreqs install django-extensions --save-dev` and you shall have this updated to a dev-requirements.txt. `--save-test` puts it in a test-requirements.txt. You can also pass a filename to save it in a different file. Like this
`pyreqs install django-extensions --save-dev mydev.txt`

## Installation
`[sudo] pip install pyreqs`
This has not been tested in python2. I do not want to test in python2 either since I strongly belive we should move towards python3. However if their is some bug you can raise an issue or send a PR. If possible I will try to resolve it.

## Usage
Install
`pyreqs install django` <br>
`pyreqs install django-extensions --save-dev`<br>
`pyreqs install coverage --save-test my-test.txt`<br>

Remove
`pyreqs remove django`<br>
`pyreqs remove django-extensions --save-dev`<br>
`pyreqs remove coverage --save-test my-test.txt`<br>

```
Usage: pyreqs [OPTIONS] COMMAND [ARGS]...

  Entry point for pyreqs

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  install  Install the package via pip, pin the package...
  remove   Uninstall the package and remove it from...
  ```
## Note
`PyReqs` is not meant to be a competitor to any existing libraries like `pipenv`. Its simply meant as a workaround to make our life easy with pip and requirements till the time we have a better stable alternative.
