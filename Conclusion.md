# Results of my research

[intersections]: ./img/intersections.png
[classes]: ./img/classes.png

This research's topic is encryption. More precisely - classification of encryption methods. I used 2 algorithms: caesar and affine ciphers, because 
they are simple, they work (relatively, but it is enough for research) and they give other "words" as an encryption. Why these reasons were 
important:

- Simple algorithms. If I would make research about modern, strong and developed algorithms of encryption, probably it will be impossible, 
because of impossibility to check results.
- Working algorithms. Research of algorithms, which are not methods of encryption at all makes no sense. Caesar and affine ciphers are real 
algorithms and it is a reason to investigate them.
- Algorithms should give "word" on their output. It is important for checking answers.

So, I've told you about reasons to choose caesar and affine ciphers, let's focus on their properties.

As soon as we have classification task, we need to divide encrypted words into several groups. I chosen 6: caesar_3, caesar_4, caesar_5, 
affine_3_4, affine_5_2, affine_9_11. Designation `caesar_a` means that to encrypt these words I used caesar cipher with shifted by `a` letters 
alphabet (formula `y = (x + a) mod m`); 'affine_a_b' means that we use formula `y = (a*x + b) mod m` to calculate new index of letter, where `m` 
is a length of our alphabet. As you can see, if we put `a = 1` in affine formula, we get caesar cipher.

All words are encrypted by these algorithms. It is important to know, how different are encrypted words. To find out this information I calculated 
all possible intersections and drawn two graphs:

![intersections][]

On the first graph we can see, that there are 2 intersections with relatively high cardinality: 5th and 13th (caesar_3 and affine_9_11; affine_3_4 
and affine_5_2) and 6 "weak" intersections. It means, that some methods are distinguished from each other easier than other ones. But all the 
intersections have really small cardiality in comparison to cardinality of set with all words (~2800 against ~420000). It means, that it is 
possible to classify somehow our algorithms.
