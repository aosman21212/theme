# -*- coding: utf-8 -*-
# =============================================================================
#  LeapAI Liquid Glass Backend Theme
# -----------------------------------------------------------------------------
#  Location  : King Abdulaziz Branch Road, Riyadh, Saudi Arabia
#  Email     : sales@leapai.ai
#  Phone     : +966 53 553 3627
#  Website   : https://leapai.ai
#  Developer : Abdulkaraim Osman — Tech Manager | Backend Engineer | DevOps Engineer
#              at Bab International Corp For Specialized Services
#  LinkedIn  : https://www.linkedin.com/in/abdulkaraim-o-385b7a110/
# =============================================================================
{
    'name': 'LeapAI Liquid Glass Backend Theme',
    'version': '19.0.1.0.0',
    'category': 'Theme/Backend',
    'summary': 'Modern glassmorphism backend theme for Odoo by LeapAI',
    'description': """
        LeapAI Liquid Glass Backend Theme
        A modern, elegant glassmorphism design for Odoo backend
    """,
    'author': 'leapai.ai',
    'maintainer': 'Abdulkaraim Osman',
    'support': 'sales@leapai.ai',
    'website': 'https://leapai.ai/en/',
    'license': 'LGPL-3',
    'depends': ['web', 'base'],
    'assets': {
        'web.assets_backend': [
            'leapai_liquid_glass/static/src/scss/variables.scss',
            'leapai_liquid_glass/static/src/scss/glass_theme.scss',
            'leapai_liquid_glass/static/src/scss/buttons.scss',
            'leapai_liquid_glass/static/src/scss/forms.scss',
            'leapai_liquid_glass/static/src/scss/lists.scss',
            'leapai_liquid_glass/static/src/scss/kanban.scss',
            'leapai_liquid_glass/static/src/scss/modals.scss',
            'leapai_liquid_glass/static/src/scss/navbar.scss',
            'leapai_liquid_glass/static/src/js/navbar_sidebar.js',
            'leapai_liquid_glass/static/src/xml/apps_sidebar.xml',
        ],
        'web.assets_backend_lazy': [
            'leapai_liquid_glass/static/src/js/canvas_text.js',
        ],
        'web.assets_web': [
            'leapai_liquid_glass/static/src/scss/website.scss',
        ],
    },
    'images': [
        'static/description/banner.jpg',
        'static/description/theme_screenshot.jpg',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
