Title: Tail Recursion with F#
Author: Michael Jacobsen
Date: 2008-10-29
Updated: 2012-11-18
Tags: programming, fsharp

The familiar for loop featured in most if not all impertive langagues
is not part of most functional languages if any because it has the
mutable loop index. The standard way of looping in F# is to use
recursion.

In the solution to Project Euler problem 7 I have the following
function

<pre class="prettyprint lang-ml">
let rec findprime primes test =
    if isprime primes test then test
    else findprime primes (test+2)
</pre>

Notice that the recursive call is placed as the very last operation in
the function and it is therefore a tail call. Using the tool <a
href="">Reflector</a> it is possible to obtain a C# version of the
program:

<pre class="prettyprint">
public static int findprime(FSharpList<int> primes, int test)
{
    while (!isprime(primes, test))
    {
        test += 2;
        primes = primes;
    }
    return test;
}
</pre>

We see that the compiler has transformed the recursive function into a
function without recursion.
