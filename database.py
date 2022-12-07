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

    product = Product(
        user=anna,
        name="Men's Leather Dopp Kit, Personalized Groomsman Gift, Men's Leather Accessory, Custom Mens Shave Bag, Anniversary Gift for Man, Birthday Gift",
        price="14.92",
        description="Personalized Leather Dopp Kit, Third Anniversary Gifts For Men, Leather Toiletry Bag, Birthday Gift For Dad, Valentines Day Gift For Him, Dopp Kit, Travel Bag, Personalized Groomsmen Gift, Custom Leather Toiletry Bag, Leather Personalized Gift, Mens Toiletry Bag, Father’s Day Gift, Birthday Gift, Gift for Him"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/32929192/r/il/cb7d09/3714311335/il_794xN.3714311335_4kwq.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="Of all the things I’ve ever ordered from Etsy, this one is my ultimate favorite! WOW! Words cannot express how beautiful this toiletry bag is! I almost want to give the gift to my FIL now! (Haha) I’ve shown all of my friends and family and am encouraging them to shop from this seller. It shipped so quickly and the added keychain was just the cherry on top! Absolutely wonderful product!! I will be shipping with this seller again and again!"
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="I’ve never experienced customer service like I did with Enes! They made sure I was satisfied and kept me up to date with my order without me asking. I ordered a bag with my boyfriends initials and it looks stunning 🤩 I’m so excited to gift it to him. Super satisfied with my item!!! Thank you 🙏"
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="The packaging on this items was a real surprise! The kit itself is well made and the stitching and name looks good. The color was also what I expected. I did measure when trying to decide on the size and think the next size up would have been better, but that is on me. I would definitely order this again."
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="Seller was very responsive and super quick with getting my order ready--even with a customization. The bag looks exactly like the picture and the packaging is really good!"
        ),
    ])

    db.session.commit()

    product = Product(
        user=anna,
        name="Leather iPhone 12 13 case bag, wallet with card pocket, Gift for Her, Leather Phone Bag, Leather Accessories for her",
        price="87.00",
        description="Crossbody phone bag Milley is very suitable for daily casual wearing, office occasion, travel. Especially for travel - it's perfect for holding your phone, cards and passport. This style features and adjustable strap, magnetic closure and a pocket on a back panel."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/31475762/r/il/7a4962/3416025636/il_794xN.3416025636_neol.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="I LOVE this bag!!!! It is perfect size to put some personal stuff and a place for cards and an outside pocket for your phone. I will be ordering another color! The only thing I regret was not getting my initials on the bag because I needed it fast for a trip. This shop shipped with a week and half when expected to be closer to 2-3 weeks!! Customer service was great! Responding to all my messages in a timely manner. Thank you so much!"
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="I just received my bag and I love it! Well made, quality and show the love of the creator in every detail. Thank you very much, happy customer here."
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="Perfect cell phone bag for when you don't need to carry a purse or bag. Holds the cards you need, cell phone, and chapstick, keys etc. Strap is adjustable.Bought in the wine burgundy color. Fast shipping quality product. My 3rd item from this store."
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="It’s beautifully made!!!! I just love it!"
        ),
    ])

    db.session.commit()

    product = Product(
        user=anna,
        name="Personalized Tote Bag, Bridesmaid Totes,Name Tote,Canvas Bag, Bridesmaid Gift, Bachelorette Gift, (Font 6 - 10 inch wide/ 6 inch height MAX)",
        price="9.10",
        description="Bag Dimensions are approximately 15x15 inches No Zipper Or Clip."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/28509384/r/il/0927a2/3343967865/il_794xN.3343967865_sjls.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="These are beautiful! Great size too !! Shipped super quick! Love them!"
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="Great product! Fast turn around & shipping! It came out so cute!!"
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="The tote bags look awesome! They worked with me to finalize the logo I wanted on the bags. 10/10 will recommend."
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="Absolutely love my order! Items were shipped extremely fast. I highly recommend!! Great quality!"
        ),
    ])

    db.session.commit()

    product = Product(
        user=anna,
        name="Custom Text Bags in Bulk , Custom Tote Bag, Promotional Tote Bag, Trade Show Gift Bag, Custom Shopper, Shopping Bags, Custom Text Tote",
        price="4.45",
        description="Custom Text Bag, Custom Tote Bag, Promotional Tote Bag, Trade Show Gift Bag, Custom Shopper, Shopping Bags, Custom Text Tote"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/17766621/r/il/16e3f0/4236608158/il_794xN.4236608158_aztc.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="This came out perfect. With my wording on my canvas I think it's best I don't post a picture. (Kinda explicit.) You did an amazing job. Thank you so much."
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="These bags turned out wonderfully! The graphics came out great and the colors are beautiful. I will definitely order from here again. Amazingly pleased with this order!!!"
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="I was so excited to receive my package, it was extra special because it had my business logo. it met all my needs I am obsessed."
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="Item was perfect, seller was very attentive and quick to respond to my questions! Item came very quickly!!! personalized totes for hotel guests for my son's wedding in Phila!!"
        ),
    ])

    db.session.commit()

    product = Product(
        user=anna,
        name="Campbell Tote | Choose Your Strap",
        price="37.19",
        description="Now you can build your perfect tote! Pick your favorite color Campbell Tote and then pick your favorite style strap to build the perfect bag. All straps are interchangeable!Our beautiful Campbell tote from the Threaded Pear is the perfect take anywhere bag. This stunning and durable bag features a zipper closure to access the spacious interior for all your must-have essentials. Multiple interior pockets allow for organization for all your items on the go."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/27481253/r/il/aee3c0/4146026909/il_794xN.4146026909_dfu3.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="I actually had my strap and needed a purse due to my purse breaking. I wax sent a picture of this purse! It worked perfect"
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="Love this bag. It’s massive! Perfect for professionals or moms who are transitioning out of the diaper bag phase but still have to carry random kid items. Super happy with the strap and the way the bag looks overall. I will be ordering more!"
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="This bag is the perfect size to carry my laptop and work stuff plus my normal purse items. No more carrying multiple bags as this one holds it all! The wide strap doesn't dig into your shoulder like small ones do and being able to choose the strap let me add a little bit of my style to this classy tote. Thank you!"
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="Love this bag so much! So spacious and arrived so fast! I’ve already gotten several compliments from friends and even strangers. I’ll definitely be purchasing other colors in the future."
        ),
    ])

    db.session.commit()

    product = Product(
        user=anna,
        name="Beach Tote Bags for Women Personalize, Embroidery Initial Monogram Large Bag, 100% Cotton Canvas, Bridesmaid Bachelorette Gift A-Z",
        price="18.97",
        description="- Elegant beach bag: The canvas beach tote is a classic, minimalist design bag with plenty of room for your daily summer tasks. Whether by the poolside, at the beach, or a quick grocery trip. It is big enough to fit all of the day's essentials and perfect for a weekend getaway."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/21515874/r/il/70440b/2916023872/il_794xN.2916023872_agns.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="These bags are simply beautiful. I ordered them for my bridesmaids for our wedding morning and I was concerned about the quality because some other sellers had poor reviews for similar items. However these bags are divine. They are so sturdy the entire inside is coded with a waterproof material they are beautiful the stitching is Flawless and I’m so glad that I had the idea of ordering one for myself because I would definitely be jealous of my girls if I hadn’t!"
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="I bought several of these tote bags as bridesmaids gifts, and they’re perfect. They are a good size, sturdy, and they come with a hard interior bottom insert that keeps them from tipping over. The embroidered letters look perfect. Love them!"
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="I ordered 5 of these and they arrived in time for my trip, they were neatly packaged so I can easily pack, size is perfect for a beach/pool bag, super cute, and they feel sturdy."
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="I ordered 5 of these and they arrived in time for my trip, they were neatly packaged so I can easily pack, size is perfect for a beach/pool bag, super cute, and they feel sturdy."
        ),
    ])

    db.session.commit()

    product = Product(
        user=anna,
        name="MakeUp Bag Make Up Bag Bridesmaid Make Up Bag with Name Birthday Gift Ideas for Her (EB3222AD)",
        price="7.22",
        description="Make Up Bags personalized with a name in pretty script make a great gift for bridesmaids or a birthday gift for any woman. Customize each bag with her name. Cosmetic Bags are lined on the inside and have a metallic zipper."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/8617622/r/il/0c6972/2264040092/il_794xN.2264040092_5oim.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="This seller is amazing! Unfortunately, my original shipment was lost/stolen and this seller worked with me on the replacement shipment and even expedited the shipping! Make up bags and mirrors are gorgeous, pictures really do not do the make up bags any justice. The pink with rose gold lettering is my fave combo and the pink is so pretty and flattering. Great customer service. Incredibly happy with my items and my experience with this shop."
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="The makeup bags were exactly as pictured. I ordered them as Christmas gifts for my nieces in their tween and teen years. It was easy to pick bag color and choice of font and print color. Shipped quickly and came nicely packaged."
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="Bags came out better than I thought! My 2 girls are going to love it!"
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="Super cute! My favorite part is the satin like inside."
        ),
    ])

    db.session.commit()

    product = Product(
        user=anna,
        name="Leather briefcase man, leather bag man, mens briefcase, shoulder bag, laptop messenger bag, satchel bag, new job gift, graduation gift",
        price="147.00",
        description="This comfortable genuine leather briefcase can be a great addition to any outfit and an excellent helper for every day. It is convenient to carry a laptop, wallet, documents, books, keys everything you need to have at hand. This is a great gift, especially if you add personalization, for a friend, boyfriend, husband, brother, dad for any occasion."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket(
                "https://i.etsystatic.com/29566173/r/il/956aa9/4036801838/il_794xN.4036801838_jl78.jpg"),
            preview=True
        ),

        Review(
            user=brian,
            product=product,
            rating=5,
            review="I love my new briefcase bag!! It’s such a great feeling supporting a small business and having a handmade, leather bag that is very functional, unique, personalized, and durable! I already purchased another matching bag from Jordan (the duffel bag) because I’m so pleased."
        ),

        Review(
            user=caitlynn,
            product=product,
            rating=5,
            review="Thanks a lot !!"
        ),

        Review(
            user=derrik,
            product=product,
            rating=5,
            review="I’m very happy with this bag. The leather quality is outstanding, the style is great, and the stitching is top-notch. I bought the large size, and there is plenty of room for my laptop, charger, and a few (small) 1” binders and folders, etc. I’m very confident that this bag will last for years if not decades (with proper leather care of course). All in all, I couldn’t be happier!"
        ),

        Review(
            user=elizabeth,
            product=product,
            rating=5,
            review="thanks!You've just made my day!"
        ),
    ])

    db.session.commit()
