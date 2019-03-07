{
    "name": """Demo Data for \"Real Multi Website\"""",
    "summary": """Provides demo websites""",
    "category": "Hidden",
    # "live_test_URL": "",
    "images": [],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        "website_multi_company_sale",
        "website_multi_company_blog",
        "theme_bootswatch",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
    ],
    "qweb": [
    ],
    "demo": [
        "demo/res.company.csv",
        "demo/website.csv",
        "demo/product_public_category_demo.xml",
        "demo/product.template.csv",
        "demo/ir.ui.view.csv",
        "demo/website_page.xml",
        "demo/website.menu.csv",
        "demo/website_templates.xml",
        "demo/website_homepage.xml",
        "demo/website_blog.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
