import sys
import os

sys.path.insert(0, os.path.abspath('../src'))

project = 'manim-mindmap'
copyright = '2026, jj-math'
author = 'jj-math'

version = '0.1.0'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.extlinks',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

autosummary_generate = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'manim': ('https://docs.manim.community/en/stable', None),
}

source_suffix = '.rst'
master_doc = 'index'

language = 'zh_CN'

napoleon_google_docstring = True
napoleon_numpy_docstring = True

graphviz_output_format = 'svg'

graphviz_dot_args = [
    '-Nfontname="Microsoft YaHei,SimHei,Arial,sans-serif"',
    '-Efontname="Microsoft YaHei,SimHei,Arial,sans-serif"',
    '-Gfontname="Microsoft YaHei,SimHei,Arial,sans-serif"',
    '-Gdpi=96',
]

inheritance_graph_attrs = {
    'rankdir': 'TB',
    'size': '"12,8"',
    'dpi': '96',
    'bgcolor': 'transparent',
    'nodesep': '0.8',
    'ranksep': '0.6',
    'fontname': '"Microsoft YaHei,SimHei,Arial,sans-serif"',
    'concentrate': True,
    'splines': 'ortho',
}

inheritance_node_attrs = {
    'fontsize': '11',
    'fontname': '"Microsoft YaHei,SimHei,Arial,sans-serif"',
    'shape': 'box',
    'style': '"rounded,filled"',
    'fillcolor': '"#e8f4f8"',
    'color': '"#4a90a4"',
    'penwidth': '1.5',
    'margin': '"0.2,0.1"',
    'width': '0.05',
    'height': '0.05',
}

inheritance_edge_attrs = {
    'color': '"#6c8ebf"',
    'penwidth': '1.0',
    'arrowsize': '0.8',
    'fontname': '"Microsoft YaHei,SimHei,Arial,sans-serif"',
    'fontsize': '9',
}

html_css_files = ['custom.css']