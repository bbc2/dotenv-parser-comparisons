#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

log() {
    local msg=$1; shift

    local color='\033[1;34m'
    local reset='\033[0m'
    printf "$color$msg$reset\n"
}

gen_dotenv() {
    local value=$1; shift

    echo "foo=$value"
}

case_parser() {
    local dotenv=$1; shift
    local dir=$1; shift
    local cmd=$1; shift

    local name=$(basename "$dir")
    local file="$dir/.env"

    echo "$dotenv" > "$file"
    (cd "$dir"
    env "NAME=$name" $cmd || true
    )
    rm "$file"
}

case_dotenv() {
    local name=$1; shift
    local value=$1; shift

    local dotenv=$(gen_dotenv "$value")

    cat << EOF
### $name

\`\`\`
$dotenv
\`\`\`

| parser | output |
|--|--|
EOF

    local python_command='env PIPENV_DONT_LOAD_ENV=1 pipenv run -- python run.py'
    case_parser "$dotenv" 'cases/python-dotenv-0.9.1' "$python_command"
    case_parser "$dotenv" 'cases/python-dotenv-0.10.1' "$python_command"
    case_parser "$dotenv" 'cases/python-dotenv-0.12.0' "$python_command"
    case_parser "$dotenv" 'cases/bash-5.0.0' 'bash run.bash'
    case_parser "$dotenv" 'cases/js-dotenv-6.2.0' 'node run.js'
    case_parser "$dotenv" 'cases/ruby-dotenv-2.6.0' 'bundle exec -- ruby run.rb'

    echo
}

main() {
    case_dotenv 'Basic' 'ab'
    case_dotenv 'Escaped `z`' 'a\zb'
    case_dotenv 'Escaped and single-quoted `z`' "'"'a\zb'"'"
    case_dotenv 'Escaped and double-quoted `z`' '"a\zb"'
    case_dotenv 'Escaped `n`' 'a\nb'
    case_dotenv 'Escaped and single-quoted `n`' "'"'a\nb'"'"
    case_dotenv 'Escaped and double-quoted `n`' '"a\nb"'
    case_dotenv 'Quoted newline' '"a
b"'
    case_dotenv 'Non-escaped space' 'a b'
    case_dotenv 'Non-escaped `#`' 'a#b'
    case_dotenv 'Non-escaped spaced `#`' 'a #b'
    case_dotenv 'Escaped `#`' '"a#b"'
    case_dotenv 'UTF-8' 'é'
    case_dotenv 'Quoted UTF-8' '"é"'
}

main
