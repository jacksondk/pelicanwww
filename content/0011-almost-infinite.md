Title: Almost Infinite Sequences in F#
Author: Michael Jacobsen
Date: 2008-09-03
Tags: programming, tips

F# has a nice syntax for creating sequences where elements are created
on demand. For instance

    let asequence1 = seq { 1 .. 20 };;

creates a sequence of the numbers 1 to 20. No supprise
here. We are also able to include steps, that is,

    let asequence2 = seq { 2 .. 2 .. 20 };;

where we only take even numbers. However, in several of the Euler
problems we do not have an upper limit on the search space. With an
"recursive sequence definition" we are able to make this "infinite
sequence".

    let rec inf_seq n = seq { yield n
                              yield! inf_seq (n+1) }

Now we do not have to consider what upper limit to choose. However,
we have an implicit upper bound as the representation of an integer
yields an upper bound of 2147483647.

If we exchange "1" with "1I", that is, one as a big integer we get a
sequence limited by the capacity of bigint whatever that is.
