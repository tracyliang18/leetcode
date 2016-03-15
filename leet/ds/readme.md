## data structure

### 树

- 并查集

    - 集合的合并和查找
    - 主要操作是合并,和查询所属集合
    - 用链表实现集合,合并为O(1),查找为O(n)
    - 用森林来实现,每棵子树代表一个集合,合并为O(1),查找最坏情况仍然O(n),若查找时同时进行路径压缩,则查找均摊复杂度约为常数.

- 二叉堆

     - 最大堆,最小堆
     - insert O(log(n))
     - build O(n) [why](http://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity)
     - get min or max O(1)

- 线段树
    - 背景:计算n条线段总覆盖长度,如果线段不会增加或删除,则对所有端点排序即可解决 nO(logn).否则,用线段数储存线段信息,然后每次更新log(n),总复杂度仍然为nlog(n)
    - 结构:二叉树
    - 每个节点代表一个区间
    - 叶子节点为单元区间(长度为1)
    - 每个节点有一个count变量,表示覆盖节点区间这条线段的数量
    - 插入一条线段,删除一条线段的复杂度log(n)
    - 每个节点有一个测度m,表示n条线段在节点区间覆盖的长度
        - 如果count > 0, m 即为区间长度
        - 否则 m 为 左右子节点的测度和(没有子节点则为0)
    - 计算线段总覆盖长段数:
        - 每个节点有一个line变量代表区间内的线段数
        - 每个节点定义lbd,rbd,分别代表左右断点是否被覆盖.
        - 则每个节点的line可以通过孩子的line得到:

            如果 count > 0, line = 1
            如果 count == 0:
            line = lchird.line + rchild.line (- 1), 如果左孩子的rbd和右孩子的lbd同时为1则需要减一

- 树状数组(binary indexed tree)
    - 背景:一维数组,会查询子数组和,数组元素可能会改变
    - s[i]代表从0到i的数组前缀和,利用树状数组可以实现log(n)且更新某个元素的值也只需log(n)

- trie

    - 前缀树
    - trie存储着若干个单词(字典).那```set<string>```也可以做,为什么需要[trie](https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/)?
        - 可以支持更多样的查询(相同前缀,一定编辑距离内)
        - 时间复杂度为O(L),L为字符串长度,时间复杂度会比基于搜索树的set快(logn),空间复杂度会比hash table低
        - The word trie is an infix of the word “re**trie**val” because the trie can find a single word in a dictionary with only a prefix of the word.
        - 应用: 浏览器网址补全,orthographic corrector
    - [trie.cpp](trie.cpp) , [trie.py](trie.cpp)
    
