##树
1. 数的存储可以用链表也可以用数组
2. 数组的话Arr[0]为空，最好用完全二叉树存储，没有浪费
3. 数的前中后序遍历，其实就是递推，递推公示如下
   1. 前序 PreOder(r) = print r --> PreOder(r->left) --> PreOder(r->right)
   2. 中序 inOder(r) = inOder(r->left) --> print r --> inOder(r-right)
   3. 后序 postOder(r) = postOder(r->left) --> postOder(r->right) --> print(r)

## leetcode
1. [树的遍历大集合](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/yi-tao-quan-fa-shua-diao-nge-bian-li-shu-de-wen--3/)
2. [树的递归](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/che-di-chi-tou-qian-zhong-hou-xu-di-gui-fa-di-gui-/)