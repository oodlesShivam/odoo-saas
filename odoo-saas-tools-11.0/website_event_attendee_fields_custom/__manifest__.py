{
    "name": """Attendee registration: Birthdate, Passport, Nationality""",
    "summary": """Ask information on registration and stores at Partner record""",
    "category": "Marketing",
    "live_test_url": "http://apps.it-projects.info/shop/product/portal-event-tickets?version=10.0",
    "images": ["images/banner.jpg"],
    "version": "10.0.1.0.1",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/yelizariev",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        "website_event_attendee_fields",
        "partner_contact_birthdate",
        "partner_firstname",
        "partner_identification",
        "partner_contact_nationality",
        "website_event_sale",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/event_event_attendee_field_data.xml",
        "views/website_event_templates.xml",
    ],
    "qweb": [
    ],
    "demo": [
        "data/event_event_demo.yml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": False,
}
