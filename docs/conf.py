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

html_css_files = ['custom.css']