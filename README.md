# Python-Switch-Case
I really miss switch case so I put one together that is closer to JavaScript.
The importance of code is that it's readable to humans.
I live for switch case so I wanted one in Python.

As Paul Graham says in his Lisp book to write code in a programming language
we have to think in the programming language. I totally agree.

Each programming language has a completely different design philosophy and
unique rules and syntax, and is strongly influenced by the thinking
of the language designer and the languages that it's evolved and morphed from.

I'm accustomed to using switch case frequently and the design
that I made for switch case is strongly influenced from C and JavaScript but
is bound within the philosophy of a Pythonic look and feel so it's clean and
fast to write. 

My guiding light was the importance of creating the identical behavior
that is expected of a user that is familiar with switch cases so there are
no blunders and no bugs that result from using the switch case design. And
the main purpose was to make the switch case reflect the Pythonic look and
feel of cleanness and elegance to live up to the expectations of Guido van Rossum
even though he did a deep <a href=https://www.python.org/dev/peps/pep-3103/> analysis</a> with inputs on whether to add a switch case
to Python though he ultimately decided that if, elif, else were sufficient. So 
though ifs alone work I used his philosophy of design retaining if, elif, else.

The switch case has "switch", "case", "break", "fallthru" but most importantly
behaves exactly how a "real" switch case does in other languages including
JavaScript, C, C++. Most importantly it does retain use of ==  for matching rather than
using a case("word") look which I considered initially; though I may add that option soon.

