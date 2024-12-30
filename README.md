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
pip install -e .

export OPENAI_API_KEY=your key here
export GEMINI_API_KEY=your key here
export ANTHROPIC_API_KEY=your key here
```

Run with `beaker notebook`

## Usage Notes

There are two contexts: `beaker_climate` and `mimi-modeling`. `beaker_climate` is used for general climate science questions in Python and `mimi-modeling` is used for questions about the Mimi integrated assessment models in Julia. The `mimi-modeling` context has only been extensively tested using Anthropic's Claude 3.5 Sonnet model as the primary model. Though it should work with other models, it may not perform as well.

### Docker Usage

To run the docker container, first copy `.beaker.conf.example` to `.beaker.conf` and set the LLM keys both there and in the `.env` file. Then use the following command:

```console
docker compose build
docker compose up
```

## License

`beaker-climate` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
