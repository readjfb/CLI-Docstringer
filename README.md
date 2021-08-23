# CLI-Docstringer
CLI Application to automatically generate docstrings for Python code using OpenAI's Codex engine. Note- You need to have your own API key to use this tool, as the Codex engine is in a closed beta.

All docstrings found in this project were automatically generated using the tool!

## Usage
1. Install dependencies as needed
2. Add API key to local bash environment variable using `export OPENAI_API_KEY="<key>`
3. View help page using `python docstr_maker.py -h`
4. Run script using `python docstr_maker.py -i <input file>`
5. To view verbose status messages, use `-v` flag
6. To edit the file in place, use the `-s` flag
7. To specify output file, use `-o <output file>`

## Help Sequence

```

Adds Python docstrings to functions
Appends _ds to output filename by default

Usage:
    python docstr_maker.py -i <input_file>

Optional args:
 -o <output_file>
 -v Verbose
 -s Use input file as output file
    Incompatable when used with -o
 -h Displays help message

Example:
    python docstr_maker.py -i <input_file> -s
    python docstr_maker.py -i <input_file>
    python docstr_maker.py -i <input_file> -o <output_file> -v

```
