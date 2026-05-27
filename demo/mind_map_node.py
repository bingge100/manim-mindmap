from manim import *
from manim_mindmap import *

class Scene_Name(MovingCameraScene):
    def construct(self):
        node_style = NodeStyle(direction=DOWN)

        root = Node(Tex(r'圆周率').to_edge(UP))
        A = Node(Tex(r'圆的面积'))
        B = Node(Tex(r'圆的周长'))
        C = Node(Tex(r'球的\\体积'))

        D = Node(Tex(r'圆的面积公式'))
        E = Node(Tex(r'圆的周长公式'))

        F = Node(Tex(r'球的表面积'))

        G = Node(Tex(r'正方形'))
        H = Node(Tex(r'长方形'))
        self.play(
            InsertNode(self,{root:[A,B,C],A:[D,E],B:[F],C:[G,H]},node_style),
            run_time = 3
        )
        self.wait()

        self.play(
            AlterNode(self,{root:Tex(r'圆周率$\pi$')},node_style),
        )
        self.wait()

        self.play(
            ScaleNode(self,{C:1.2},node_style),
        )

        self.play(
            RemoveNode(self,B,node_style),
        )
        self.wait()

        self.play(
            InsertNode(self,{root:[B]},node_style),
        )
        self.wait()

        self.play(
            RemoveNode(self,root,node_style),
        )
        self.wait()

with tempconfig(
    {
        "quality": "low_quality", # low_quality   medium_quality   high_quality
        "preview": True,
        "tex_template":TexTemplateLibrary.ctex,
        # "renderer": "opengl"
    }
):
    Scene_Name().render()