思维导图模块 (manim_mindmap.mindmap)
=====================================

该模块定义了思维导图的核心类：布局类和思维导图主类。

类继承关系
----------

.. inheritance-diagram:: manim_mindmap.mindmap.layout.MindMap manim_mindmap.mindmap.layout.Layout
   :parts: 1

模块架构
--------

.. graphviz::

   digraph mindmap_arch {
      rankdir=LR;
      node [shape=box, style=rounded,filled, fillcolor="#f8f8f8", fontsize=11];
      "MindMap" -> "Layout" [label=use];
      "MindMap" -> "NodeStyle" [label=config];
      "Layout" -> "tidy_tree_layout" [label=call];
      "tidy_tree_layout" -> "TidyTreeLayout" [label=impl];
   }

布局类
------

.. autoclass:: manim_mindmap.mindmap.layout.Layout
   :members:
   :show-inheritance:

思维导图类
----------

.. autoclass:: manim_mindmap.mindmap.layout.MindMap
   :members:
   :show-inheritance:

节点 Mobject
------------

.. autoclass:: manim_mindmap.mindmap.layout.NodeMobject
   :members:
