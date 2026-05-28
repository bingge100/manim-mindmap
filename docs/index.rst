.. manim-mindmap documentation master file

manim-mindmap 文档
===================

``manim-mindmap`` 是一个基于 Manim 的思维导图插件，用于在 Manim 动画中创建和操作思维导图。

.. toctree::
   :maxdepth: 2
   :caption: 目录

   api/index


快速开始
=========

安装
----

.. code-block:: bash

   pip install manim-mindmap


基本用法
--------

使用字典定义思维导图结构，然后创建 ``MindMap`` 对象：

.. code-block:: python

   from manim_mindmap import MindMap, NodeStyle

   mindmap_data = {
       'node': r'根节点',
       'child': [
           {'node': r'子节点1'},
           {'node': r'子节点2', 'child': [
               {'node': r'孙节点1'},
           ]},
       ]
   }

   mind = MindMap(mindmap_data)


核心概念
---------

- **Node**: 树节点类，表示思维导图中的一个节点
- **NodeStyle**: 节点样式配置，控制布局方向、间距、颜色等
- **MindMap**: 思维导图主类，解析字典数据并生成可视化对象
- **Layout**: 布局类，使用 Tidy Tree 算法计算节点位置
- **动画类**: ``LayoutAnimation``, ``InsertNode``, ``RemoveNode``, ``ScaleNode``, ``AlterNode``

整体架构
---------

.. graphviz::

   digraph overview {
      rankdir=TB;
      node [shape=box];
      MindMap -> NodeStyle;
      MindMap -> Layout;
      Layout -> TidyTreeLayout;
      TidyTreeLayout -> WrappedTree;
      MindMap -> Node;
      InsertNode -> Node;
      RemoveNode -> Node;
      ScaleNode -> Node;
      AlterNode -> Node;
   }


索引
=====

* :ref:`genindex`
* :ref:`modindex`
