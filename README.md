# CS3310-Assignment3 - Time Huffman Codes
Due: 11/4/24 @11:59 PM

# Problem Specifications
This assignment requires you to write a program to implement the Huffman Codes algorithm. You can use the programming language of your choice (Python, Java, or C++). You will determine Huffman codes using the English alphabet and frequencies provided in Canvas. They are provided here:

Letter | Frequency | Letter | Frequency
A      | 77        | N      | 67
B      | 17        | O      | 67
C      | 32        | P      | 20
D      | 42        | Q      | 5
E      | 120       | R      | 59
F      | 24        | S      | 67
G      | 17        | T      | 85
H      | 50        | U      | 37
I      | 76        | V      | 12
J      | 4         | W      | 22
K      | 7         | X      | 4
L      | 42        | Y      | 22
M      | 24        | Z      | 2

You will need to use a min heap for this assignment. DO NOT use data structures inherent to the programming language you choose. Develop the min heap yourself. We have discussed the code for min heaps in class. You will construct the Huffman tree, first. And, then use the tree to produce the codes using 0s and 1s. Your program output should look like this:

Letter Frequency   Code Length Freq X Len
------ --------- ------ ------ ---------- 
A      77          1101 4      308
B      17        111000 6      102
C      32         10110 5      160

The last line of output should be the sum of the last column as below: The weighted minimum path length is: ????

The only requirements for this assignment are:
1) the program works
2) the min heap was developed instead of using built-in data structures
3) good programming practices and techniques are used
4) the output is sorted in alphabetical order

Also, please document your code to earn all possible points.
Please submit your code in a .zip file to the Assignment 3 dropbox in elearning