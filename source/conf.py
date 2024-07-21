# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Enzo Busseti'
copyright = '2024, Enzo Busseti'
author = 'Enzo Busseti'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_title = 'Enzo Busseti Personal Website'
html_static_path = ['_static']

# put CNAME in the build folder
# html_extra_path = ['../CNAME']

###
# Customizations to the pydata sphinx theme for personal website
###

# remove sphinx line from footer
html_show_sphinx = False

# this dict is the main customization; gets populated with defaults (see
# pydata-sphinx docs), apart from user settings specified here
html_theme_options = {

    # remove site search cell
    "navbar_persistent": [],

    # remove light/dark theme switcher
    "navbar_end": [],

    # remove right bar
    "secondary_sidebar_items": [],
    "primary_sidebar_end": [],

    # remove footer content
    "footer_start": [],
    "footer_end": [],

    # remove prev/next buttons
    "show_prev_next": False,
    }

# this should remove the sidebar from all pages
html_sidebars = {
  "*": []
}

# for extra customization can extend source/_static/css/custom.css
html_css_files = ["css/custom.css"]
