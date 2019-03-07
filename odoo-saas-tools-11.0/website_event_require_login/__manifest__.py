{
    "name": """Tickets purchasing: force user to sign in / sign up""",
    "summary": """User registration at your portal is always a plus for marketing""",
    "category": "Marketing",
    "live_test_url": "http://apps.it-projects.info/shop/product/portal-event-tickets?version=10.0",
    "images": ["images/banner.jpg"],
    "version": "10.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/yelizariev",
    "license": "LGPL-3",
    "price": 37.00,
    "currency": "EUR",

    "depends": [
        "website_event",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/website_event_sale_templates.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": False,
}
