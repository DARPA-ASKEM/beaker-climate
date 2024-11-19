# beaker-climate

[![PyPI - Version](https://img.shields.io/pypi/v/beaker-climate.svg)](https://pypi.org/project/beaker-climate)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beaker-climate.svg)](https://pypi.org/project/beaker-climate)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
# Install Julia
curl -fsSL https://install.julialang.org | sh -s -- -y
export PATH="/root/.julialup/bin:${PATH}"

# Set up Julia environment
julia -e 'using Pkg; Pkg.add("Mimi"); Pkg.add("JSON3"); Pkg.add("DisplayAs"); using Mimi'

# Install Mimi Julia library
julia -e 'using Pkg; Pkg.add("Mimi")'

# install beaker-climate contexts
pip install -e climate-python
pip install -e mimi-julia

export OPENAI_API_KEY=your key here
export GEMINI_API_KEY=your key here
```

Run with `beaker notebook`

## License

`beaker-climate` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
