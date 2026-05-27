from manim import *
from manim_mindmap import *

class Scene_Name(MovingCameraScene):
    def construct(self):
        mindmap = {
            'node':r'球体积',
            'text':'用于TTS讲解的文本',
            'child':[
                {
                    'node':r'公元前3世纪',#或者为VMobject、Mobject对象
                    'child':[
                        {
                            'node':r'阿基米德平衡法',
                        }
                    ]
                },
                {
                    'node':r'公元3世纪',
                    'child':[
                        {
                            'node':r'《九章算术》',
                        },
                        {
                            'node':r'刘徽：牟合方盖',
                            'child':[
                                {
                                    'node':r'球与牟合方盖的关系',
                                },
                                {
                                    'node':r'牟合方盖体积？',
                                }
                            ]
                        }
                    ]
                },
                {
                    'node':r'公元5世纪',
                    'child':[
                        {
                            'node':r'祖暅：开立圆术',
                        }
                    ]
                },
                {
                    'node':r'公元17世纪',
                    'child':[
                        {
                            'node':r'开普勒',
                        },
                        {
                            'node':r'卡瓦列里原理',
                        }
                    ]
                },
                {
                    'node':r'公元18世纪',
                    'child':[
                        {
                            'node':r'松永良弼：会玉术',
                        }
                    ]
                }
            ]
        }

        mind = MindMap(mindmap)
        mind.scale_to_fit_width(12)
        for node in mind.dfs_walker():
            if node.connector:
                self.play(
                    Create(node.connector),
                    run_time = 0.5
                )
            self.play(
                Create(node.surr_rect),
                Write(node.vmobject)
            )
        self.wait()

        children = mind.get_children(ID = (0,1))
        self.play(
            *[
                Wiggle(child) for child in children
            ]
        )
        self.wait()

        descendants = mind.get_descendants(ID = (0,1))
        self.play(
            *[
                Wiggle(descendant) for descendant in descendants
            ]
        )
        self.wait()

        mini_mind = mind.get_submindmap(ID = (0,1))
        self.play(
            *[
                mobj.animate(rate_func = there_and_back).set_stroke_width(20) for mobj in mini_mind if isinstance(mobj, Line)
            ]
        )
        self.wait()

        self.play(
            *[
                mobj.animate(rate_func = there_and_back).set_stroke_width(20) for mobj in mini_mind if isinstance(mobj, Rectangle)
            ]
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