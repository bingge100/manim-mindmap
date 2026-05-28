动画模块 (manim_mindmap.animations)
====================================

该模块提供了思维导图的各种动画类，用于节点的插入、删除、缩放和替换等操作。

动画基类
--------

.. autoclass:: manim_mindmap.animations.animations.AbstractLayoutAnimation
   :members:
   :show-inheritance:

布局动画
--------

.. autoclass:: manim_mindmap.animations.animations.LayoutAnimation
   :members:
   :show-inheritance:

插入节点
--------

.. autoclass:: manim_mindmap.animations.animations.InsertNode
   :members:
   :show-inheritance:

删除节点
--------

.. autoclass:: manim_mindmap.animations.animations.RemoveNode
   :members:
   :show-inheritance:

缩放节点
--------

.. autoclass:: manim_mindmap.animations.animations.ScaleNode
   :members:
   :show-inheritance:

替换节点
--------

.. autoclass:: manim_mindmap.animations.animations.AlterNode
   :members:
   :show-inheritance:

辅助函数
--------

.. autofunction:: manim_mindmap.animations.animations.animate_of_layout

.. autofunction:: manim_mindmap.animations.animations.fadeout_of_subtrees
