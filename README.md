# passwordgenerator
A psuedo-random password generator that was built with a TDD approach

## Usage
```bash
 generator.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  passphrase
  password

```

### Passwords
```bash
Usage: generator.py password [OPTIONS] LENGTH

Arguments:
  LENGTH  [required]

Options:
  -u, --uppercase  [default: False]
  -d, --digits     [default: False]
  -s, --symbols    [default: False]
  --help           Show this message and exit.
```
### Passphrases
```bash
Usage: generator.py passphrase [OPTIONS] [SEPARATOR]

Arguments:
  [SEPARATOR]  [default:  ]

Options:
  -w, --word-count INTEGER  [default: 3]
  -c, --capitalize          [default: False]
  --help                    Show this message and exit.
```
