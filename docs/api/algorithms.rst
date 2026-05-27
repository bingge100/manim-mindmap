算法模块 (manim_mindmap.algorithms)
====================================

该模块实现了非分层整洁树布局算法（Tidy Tree Layout），用于计算树形结构的节点位置。

算法参考：*Improving Walker's Algorithm to Run in Linear Time*

布局接口
--------

.. autofunction:: manim_mindmap.algorithms.tidy_tree.tidy_tree_layout

布局算法类
----------

.. autoclass:: manim_mindmap.algorithms.tidy_tree.TidyTreeLayout
   :members:
   :show-inheritance:

数据结构
--------

.. autoclass:: manim_mindmap.algorithms.tidy_tree.WrappedTree
   :members:

.. autoclass:: manim_mindmap.algorithms.tidy_tree.IYLNode
   :members:
