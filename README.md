# Read Only Data Center (RODC)

Currently used to serve static files for [amyip.net](https://amyip.net), and
hosted at https://rodc.amyip.net. It is used as an alternative to more involved
CDNs, file management systems, and CMSes.

## Installation

If you like RODC, you can self-host it.

### Server

Download the repository:

```
git clone https://github.com/amyipdev/rodc
cd rodc
```

Build a `venv`, activate it, and install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install gunicorn
```

(Optional) Launch a `tmux` session for persistence

Add a randomly-generated password/key to the server's shell config (commonly `~/.bashrc`):

```
export RODC_API_KEY="your_api_key"
```

Reload your shell config (exit and re-login).

Make the files directory:

```
cd rodc
mkdir files
```

Run the server:

```
gunicorn -b [::]:8081 server:app
```

(Optional) Use a reverse proxy, like `nginx`, to expose the RODC instance and proxy w/ HTTPS, HTTP2, QUIC, etc

### Client

Install using [pipx](https://github.com/pypa/pipx):

```
pipx install rodc-cli
```

Set the necessary variables in your shell config (commonly `~/.bashrc`):

```
export RODC_API_KEY="your_api_key"
export RODC_TARGET="https://rodc.yourserver.tld"
```

Reload your shell config (restart the terminal).

RODC is now installed as the `rodc` command.

## Usage

Send a file and keep the filename with `rodc -f`:

```
rodc -f yourfile.txt
```

Send a file and use a random filename with `rodc`: 

```
rodc yourfile.txt
```

Random filenames are 12 hex characters (from the file's SHA256) plus the original file extension.

Assuming no errors occur, you should get a message like the following:

```
200 files/abcdef123456.txt
```

This file would be accessible at rodc.yourserver.tld/f/abcdef123456.txt.

## Contributing

Feel free to submit an issue or PR! All contributions are under the GPL-2.0 license.

Please signoff your commits with the [DCO](https://en.wikipedia.org/wiki/Developer_Certificate_of_Origin)
by ending your commits with `Signed-off-by: Your Name <your@email.tld>`.
