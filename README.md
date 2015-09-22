# tldr.py

[![Latest Version][1]][2]

Yet another python client for [tldr][].


## Install

    $ (sudo) pip install tldr.py


## Usage

### Initialize

1. clone the tldr repo to somewhere(e.g. ~/code/tldr). We will use it when we look for a
command usage.

        $ cd ~/code
        $ git clone git@github.com:tldr-pages/tldr.git

2. init the configuration file.

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

Or you can use `tldr --help` to get the help message.


## Contributing

* It sucks? Why not help me improve it? Let me know the bad things.
* Want a new feature? Feel free to file an issue for a feature request.
* Find a bug? Open an issue please, or it's better if you can send me a pull request.

Contributions are always welcome at any time! :sparkles: :cake: :sparkles:


## License

MIT.

[1]: http://img.shields.io/pypi/v/tldr.py.svg
[2]: https://pypi.python.org/pypi/tldr.py
[tldr]: https://github.com/tldr-pages/tldr
