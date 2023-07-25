// 定义二叉树的节点类
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode(int x) {
    val = x;
  }
}

// 定义一个方法，返回二叉树的最小深度
public int minDepth(TreeNode root) {
  // 如果根节点为空，返回0
  if (root == null) {
    return 0;
  }
  // 如果根节点没有左右子节点，返回1
  if (root.left == null && root.right == null) {
    return 1;
  }
  // 初始化最小深度为最大整数值
  int min = Integer.MAX_VALUE;
  // 如果根节点有左子节点，递归计算左子树的最小深度，并更新最小值
  if (root.left != null) {
    min = Math.min(min, minDepth(root.left));
  }
  // 如果根节点有右子节点，递归计算右子树的最小深度，并更新最小值
  if (root.right != null) {
    min = Math.min(min, minDepth(root.right));
  }
  // 返回最小深度加上根节点本身的深度1
  return min + 1;
}
