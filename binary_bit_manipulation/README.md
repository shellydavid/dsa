
# Binary Conversions & Bit Manipulation

![img](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.cpu-design.at%2Fwp-content%2Fuploads%2F2015%2F11%2FBase2.png&f=1&nofb=1&ipt=98196605e90d5ca8d9f888137b6177db5ca3d5fe9cfe5098f6a5228f3194041b)


## Converting Decimal -> Binary

1. Divide by 2 continuously and record remainders
2. Write remainders in reverse order

![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.geeksforgeeks.org%2Fwp-content%2Fuploads%2F20230731110443%2FJava-Program-for-Decimal-to-Binary-Conversion-300.png&f=1&nofb=1&ipt=57aabe38c1792358fc7d1c04c92cb0c6e973409d3f52e17d9aca7cf3d06a84bc)


## Bit Manipulation
1. Bitwise AND - `&`
2. Bitwise OR - `|`
3. Bitwise XOR - `^` (true if values are different, false if same)
4. Bitwise NOT - `~`
5. Left shift - `<<`  (multiples by power of 2)
6. Right shift - `>>`  (divides by power of 2)
   - Logical (always pads with 0's)
   - Arithmetic/Signed shift (keeps sign of original number)
![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.AM9zIe5ieqt2ZiJEjxU7yQHaCa%3Fpid%3DApi%26ucfimg%3D1&f=1&ipt=4227fcb4e1a067ede7bcd9743707660f60ea64b48bd2a946ccf51c300d2e7c16&ipo=images)


## Representing Negative Numbers in Binary
1. Signed Bit
2. One's Complement
3. **Two's Complement**

Two's Complement is the standard way to represent signed numbers in binary, since it addresses drawbacks of the first two methods.

### Signed Bit
---
Signed integers reserve the MSB (left-most) to indicate the sign (0 positive & 1 negative)

This reduces the magnitude of digits it can represent, compared to an unsigned integer with the same number of bits

Ex: For a 32 bit number:
- Unsigned: 2<sup>32</sup>
- Signed: -2<sup>31</sup> to 2<sup>31</sup>−1

#### Signed Bit Representation Drawbacks:
1. There are two representations of zero `0000` +0 and `1000` -0, which introduces problems for digital circuits
2. Binary arithmetic doesn't produce the expected values
3. Negative values are not extendable if you want to increase bit size
   - Positive numbers can simply be padded with 0s
   - Negative numbers have to have just the magnitude padded with 0s and the sign bit copied in order to still represent the correct value. This is not easily extendable on the digital circuit level.


### Complement of a Number
---
A complement of a number is a value that, when added to it, brings the number to the next power of the base system (ex: from 1s place to 10s place, or 10s place to 100s place). 

In a base10 system, 10's complement of 2 = 10-2 -> 8
   - Adding 8 to 2 brings the result from 1s place to 10s place

9's complement is a similar idea, but it would be one value short, so you can add 1
- 9's complement of 2 = 9-2 = 7
   - 7+2 = 9, but +1 brings you to next highest power of 10


### One's Complement
---
One's Complement can be achieved by simply inverting the bits

However:
- It still has two representations of 0
- Binary arithmetic works, but requires workarounds in certain cases 

### Two's Complement
---
Two's Complement addresses all the drawbacks:
1. There is one representation for 0
2. Arithmetic works as expected
3. Negative values are extendable by simply padding with 1s
4. Digital circuits are simplified

To convert an integer to its TC form or revert from TC form:
- Negate bits
- Add 1

If the TC form had a 1 in the sign bit, the number should be interpreted as negative
