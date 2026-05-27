__all__ = [
    'Layout',
    'MindMap'
]
from typing import Generator,List,Dict
from ..nodes import Node,NodeStyle,bfs_walker,dfs_walker
from ..algorithms import tidy_tree_layout
import numpy as np
from manim.constants import *
from manim.utils.tex_templates import TexTemplateLibrary
from manim.utils.color import *
from manim.mobject.mobject import Group,Mobject
from manim.mobject.geometry.line import Line
from manim.mobject.geometry.polygram import Rectangle
from manim.mobject.types.vectorized_mobject import VMobject
from manim.mobject.text.tex_mobject import Tex

class Layout:
    """基础布局类"""
    def __init__(
        self,
        root: Node,
        direction = DOWN,
        level_spacing = 0.5,
        node_spacing = 0.5
    ):
        self.root = root
        self.level_spacing = level_spacing
        self.node_spacing = node_spacing
        if np.array_equal(direction,UP):
            self.direction = 'up'
        elif np.array_equal(direction,DOWN):
            self.direction = 'down'
        elif np.array_equal(direction,LEFT):
            self.direction = 'left'
        elif np.array_equal(direction,RIGHT):
            self.direction = 'right'
    
    def do_layout(self) -> Node:
        """执行布局计算"""
        # TODO: 采用策略模式,选择不同的布局算法,实现不同的布局,比如: 时序图布局, 鱼骨图布局等
        return tidy_tree_layout(
            self.root,
            direction = self.direction,
            level_spacing = self.level_spacing,
            node_spacing = self.node_spacing
        )
    
class NodeMobject:
    __slots__ = ['vmobject','surr_rect','connector','text']
    def __init__(
        self,
        vmobject:VMobject,
        surr_rect:Rectangle,
        connector:Line,
        text:str
    ):
        self.vmobject = vmobject
        self.surr_rect = surr_rect
        self.connector = connector
        self.text = text
    
class MindMap(Group):
    """
    思维导图类: 解析如下格式的思维导图数据,并生成对应的思维导图对象

    Example::

        mindmap = {
            'node':r'球体积',
            'text':'用于TTS讲解的文本',
            'child':[
                {
                    'node':r'公元前3世纪',
                    'child':[
                        {'node':r'阿基米德平衡法'}
                    ]
                },
                {
                    'node':r'公元3世纪',
                    'child':[
                        {'node':r'《九章算术》'},
                        {
                            'node':r'刘徽：牟合方盖',
                            'child':[
                                {'node':r'球与牟合方盖的关系'},
                                {'node':r'牟合方盖体积？'}
                            ]
                        }
                    ]
                },
            ]
        }
        mind = MindMap(mindmap)
        mind.scale_to_fit_width(12)
        self.play(FadeIn(mind))
    """
    def __init__(
        self,
        map:Dict = {},
        buff:float = 0.2,
        node_style :NodeStyle = NodeStyle(
            direction = RIGHT,
            level_spacing = 1.0,
            node_spacing = 0.5,
            node_style = [
                {'color':WHITE,'stroke_width':8},
                {'color':WHITE,'stroke_width':6},
                {'color':WHITE,'stroke_width':4}
            ],
            line_style = [
                {'color':WHITE,'stroke_width':8},
                {'color':WHITE,'stroke_width':6},
                {'color':WHITE,'stroke_width':4}
            ],
            text_style = [
                {'color':RED,'font_size':64},
                {'color':YELLOW,'font_size':56},
                {'color':GREEN,'font_size':48},
                {'color':WHITE,'font_size':36}
            ]
        )
    ):
        super().__init__()
        self.buff = buff
        self.node_style = node_style
        self.node_data_dict = {}
        self._generate_tree(Map = map)
        self.root = Layout(
            self.root,
            node_style.direction,
            node_style.level_spacing,
            node_style.node_spacing,
        ).do_layout()
        self._set_node_position(self.root)
        self._set_connectors()
        self.add(*self.get_all_mindmap())
        self.move_to(ORIGIN)

    def _generate_tree(self,root:Node = None,ID = (0,),Map = None):
        """
        递归的遍历Map: 生成树的根节点
        text: 为讲解文字，可用于合成语言
        """
        level = len(ID)
        node = self._generate_node(Mobj = Map['node'],level = level)
        node = Node(node,self.buff,**self._get_node_style(level=level))
        if root is None:
            root = node
            self.root = root
        else:
            root.add_child(node)
        node.ID = ID
        node.text = Map['text'] if 'text' in Map else None

        if 'child' in Map:
            for index,mp in enumerate(Map['child']):
                self._generate_tree(root = node,ID = (*ID,index),Map = mp)

    def _generate_node(self,Mobj,level = 1) -> Mobject:
        """生成节点"""
        if isinstance(Mobj,str):
            Mobj = Tex(
                Mobj,
                tex_template = TexTemplateLibrary.ctex,
                **self._get_tex_style(level = level)
            )
        return Mobj
    
    def _set_node_position(self,node:Node):
        pos = np.array([node.x, node.y, 0])
        node.vmobject.move_to(pos)
        node.surr_rect.move_to(pos)
        for child in node.children:
            self._set_node_position(child)
    
    def _set_connectors(self):
        """设置连接线"""
        for node in bfs_walker(self.root):
            node.connector = node.get_connector(
                direction = self.node_style.direction,
                **self._get_connector_style(level = len(node.ID))
            ) if node.parent is not None else None

            self.node_data_dict[node.ID] = NodeMobject(
                vmobject = node.vmobject,
                surr_rect = node.surr_rect,
                connector = node.connector,
                text = node.text
            )

    def _get_connector_style(self,level):
        return self.node_style.get_line_style(level = level)
    
    def _get_tex_style(self,level = 1):
        return self.node_style.get_text_style(level = level)
        
    def _get_node_style(self,level = 1):
        return self.node_style.get_node_style(level = level)
        
    def get_node_component(self,ID) -> NodeMobject:
        return self.node_data_dict.get(ID,None)

    def get_node(self,ID) -> Group:
        node = self.node_data_dict.get(ID,None)
        if node is not None:
            return Group(node.vmobject,node.surr_rect)
        return None

    def get_text(self,ID) -> str:
        node = self.node_data_dict.get(ID,None)
        if node is not None:
            return node.text
        return None
    
    def get_connector(self,ID) -> Line:
        node = self.node_data_dict.get(ID,None)
        if node is not None:
            return node.connector
        return None
    
    def get_all_mindmap(self) -> Group:
        all_mobjects = Group()
        for node in self.node_data_dict.values():
            if node.connector is not None:
                all_mobjects.add(node.vmobject,node.surr_rect,node.connector)
            else:
                all_mobjects.add(node.vmobject,node.surr_rect)
        return all_mobjects
    
    def bfs_walker(self) -> Generator:
        """广度优先遍历"""
        for node in bfs_walker(self.root):
            yield self.node_data_dict[node.ID]

    def dfs_walker(self) -> Generator:
        """深度优先遍历"""
        for node in dfs_walker(self.root):
            yield self.node_data_dict[node.ID]

    def custom_walker(self,id_list: List[tuple]) -> Generator:
        """自定义遍历"""
        for id in id_list:
            yield self.node_data_dict.get(id,None)

    def _get_origin_node(self,ID) -> Node:
        for node in dfs_walker(self.root):
            if node.ID == ID:
                return node
        return None

    def get_children(self,ID) -> Group:
        '''获取节点的子节点'''
        node = self._get_origin_node(ID)
        if node is None:
            return Group()
        return node.get_children_mobjects()
    
    def get_submindmap(self,ID) -> Group:
        '''获取以节点 ID 为根的子树'''
        node = self._get_origin_node(ID)
        mondmap = Group()
        if node is None:
            return mondmap
        for node_ in dfs_walker(node):
            if node_.connector is not None and len(node_.ID) > len(ID):
                mondmap.add(node_.vmobject,node_.surr_rect,node_.connector)
            else:
                mondmap.add(node_.vmobject,node_.surr_rect)
        return mondmap

    def get_descendants(self,ID) -> Group:
        '''获取节点的后代'''
        node = self._get_origin_node(ID)
        if node is None:
            return Group()
        return node.get_descendants_mobjects()