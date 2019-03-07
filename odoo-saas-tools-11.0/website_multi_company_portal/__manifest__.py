{
    "name": """Real Multi Website (portal extension)""",
    "summary": """Multi Website support in Portal""",
    "category": "Portal",
    "live_test_url": "http://apps.it-projects.info/shop/product/website-multi-company?version=10.0",
    "images": ["images/website_multi_company_portal_main.png"],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/yelizariev",
    "license": "LGPL-3",
    "price": 9.00,
    "currency": "EUR",

    "depends": [
        "website_multi_company",
        "portal",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
