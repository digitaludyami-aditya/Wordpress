"""Portfolio sites for digitaludyami.com/portfolio

Edit this list, then run `python3 build.py`.

Each row: (url, display name, Type, Category, check)
  Type      one of: E-commerce, Corporate, Blog, Lead Generation, Educational
  Category  industry, for example: Clothing & Fashion, Loan & Finance, D2C ...
  check     True = I could not see the site, so Type/Category are my best guess from
            the name. Please confirm these. The capture tool prints each site's title
            and description to help.

Technology (WordPress, Shopify, React ...) is NOT guessed here. The capture tool
(tools/capture.js) detects it from the live site. To force a value for a site, add it
to TECH_OVERRIDE below.
"""

SHOTS_BASE = "https://www.digitaludyami.com/wp-content/uploads/portfolio/"  # where you upload tools/out/shots/*.jpg

TECH_OVERRIDE = {
    # "modishh-co-in": "Shopify",
}

SITES = [
    ("https://vedicyogacentre.org/", "Vedic Yoga Centre", "Corporate", "Yoga & Wellness", False),
    ("https://hitechpipes.in/", "Hitech Pipes", "Corporate", "Manufacturing", False),
    ("https://settlementonloan.com/", "Settlement on Loan", "Lead Generation", "Loan & Finance", False),
    ("https://kiddieskingdomplayarea.in/", "Kiddies Kingdom Play Area", "Corporate", "Kids & Entertainment", False),
    ("https://www.kktalksfinance.com/", "KK Talks Finance", "Blog", "Loan & Finance", True),
    ("https://truckinzy.com/", "Truckinzy", "Corporate", "Logistics & Transport", True),
    ("https://yogvishwasyogshala.com/", "Yog Vishwas Yogshala", "Corporate", "Yoga & Wellness", False),
    ("https://meri.edu.in/", "MERI", "Educational", "Education", False),
    ("https://www.primegoldgroup.com/", "Prime Gold Group", "Corporate", "Business Services", True),
    ("https://www.rudrayogpeeth.org/", "Rudra Yog Peeth", "Corporate", "Yoga & Wellness", False),
    ("https://swaastikyogschool.com/", "Swaastik Yoga School", "Corporate", "Yoga & Wellness", False),
    ("https://udyamitahelpline.com/", "Udyamita Helpline", "Lead Generation", "Business Services", True),
    ("https://newgenhealthcare.in/", "NewGen Healthcare", "Corporate", "Healthcare", False),
    ("https://www.zeluxled.com/", "Zelux LED", "Corporate", "Lighting & Electricals", True),
    ("https://modishh.co.in/", "Modishh", "E-commerce", "Clothing & Fashion", False),
    ("https://www.jaypeegreensproperties.com/", "Jaypee Greens Properties", "Corporate", "Real Estate", False),
    ("https://blueskyconsultancy.com/", "Bluesky Consultancy", "Corporate", "Consulting", True),
    ("https://www.mavenconsultingservices.com/", "Maven Consulting Services", "Corporate", "Consulting", False),
    ("https://convexgadgets.com/", "Convex Gadgets", "E-commerce", "Electronics & Gadgets", False),
    ("https://www.d2csale.com/", "D2C Sale", "E-commerce", "D2C", False),
    ("https://archiesonline.com/", "Archies Online", "E-commerce", "Gifts & Cards", False),
    ("https://rossettecoffee.com/", "Rossette Coffee", "E-commerce", "Food & Beverage", True),
    ("https://airpest.in/", "Airpest", "Corporate", "Pest Control & Services", True),
    ("https://magnusarc.com/", "Magnus Arc", "Corporate", "Architecture & Design", True),
    ("https://sparshmedia.com/", "Sparsh Media", "Corporate", "Media & Marketing", True),
    ("https://okana.co.nz/", "Okana", "E-commerce", "General", True),
    ("https://quirkytales.in/", "Quirky Tales", "E-commerce", "General", True),
    ("https://aarbab.com/", "Aarbab", "E-commerce", "General", True),
    ("https://www.botnia.in/", "Botnia", "E-commerce", "General", True),
    ("https://www.teez.in/", "Teez", "E-commerce", "Clothing & Fashion", True),
    ("https://meticsfashion.com/", "Metics Fashion", "E-commerce", "Clothing & Fashion", False),
    ("https://lovemodisch.com/", "Love Modisch", "E-commerce", "Clothing & Fashion", False),
    ("https://chelvet.com/", "Chelvet", "E-commerce", "Clothing & Fashion", True),
    ("https://balwom.in/", "Balwom", "E-commerce", "Clothing & Fashion", True),
    ("https://sleepnslip.com/", "Sleep N Slip", "E-commerce", "Clothing & Fashion", True),
    ("https://unitravels.in/", "Uni Travels", "Corporate", "Travel & Tours", False),
    ("https://avianexperiences.com/", "Avian Experiences", "Corporate", "Travel & Tours", False),
    ("https://www.traveloholicadventures.com/", "Traveloholic Adventures", "Corporate", "Travel & Tours", False),
    ("https://srisaitours.co.in/", "Sri Sai Tours", "Corporate", "Travel & Tours", False),
    ("https://travenciaindia.com/", "Travencia India", "Corporate", "Travel & Tours", False),
    ("https://decoruss.com/", "Decoruss", "E-commerce", "Home Decor", True),
    ("https://pivotrealestate.com.au/", "Pivot Real Estate", "Corporate", "Real Estate", False),
    ("https://www.dezirehomes.com.au/", "Dezire Homes", "Corporate", "Real Estate", False),
    ("https://cnrintellects.com/", "CNR Intellects", "Corporate", "Consulting", True),
    ("https://cnrpartners.com/", "CNR Partners", "Corporate", "Consulting", True),
]
