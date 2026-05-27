__all__ = [
    'Node',
    'NodeSate',
    'NodeStyle',
    'dfs_walker',
    'bfs_walker'
]
from enum import Enum
from collections import deque
from typing import Generator,List,Dict
from manim.mobject.mobject import Group
from manim.mobject.types.vectorized_mobject import VMobject,VGroup
from manim.mobject.geometry.line import Line
from manim.mobject.geometry.polygram import Rectangle
from manim.constants import LEFT, RIGHT, UP, DOWN
from manim.utils.color import *
import numpy as np
    
class NodeSate(Enum):
    """节点状态"""
    INSERT = 0  # 新插入
    REMOVE = 1  # 待移除
    DISPLAY = 2  # 已显示
    SCALE = 3  # 待放大
    ALTER = 4  # 替换节点中的内容

class NodeStyle:
    '''整体布局参数,以及节点样式字典列表,按节点层级索引'''
    def __init__(
        self,
        direction = RIGHT,
        level_spacing = 0.5,
        node_spacing = 0.5,
        node_style:List[Dict] = [
            {'color':RED, 'stroke_width':8},
            {'color':BLUE, 'stroke_width':6},
            {'color':YELLOW, 'stroke_width':4},
            {'color':GREEN, 'stroke_width':4}
        ],
        line_style:List[Dict] = [
            {'color':RED, 'stroke_width':8},
            {'color':BLUE, 'stroke_width':6},
            {'color':YELLOW, 'stroke_width':4},
            {'color':GREEN, 'stroke_width':4}
        ],
        text_style = [
            {'color':RED,'font_size':64},
            {'color':YELLOW,'font_size':56},
            {'color':GREEN,'font_size':48},
            {'color':WHITE,'font_size':36}
        ]
    ):
        if not any(np.array_equal(direction, d) for d in [UP, DOWN, LEFT, RIGHT]):
            raise ValueError(f'direction must be one of {LEFT,RIGHT,UP,DOWN}')
        self.direction = direction
        self.level_spacing = level_spacing
        self.node_spacing = node_spacing
        
        self.node_num = len(node_style)
        if self.node_num:
            self.node_style = node_style
        else:
            self.node_style = [{'color':YELLOW, 'stroke_width':4}]
            self.node_num = 1

        self.line_num = len(line_style)
        if self.line_num:
            self.line_style = line_style
        else:
            self.line_style = [{'color':YELLOW, 'stroke_width':4}]
            self.line_num = 1

        self.text_num = len(text_style)
        if self.text_num: 
            self.text_style = text_style
        else:
            self.text_style = [{'color':YELLOW, 'font_size':36}]
            self.text_num = 1

    def get_node_style(self,level:int) -> Dict:
        if level < self.node_num:
            return self.node_style[level]
        return self.node_style[-1]
    
    def get_line_style(self,level:int) -> Dict:
        if level < self.line_num:
            return self.line_style[level]
        return self.line_style[-1]
    
    def get_text_style(self,level:int) -> Dict:
        if level < self.text_num:
            return self.text_style[level]
        return self.text_style[-1]

def dfs_walker(root: 'Node') -> Generator:
    """深度优先,前序遍历:后进先出,用栈"""
    if not root:
        return []
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        for child in reversed(node.children):
            stack.append(child)

def bfs_walker(root: 'Node') -> Generator:
    """广度优先,层序遍历:先进先出,用队列"""
    if not root:
        return []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        yield node
        for child in node.children:
            queue.append(child)

class Node:
    """树节点类"""
    direction = RIGHT
    def __init__(
        self,
        vmobject:VMobject = None,
        buff: float = 0.2,
        **kwargs
    ):
        self.vmobject = vmobject
        self.height = self.vmobject.height + 2*buff
        self.width = self.vmobject.width + 2*buff
        self.buff = buff
        self.surr_rect = Rectangle(
            width = self.width,
            height = self.height,
            **kwargs
        )
        self.x = 0
        self.y = 0
        self.level = 0
        self.parent = None
        self.neighbor = None  # 邻居节点
        self.children = []
        self.node_state = NodeSate.INSERT  # 节点状态
    
    def scale(self, scale_factor: float):
        """缩放节点"""
        self.node_state = NodeSate.SCALE
        self.scale_factor = scale_factor
        self.width *= scale_factor
        self.height *= scale_factor
    
    def add_child(self, child: 'Node'):
        """添加子节点"""
        if self.children:
            child.neighbor = self.children[-1]
            child.node_state = NodeSate.INSERT
        self.children.append(child)
        child.parent = self

    def remove_child(self, child: 'Node'):
        """删除子节点"""
        if child not in self.children:
            raise ValueError(f"Node {child} is not a child of {self}")
        child.node_state = NodeSate.REMOVE

    def alter_content(self, vmobject: VMobject):
        """替换节点内容"""
        self.node_state = NodeSate.ALTER
        self.alter_vmobject = vmobject
        self.width = self.alter_vmobject.width + 2*self.buff
        self.height = self.alter_vmobject.height + 2*self.buff

    def get_connector(self, direction = RIGHT,**kwargs) -> Line:
        if np.array_equal(direction,UP):
            start,end = self.parent.surr_rect.get_top(),self.surr_rect.get_bottom()
        elif np.array_equal(direction,DOWN):
            start,end = self.parent.surr_rect.get_bottom(),self.surr_rect.get_top()
        elif np.array_equal(direction,LEFT):
            start,end = self.parent.surr_rect.get_left(),self.surr_rect.get_right()
        else:
            start,end = self.parent.surr_rect.get_right(),self.surr_rect.get_left()
        vec = np.dot(end - start,direction) * direction*0.5
        return Line(start,start+vec,**kwargs).add_line_to(end-vec).add_line_to(end)
    
    def set_connector(self,direction = RIGHT,**kwargs):
        """设置连接线"""
        if self.parent is not None:
            if not hasattr(self,'connector'):
                self.direction = direction
                self.connector = self.get_connector(direction,**kwargs)
                self.connector.add_updater(lambda m: m.become(self.get_connector(direction,**kwargs)))
    
    def change_connector(self,direction = RIGHT,**kwargs):
        """改变连接线"""
        if hasattr(self,'connector') and not np.array_equal(self.direction,direction):
            self.connector.remove_updater(*self.connector.get_updaters())
            self.direction = direction
            self.connector.add_updater(lambda m: m.become(self.get_connector(direction,**kwargs)))

    def get_node_and_line_without_updater(self) -> Group:
        node_mobj = Group(self.surr_rect,self.vmobject)
        if hasattr(self,'connector'):
            self.connector.remove_updater(*self.connector.get_updaters())
            node_mobj.add(self.connector)
            del self.connector
        return node_mobj
    
    def get_children(self) -> List['Node']:
        """获取所有子节点"""
        return self.children
    
    def get_descendants(self) -> List['Node']:
        """获取所有子孙节点"""
        def descendants_of_node(node: Node,descendants: list[Node] = []) -> list[Node]:
            if node.children:
                descendants.extend(node.children)
            for node_ in node.children:
                descendants_of_node(node_,descendants)
            return descendants
        return descendants_of_node(self)
    
    def get_children_mobjects(self) -> Group:
        """获取所有子节点对象"""
        group = Group()
        for node in self.children:
            group.add(node.vmobject,node.surr_rect)
        return group
    
    def get_descendants_mobjects(self) -> Group:
        """获取所有子孙节点对象"""
        def descendants_mobjects_of_node(node: Node,descendants: Group = Group()) -> Group:
            for node_ in node.children:
                descendants.add(node_.vmobject,node_.surr_rect)
                descendants_mobjects_of_node(node_,descendants)
            return descendants
        return descendants_mobjects_of_node(self)
    
    def get_root(self) -> 'Node':
        """获取根节点"""
        if self.parent is None:
            return self
        return self.parent.get_root()