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

        root.add_child(A)
        root.add_child(B)
        root.add_child(C)

        B.add_child(F)

        C.add_child(D)
        C.add_child(E)
        
        self.play(
            LayoutAnimation(self,root,node_style)
        )
        self.wait()

        G = Node(Tex(r'正方形'))
        H = Node(Tex(r'长方形'))

        C.add_child(G)
        F.add_child(H)

        self.play(
            LayoutAnimation(self,root,node_style)
        )
        self.wait()

        F.scale(1.5)

        self.play(
            LayoutAnimation(self,root,node_style)
        )
        self.wait()

        C.remove_child(G)
        root.remove_child(C)
        
        self.play(
            LayoutAnimation(self,root,node_style)
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