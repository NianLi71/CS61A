## hw03
##### How to run
Run with
```
python3 ok
```
or 
```
python3 ok -v
```
For detail check [using-ok](https://inst.eecs.berkeley.edu/~cs61a/fa21/articles/using-ok/)

### Links
https://inst.eecs.berkeley.edu/~cs61a/fa21/hw/hw03/
http://composingprograms.com/pages/17-recursive-functions.html

### Q1: Num eights


### Q2: Ping-pong
* 题目要求用递归实现，先通过自己的想法实现了一版在recursion_v1
* 之后用while 做递推方式实现了一版while_v1
* 在实现while版本后，看题目Hint:
  *Hint: If you're stuck, first try implementing pingpong using assignment statements and a while statement. Then, to convert this into a recursive solution, write a helper function that has a parameter for each variable that changes values in the body of the while loop.*
  把while_v1中变化的变量i, pp, delta放入一个helper function f中，通过递归的方式update这些变量值，用递归的方式实现递推

### Q3: Missing Digits
* **在Python中，利用helper function来辅助实现递归是一个常用的pattern**, 在做leetcode时也经常使用，这里Q2 Q3都用到了
* 使用helper function可以自由定义递归函数的signature，而不会局限于入口函数的参数个数限制
Q4 Hint中也提到:
**If you need to keep track of more than one value across recursive calls, consider writing a helper function.**

run:
```sh
python3 ok -q missing_digits
```

### Q4: Count coins
作业提示可以参考
http://composingprograms.com/pages/17-recursive-functions.html#example-partitions
在实现递归的过程中，发现有点像动态规划的感觉了，不过确实动态规划可以用递归实现

## Just for fun Questions
这一部分没做，先做后面的作业，有时间在回来做