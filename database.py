from app import app
from app.models import db, User, Product, ProductImage, Review
from upload import upload_image_to_bucket
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    ###########
    ## Users ##
    ###########

    anna = User(display_name="Anna",
                email="email@email.com",
                password="password")
    brian = User(display_name="Brian",
                 email="email2@email.com",
                 password="password")
    caitlynn = User(display_name="Caitlynn",
                    email="email3@email.com",
                    password="password")
    derrik = User(display_name="Derrik",
                  email="email4@email.com",
                  password="password")
    elizabeth = User(display_name="Elizabeth",
                     email="email5@email.com",
                     password="password")
    db.session.add_all([anna, brian, caitlynn, derrik, elizabeth])
    db.session.commit()

    ##############
    ## Products ##
    ##############

    product = Product(
        user=anna,
        name="60%Off customized straw bags Personalized WEDDING GUEST GIFT monogrammed bag bridal shower bags,custom beach bag,straw tote,embroidered bag",
        price="28.00",
        description="This straw is Personalized order and send me your name Personalized you want Write it down in this bags"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/23020574/r/il/831fda/3099213156/il_794xN.3099213156_rar7.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="I love, love how the bag turned out!!! So cute!! Amazing customer service and quick delivery… My only complaint was the packaging for shipping. I felt like the basket got a little banged up in transit because it was just in like a bag. Otherwise couldn’t recommend any more!"
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="This is the perfect little bag for summer! It fits a lot and still looks stylish! I’m so glad I found this!"
        ),

        Review(
            user=derrik,
            product=product,
            rating=3,
            review="I'll start by saying that I was pleased with my bags when they arrived. Shipping was pretty quick, but the packaging was essentially a tarp wrapped around the bags and duct taped. My biggest issue was communication. I ordered 5 bags for myself and my bridesmaids for my upcoming wedding and wanted personalized writing on the bags. Nowhere in the listing did it indicate that there was a character limit, or that I would be upcharged for a larger bag if I exceeded that character limit. I actually used a phrase that is advertised in one of the listing pictures, but was informed there would be an additional surcharge because the writing wouldn't fit. Ultimately, I had to pay an extra $24 for 3 larger bags, but the seller did use the same larger bag for my 2 remaining items for free. Just be aware of this when placing your order."
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=4,
            review="Only complaint is that the text is not centered on the bag - is pretty 'left justified'. Otherwise, super adorable product and fast shipping."
        ),
    ])

    db.session.commit()
