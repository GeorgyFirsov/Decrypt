# Results of my research

[intersections]: ./img/intersections.png
[classes]: ./img/classes.png

## Table of contents

- [Introduction](#Introduction)
- [First look](#First-look)
- [Hypotheses. Proofs and confutations](#Hypotheses-proofs-and-confutations)
 - [Numbers](#Numbers)
 - [Vectors](#Vectors)
- [Conclusion](#Conclusion)
- [Further research](#Further-research)

## Introduction

This research's topic is encryption. More precisely - classification of encryption methods. I used 2 algorithms: caesar and affine ciphers, because 
they are simple, they work (relatively, but it is enough for research) and they give other "words" as an encryption. Why these reasons were 
important:

- Simple algorithms. If I would make research about modern, strong and developed algorithms of encryption, probably it will be impossible, 
because of impossibility to check results.
- Working algorithms. Research of algorithms, which are not methods of encryption at all makes no sense. Caesar and affine ciphers are real 
algorithms and it is a reason to investigate them.
- Algorithms should give "word" on their output. It is important for checking answers.

## First look

So, I've told you about reasons to choose caesar and affine ciphers, let's focus on their properties.

As soon as we have classification task, we need to divide encrypted words into several groups. I chosen 6: caesar_3, caesar_4, caesar_5, 
affine_3_4, affine_5_2, affine_9_11. Designation `caesar_a` means that to encrypt these words I used caesar cipher with shifted by `a` letters 
alphabet (formula `y = (x + a) mod m`); `affine_a_b` means that we use formula `y = (a*x + b) mod m` to calculate new index of letter, where `m` 
is a length of our alphabet. As you can see, if we put `a = 1` in affine formula, we get caesar cipher.

All words are encrypted by these algorithms. It is important to know, how different are encrypted words. To find out this information I calculated 
all possible intersections and drawn two graphs:

![intersections][]

On the first graph we can see, that there are 2 intersections with relatively high cardinality: 5th and 13th (caesar_3 and affine_9_11; affine_3_4 
and affine_5_2) and 6 "weak". It means, that some methods are distinguished from each other easier than other ones. But all the 
intersections have really small cardiality in comparison to cardinality of set with all words (~2800 against ~420000). It means, that it is 
possible to classify somehow our algorithms.
The second graph is another representation of this situation: the more yellow the picture is, the larger cardinality the intersection has. Marked 
above maximums and minimums are higlighted with colored triangles.

The main idea of our first look is that we have possibility to classify encrypted words relatively accurate.

## Hypotheses. Proofs and confutations

I consider two hypotheses about way of classification:
- We can calculate some almost unique numbers for each encrypted word
- We can vectorize word

### Numbers

Let's focus on number calculation. I chosen Crc32 algorithm and the custom one, which is calculated by following code:
```python
result = 0
for index, letter in enumerate(word):
    result += letter * (index + 1) ** 2
```

Actually, I got bad results - all classes of words were mixed with each other and there is no possibility to classify them:

![classes][]

It has a clear reason: hash algorithms for close objects should give extremely different results. We can see this fact on the graph above. So, 
number calculation was bad idea, I need some function `f`, which gives relatively close answers for close arguments.

### Vectors

This function is a vector! Let's consider 26-dimensional vector space with this basis:
```
a = (1, 0, 0, ..., 0, 0)

b = (0, 1, 0, ..., 0, 0)

          . . .

z = (0, 0, 0, ..., 0, 1)
```

Each word we will encode like this: 'abczb' = (1, 2, 1, 0, ..., 0, 1). Actually, it causes some problems: 'mean' = 'name', but it doesn't matter 
at all, just because our algorithm should *classify* words - not *decode*.

The way I built basis is not quite effective (it has a name: "One Hot Encoding"), but it is simple and understandable and it's easy to encode 
words in such a way.

The main argument for such vectorization is, that letters have weak dependency on each other (they have, but we can ignore this fact).

For classification I use mixed algorithm: KNN (we have vectors or points in 26-dimensional space, so we can look on the distance between them) 
and Naive Bayes (all features are "independent"). Model learned on 18000 words (this is small set) and gives about 20% right answers on ***all*** 
words, but it is actually quite accurate on small sets (with less than 200 words).

## Conclusion

I proved, that it is possible to classify encrypted words by their encryption method. It is possible, because algorithms give different words as an 
output. Sets of encrypted words have "weak" intersections relative to cardinality of a set of all words. If we represent words as vectors, we can 
see, that they can be divided into some classes. Low accuracy of a model in this research caused by small train set and smooth bounds of classes, 
which we want to distinguish.

## Further research

It is not the end of my research, it is just a milestone. I'll continue to build accurate classifier and now I look to the neural networks, but I 
need to get some knowledge about them to resume my investigations. Also, I'm on the way to some mathematical research near this topic.

And as I said: it is not a conclusion at all!
