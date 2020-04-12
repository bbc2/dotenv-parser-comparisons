Generated by [bbc2/dotenv-parser-comparisons](https://github.com/bbc2/dotenv-parser-comparisons)

| | Basic | Escaped `z` | Escaped and single-quoted `z` | Escaped and double-quoted `z` | Escaped `n` | Escaped and single-quoted `n` | Escaped and doubel-quoted `n` | Quoted newline | Non-escaped space | Non-escaped `#` | Non-escaped spaced `#` | Escaped spaced `#` | UTF-8 | Quoted UTF-8 | Variable | Variable undefined | Variable followed by dot | Variable followed by hyphen | Variable followed by underscore | Variable with braces | Variable with braces undefined | Variable with unused default expansion | Variable with default expansion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| source file | <pre>foo=ab</pre> | <pre>foo=a\zb</pre> | <pre>foo='a\zb'</pre> | <pre>foo="a\zb"</pre> | <pre>foo=a\nb</pre> | <pre>foo='a\nb'</pre> | <pre>foo="a\nb"</pre> | <pre>foo="a<br>b"</pre> | <pre>foo=a b</pre> | <pre>foo=a#b</pre> | <pre>foo=a #b</pre> | <pre>foo="a#b"</pre> | <pre>foo=é</pre> | <pre>foo="é"</pre> | <pre>a=b<br>foo=x$a<br></pre> | <pre>foo=x$a<br></pre> | <pre>a=b<br>foo=x$a.y<br></pre> | <pre>a=b<br>foo=x$a-y<br></pre> | <pre>a=b<br>a_y=c<br>foo=x$a_y<br></pre> | <pre>a=b<br>foo=x${a}y<br></pre> | <pre>foo=x${a}y<br></pre> | <pre>a=b<br>foo=x${a:-c}<br></pre> | <pre>foo=x${a:-c}<br></pre> |
| bash&#8209;5.0.0 | `a`&nbsp;`b` | `a`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | <pre>.env: line 1: b: command not found<br>[print_env] foo undefined<br></pre> | `a`&nbsp;`#`&nbsp;`b` | `a` | `a`&nbsp;`#`&nbsp;`b` | `é` | `é` | `x`&nbsp;`b` | `x` | `x`&nbsp;`b`&nbsp;`.`&nbsp;`y` | `x`&nbsp;`b`&nbsp;`-`&nbsp;`y` | `x`&nbsp;`c` | `x`&nbsp;`b`&nbsp;`y` | `x`&nbsp;`y` | `x`&nbsp;`b` | `x`&nbsp;`c` |
| js&#8209;dotenv&#8209;6.2.0 | `a`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a` | `a`&nbsp;`␣`&nbsp;`b` | `a`&nbsp;`#`&nbsp;`b` | `a`&nbsp;`␣`&nbsp;`#`&nbsp;`b` | `a`&nbsp;`#`&nbsp;`b` | `é` | `é` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`.`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`-`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`_`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`{`&nbsp;`a`&nbsp;`}`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`{`&nbsp;`a`&nbsp;`}`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`{`&nbsp;`a`&nbsp;`:`&nbsp;`-`&nbsp;`c`&nbsp;`}` | `x`&nbsp;`$`&nbsp;`{`&nbsp;`a`&nbsp;`:`&nbsp;`-`&nbsp;`c`&nbsp;`}` |
| python&#8209;dotenv&#8209;0.9.1 | `a`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `"`&nbsp;`a` | `a`&nbsp;`␣`&nbsp;`b` | `a`&nbsp;`#`&nbsp;`b` | `a`&nbsp;`␣`&nbsp;`#`&nbsp;`b` | `a`&nbsp;`#`&nbsp;`b` | `\`&nbsp;`x`&nbsp;`e`&nbsp;`9` | `é` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`.`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`-`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`_`&nbsp;`y` | `x`&nbsp;`b`&nbsp;`y` | `x`&nbsp;`y` | `x` | `x` |
| python&#8209;dotenv&#8209;0.10.1 | `a`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a`&nbsp;`␣`&nbsp;`b` | `a` | `a` | `a`&nbsp;`#`&nbsp;`b` | `é` | `é` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`.`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`-`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`_`&nbsp;`y` | `x`&nbsp;`b`&nbsp;`y` | `x`&nbsp;`y` | `x` | `x` |
| python&#8209;dotenv&#8209;0.12.0 | `a`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a`&nbsp;`␣`&nbsp;`b` | `a`&nbsp;`#`&nbsp;`b` | `a` | `a`&nbsp;`#`&nbsp;`b` | `é` | `é` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`.`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`-`&nbsp;`y` | `x`&nbsp;`$`&nbsp;`a`&nbsp;`_`&nbsp;`y` | `x`&nbsp;`b`&nbsp;`y` | `x`&nbsp;`y` | `x` | `x` |
| ruby&#8209;dotenv&#8209;2.6.0 | `a`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`z`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\`&nbsp;`n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a`&nbsp;`\n`&nbsp;`b` | `a`&nbsp;`␣`&nbsp;`b` | `a` | `a` | `a`&nbsp;`#`&nbsp;`b` | `é` | `é` | `x`&nbsp;`b` | `x` | `x`&nbsp;`b`&nbsp;`.`&nbsp;`y` | `x`&nbsp;`b`&nbsp;`-`&nbsp;`y` | `x`&nbsp;`c` | `x`&nbsp;`b`&nbsp;`y` | `x`&nbsp;`y` | `x`&nbsp;`b`&nbsp;`:`&nbsp;`-`&nbsp;`c`&nbsp;`}` | `x`&nbsp;`:`&nbsp;`-`&nbsp;`c`&nbsp;`}` |

