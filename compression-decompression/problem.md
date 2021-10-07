# The Challenge

In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

```
The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc

```

### Rules

1. Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

2. One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

3. Characters allowed as input include digits, small English letters and brackets [].

4. Digits are only to represent amount of repetitions.

5. Letters are just letters.

6. Brackets are only part of syntax of writing repeated substring.

7. Input is always valid, so no need to check its validity.

---

## Learning objectives

This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.

---

## Solution

This approach will work for all kind of inputs mentioned above in the **Rules** section

There are three lists, one for storing the position of opening bracket **bracket_index_stack**, one for storing the count for which string should be repeated **number_stack** and one for storing the start position from where string should be replaced with decompressed string **replace_index_stack**.

These lists work like **STACK**, first in last out principle. On opening of bracket, relivent positions/indexes are added in the stacks accordingly and on closing of brackets, base string is updated with decompressed substring and index of `for loop` is set to next position in the string.

---

### For more help, You can check the code OR

[Visit Google Tech Guide page](https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#)
