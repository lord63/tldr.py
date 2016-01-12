# tldr.py

[![Latest Version][1]][2]
[![Build Status][3]][4]
[![Coverage Status][5]][6]
![Python Versions][7]


Yet another python client for [tldr][].


## Intro

tldr.py is a python client for [tldr][]: simplified and community-driven man pages.
Instead of the long man pages:

![tar-man-page][]

 tldr will give you several simple yet powerful examples:

![tar-tldr-page][]

The command examples are not good? Don't worry, you can set up your own 'tldr'!
They are just markdown files and you can modify them at your ease. Don't forget to
Share them with the community!

One more thing, tldr is just a simple version for the man page, it's **NOT** an
alternative. Sometimes, you should read the man pages patiently ;)


## Features highlight

* use local file, fast.
* support custom the output color.
* support fetch the latest tldr pages.
* support rebuild the index.


## Install

    $ (sudo) pip install tldr.py


## Usage

### Initialize

1. clone the tldr repo to somewhere(e.g. ~/code/tldr). We will use it when we look for a
command usage.

        $ cd ~/code
        $ git clone git@github.com:tldr-pages/tldr.git

2. init the configuration file, the default location for the configuration file is your
home directory, you can use the `TLDR_CONFIG_DIR` environment variable to point it to
another folder(e.g. $HOME/.config)

        $ tldr init
        Input the tldr repo path(absolute path): (e.g. /home/lord63/code/tldr/)
        Input your platform(linux, osx or sunos): (e.g. linux)
        Initializing the config file at ~/.tldrrc

and you configuration file should look like this:

    colors:
       command: cyan
       description: blue
       usage: green
    platform: linux
    repo_directory: /home/lord63/code/tldr

Don't worry about the `colors` option, it is for the output when you look for a command,
you can custom it by yourself.(Note that the color should be in ['black', 'red', 'green',
'yellow', 'blue', 'magenta', 'cyan', 'white'])

### Use tldr

look for a command usage:

    $ tldr find {{command}}

check for updates(so that we can get the latest man pages):

    $ tldr update

rebuild the index.json after you add some new pages:

    $ tldr reindex

Or you can use `tldr --help` to get the help message.


## FAQ

> Q: I want to add some custom command usages to a command, how to do it?

A: Find the location of the command page; add the command usages; done.

> Q: I want to add some custom command pages, how?

A: Add the comand pages to the right folder(e.g. /tldrrepo/pages/linux); rebuild the index; done.

> Q: I don't like the default color theme, how to change it?

A: Edit the tldr configuration file at `~/.tldrrc`; modify the color until you're happy with it.

> Q: I faided to update the tldr pages, why?

A: Actually, `tldr.py` just tries to pull the latest tldr pages for you, no magic behinds it. So the
reason why you faided to update is that `tldr.py` failed to pull the latest upstream, check the failing
output and you may know the reason, e.g. you make some changes and haven't commit them yet. You can
pull the pages by hand so you can have a better control on it.

> Q: Why use the git repo instead of the assets packaged by the official?

A: In fact, you can use the offical assets if you want, download the assets and extract it somewhere,
but `tldr.py` don't support update it using `tldr update`.

Use a git repo, you can:

* do the version control, yeah, use git.
* better for customization, just edit the pages and add new pages, they belongs to you. You can
  even maintain your own 'tldr'. If use the official assets, you'll always get the latest pages.


## Contributing

* It sucks? Why not help me improve it? Let me know the bad things.
* Want a new feature? Feel free to file an issue for a feature request.
* Find a bug? Open an issue please, or it's better if you can send me a pull request.

Contributions are always welcome at any time! :sparkles: :cake: :sparkles:


## License

MIT.

[1]: http://img.shields.io/pypi/v/tldr.py.svg
[2]: https://pypi.python.org/pypi/tldr.py
[3]: https://travis-ci.org/lord63/tldr.py.svg
[4]: https://travis-ci.org/lord63/tldr.py
[5]: https://codecov.io/github/lord63/tldr.py/coverage.svg?branch=master
[6]: https://codecov.io/github/lord63/tldr.py?branch=master
[7]: https://img.shields.io/pypi/pyversions/tldr.py.svg
[tldr]: https://github.com/tldr-pages/tldr
[tar-man-page]: https://cloud.githubusercontent.com/assets/5268051/10731428/5b5fd2fc-7c30-11e5-8cb1-4a3a24218ede.jpeg
[tar-tldr-page]: https://cloud.githubusercontent.com/assets/5268051/10731475/95df13fc-7c30-11e5-97d8-8090b6146208.jpeg
