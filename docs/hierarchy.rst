类继承体系与模块架构
======================

继承体系
--------

.. inheritance-diagram:: manim_mindmap.nodes.node.Node
    manim_mindmap.mindmap.layout.Layout
    manim_mindmap.mindmap.layout.MindMap
    manim_mindmap.animations.animations.AbstractLayoutAnimation
    manim_mindmap.animations.animations.LayoutAnimation
    manim_mindmap.animations.animations.RemoveNode
    manim_mindmap.animations.animations.InsertNode
    manim_mindmap.animations.animations.ScaleNode
    manim_mindmap.animations.animations.AlterNode
    :parts: 1

模块架构图
----------

.. graphviz::

    digraph modules {
        rankdir=TB;
        size="10,6";
        node [shape=box, style=rounded, fontname="sans-serif"];

        subgraph cluster_nodes {
            label="nodes 模块";
            color=lightgray;
            "Node" [fillcolor=lightblue, style=filled];
            "NodeStyle" [fillcolor=lightblue, style=filled];
            "NodeSate" [fillcolor=lightblue, style=filled];
            "dfs_walker" [fillcolor=lightyellow, style=filled];
            "bfs_walker" [fillcolor=lightyellow, style=filled];
        }

        subgraph cluster_mindmap {
            label="mindmap 模块";
            color=lightgray;
            "MindMap" [fillcolor=lightgreen, style=filled];
            "Layout" [fillcolor=lightgreen, style=filled];
        }

        subgraph cluster_algorithms {
            label="algorithms 模块";
            color=lightgray;
            "tidy_tree_layout" [fillcolor=lightyellow, style=filled];
            "TidyTreeLayout" [fillcolor=lightyellow, style=filled];
        }

        subgraph cluster_animations {
            label="animations 模块";
            color=lightgray;
            "AbstractLayoutAnimation" [fillcolor=lightpink, style=filled];
            "LayoutAnimation" [fillcolor=lightpink, style=filled];
            "RemoveNode" [fillcolor=lightpink, style=filled];
            "InsertNode" [fillcolor=lightpink, style=filled];
            "ScaleNode" [fillcolor=lightpink, style=filled];
            "AlterNode" [fillcolor=lightpink, style=filled];
        }

        // MindMap uses nodes
        "MindMap" -> "Node" [style=dashed, arrowhead=none];
        "MindMap" -> "NodeStyle" [style=dashed, arrowhead=none];
        "MindMap" -> "Layout" [style=dashed, arrowhead=none];
        "MindMap" -> "bfs_walker" [style=dashed, arrowhead=none];
        "MindMap" -> "dfs_walker" [style=dashed, arrowhead=none];

        // Layout uses tidy_tree
        "Layout" -> "tidy_tree_layout" [style=dashed, arrowhead=none];

        // Animations use Layout
        "LayoutAnimation" -> "Layout" [style=dashed, arrowhead=none];
        "AbstractLayoutAnimation" -> "Layout" [style=dashed, arrowhead=none];
    }

模块说明
--------

nodes 模块
^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 类/函数
     - 说明
   * - ``Node``
     - 树节点类，存储节点坐标、父子关系、连接线等
   * - ``NodeStyle``
     - 节点样式配置，控制布局方向、间距、颜色等
   * - ``NodeSate``
     - 节点状态枚举（INSERT/REMOVE/DISPLAY/SCALE/ALTER）
   * - ``dfs_walker``
     - 深度优先遍历生成器
   * - ``bfs_walker``
     - 广度优先遍历生成器

mindmap 模块
^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 类
     - 说明
   * - ``Layout``
     - 基础布局类，使用 Tidy Tree 算法计算节点位置
   * - ``MindMap``
     - 思维导图主类，解析字典数据并生成可视化对象

algorithms 模块
^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 函数/类
     - 说明
   * - ``tidy_tree_layout``
     - Tidy Tree 布局算法函数接口
   * - ``TidyTreeLayout``
     - 非分层整洁树布局算法实现类

animations 模块
^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 类
     - 说明
   * - ``AbstractLayoutAnimation``
     - 动画基类，执行布局算法并生成动画
   * - ``LayoutAnimation``
     - 通用布局动画
   * - ``InsertNode``
     - 插入节点动画
   * - ``RemoveNode``
     - 移除节点动画
   * - ``ScaleNode``
     - 缩放节点动画
   * - ``AlterNode``
     - 替换节点内容动画

数据流图
--------

.. graphviz::

    digraph dataflow {
        rankdir=LR;
        size="12,5";
        node [shape=box, style=rounded, fontname="sans-serif"];

        "字典数据" -> "MindMap.__init__" [label="map:Dict"];
        "MindMap.__init__" -> "_generate_tree" [label="解析"];
        "_generate_tree" -> "Node 树" [label="生成"];
        "Node 树" -> "Layout.do_layout" [label="布局"];
        "Layout.do_layout" -> "tidy_tree_layout" [label="算法"];
        "tidy_tree_layout" -> "节点坐标" [label="计算"];
        "节点坐标" -> "_set_connectors" [label="设置连线"];
        "_set_connectors" -> "NodeMobject" [label="包装"];
        "NodeMobject" -> "Group (MindMap)" [label="返回"];

        {rank=same; "字典数据"; "Node 树"; "节点坐标"; "NodeMobject";}
    }

导入方式
--------

.. code-block:: python

    from manim_mindmap import MindMap, NodeStyle

    # 或者单独导入
    from manim_mindmap.nodes import Node, NodeStyle, bfs_walker, dfs_walker
    from manim_mindmap.mindmap import MindMap, Layout
    from manim_mindmap.animations import (
        LayoutAnimation,
        InsertNode,
        RemoveNode,
        ScaleNode,
        AlterNode
    )