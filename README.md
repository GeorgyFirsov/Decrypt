# Decrypt

> 👉 **Note**: it is just an experiment to improve my skills in machine learning and data science. It is not an accurate method for decryption. 
I just want to find out various regularities in words encrypted with different methods and research them.

### Motivation

It is hard to decrypt a message with unknown encryption method. Main reason for this fact is following: encryption methods are developed in such 
a way to make you not to find out original message easily without a knowledge about encryption method used for this concrete text.

I think it is possible to make some dictionary with all the words encrypted with some method (for instance, with Caesar cipher). But having such 
dictionaries for almost all encryption methods means having A LOT OF SPACE on your HDD. In our time, I think, it is impossible to have such 
amount of disk storage.

So... This project is my attempt to avoid problems mentioned above and apply machine learning to solve this task.

### Desciption

We have a kind of classification task: random encrypted word should be a member of one of 6 different classes, destinguished by 
encryption method:
- Caesar cipher with shift 3
- Caesar cipher with shift 4
- Caesar cipher with shift 5
- Affine cipher with multiplier 3 and shift 4
- Affine cipher with multiplier 5 and shift 2
- Afifne cipher with multiplier 9 and shift 11

> 👉 **Note**: affine cipher uses following formula to calculate letter index: `y = (a*x + b) mod m`, where a is a multiplier, b is a shift and m 
is a length of original alphabet. Caesar cipher is a "subset" of affine with `a = 1`, formula of encrypted letter's index is following: 
`y = (x + b) mod m`.

### Brief research conclusion

Classification based on some almost unique numbers for each word is impossible. Explanation: good hash functions for close arguments should give 
values, which are far away from each other on number line. It is a reason why all encrypted words are completely mixed in space with their hash 
values as a basis.

What about classification based on vectorization of words. Here we represent words as 26-dimensional vectors. For basis we use separate letters 
(for more information look to full research results). It is possible, because in general encrypted sets don't intersect strongly. So... It is a 
reason why you can successfully build build your own classifier based on vectorized words.

#### Credits

- List of english words was taken from here: https://github.com/dwyl/english-words
