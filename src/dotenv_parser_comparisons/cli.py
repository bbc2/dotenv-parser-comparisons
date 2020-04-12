import subprocess
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Sequence

import progressbar


@dataclass(frozen=True)
class Input:
    name: str
    value: bytes


@dataclass(frozen=True)
class Parser:
    name: str


@dataclass(frozen=True)
class Case:
    input_: Input
    parser: Parser


@dataclass(frozen=True)
class Output:
    value: bytes


@dataclass(frozen=True)
class Result:
    case: Case
    output: Output


def build_image(parser: Parser) -> None:
    subprocess.check_output(
        [
            "docker",
            "build",
            "--force-rm",
            "--tag",
            tag(parser),
            "--target",
            parser.name,
            "docker",
        ],
    )


def tag(parser: Parser) -> str:
    return f"dotenv-parser-comparisons:{parser.name}"


def run_case(case: Case) -> Output:
    value = subprocess.check_output(
        ["docker", "run", "--rm", "--env", "INPUT", tag(case.parser)],
        env={"INPUT": case.input_.value.decode("utf-8")},
    )
    return Output(value=value)


def show_bytes_in_pre(bytes_: bytes) -> str:
    string = bytes_.decode("utf-8").replace("\n", "<br>")
    return f"<pre>{string}</pre>"


def show_char_code(char: str) -> str:
    if char == "\n":
        return "\\n"
    if char == " ":
        return "␣"
    return char


def split_bytes(bytes_: bytes) -> str:
    return "&nbsp;".join(f"`{show_char_code(byte)}`" for byte in bytes_.decode())


def render_results(
    inputs: Sequence[Input], parsers: Sequence[Parser], results: Sequence[Result],
) -> str:
    values: Dict[Parser, Dict[Input, Output]] = defaultdict(dict)

    for result in results:
        values[result.case.parser][result.case.input_] = result.output

    out = ""
    header_line = " | ".join([f"{input_.name}" for input_ in inputs])
    out += f"| | {header_line} |\n"

    separator_line = " | ".join(["---"] * (len(inputs) + 1))
    out += f"| {separator_line} |\n"

    input_line = " | ".join(show_bytes_in_pre(input_.value) for input_ in inputs)
    out += f"| source file | {input_line} |\n"

    for parser in parsers:
        outputs = " | ".join(
            split_bytes(values[parser][input_].value) for input_ in inputs
        )
        unbreakable_hyphen = "&#8209;"
        unbreakable_name = parser.name.replace("-", unbreakable_hyphen)
        out += f"| {unbreakable_name} | {outputs} |\n"

    return out


def main():
    inputs = [
        Input(name="Basic", value=b"foo=ab"),
        Input(name="Escaped `z`", value=b"foo=a\\zb"),
        Input(name="Escaped and single-quoted `z`", value=b"foo='a\\zb'"),
        Input(name="Escaped and double-quoted `z`", value=b'foo="a\\zb"'),
        Input(name="Escaped `n`", value=b"foo=a\\nb"),
        Input(name="Escaped and single-quoted `n`", value=b"foo='a\\nb'"),
        Input(name="Escaped and doubel-quoted `n`", value=b'foo="a\\nb"'),
        Input(name="Quoted newline", value=b'foo="a\nb"'),
        Input(name="Non-escaped space", value=b"foo=a b"),
        Input(name="Non-escaped `#`", value=b"foo=a#b"),
        Input(name="Non-escaped spaced `#`", value=b"foo=a #b"),
        Input(name="Escaped spaced `#`", value=b'foo="a#b"'),
        Input(name="UTF-8", value="foo=é".encode("utf-8")),
        Input(name="Quoted UTF-8", value='foo="é"'.encode("utf-8")),
    ]
    parsers = [
        Parser(name="bash-5.0.0"),
        Parser(name="js-dotenv-6.2.0"),
        Parser(name="python-dotenv-0.9.1"),
        Parser(name="python-dotenv-0.10.1"),
        Parser(name="python-dotenv-0.12.0"),
        Parser(name="ruby-dotenv-2.6.0"),
    ]

    for parser in parsers:
        build_image(parser=parser)

    cases = [
        Case(input_=input_, parser=parser) for input_ in inputs for parser in parsers
    ]

    results = []
    for case in progressbar.progressbar(cases):
        results.append(Result(case=case, output=run_case(case)))

    print(render_results(inputs=inputs, parsers=parsers, results=results))


if __name__ == "__main__":
    main()
