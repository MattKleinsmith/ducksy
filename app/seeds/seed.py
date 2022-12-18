from app.models import db, environment, SCHEMA, User, Product, ProductImage, Review, Category, Order, OrderDetail
from app.seeds.upload import upload_image_to_bucket_from_url
from random import randint

# Adds a demo user, you can add other users here if you want


def seed_all():
    ###########
    ## Users ##
    ###########

    anna = User(display_name="Anna",
                email="email@email.com",
                password="password",
                profile_picture_url=upload_image_to_bucket_from_url("https://avatars.githubusercontent.com/u/98060462"))
    brian = User(display_name="Brian",
                 email="email2@email.com",
                 password="password",
                 profile_picture_url=upload_image_to_bucket_from_url("https://cdn.discordapp.com/avatars/872026711506694144/dd925f9567051c4ff4e60d3f345625eb.png"))
    caitlynn = User(display_name="Caitlynn",
                    email="email3@email.com",
                    password="password",
                    profile_picture_url=upload_image_to_bucket_from_url("https://avatars.githubusercontent.com/u/106051387"))
    derrik = User(display_name="Derrik",
                  email="email4@email.com",
                  password="password",
                  profile_picture_url=upload_image_to_bucket_from_url("https://cdn.discordapp.com/avatars/974032930202583140/f8deca01d6afdfcf27a12f2cf4dece59.png"))
    elizabeth = User(display_name="Elizabeth",
                     email="email5@email.com",
                     password="password",
                     profile_picture_url=upload_image_to_bucket_from_url("https://cdn.discordapp.com/avatars/485640660490387456/0b1731101c8e53e2758b6c95e34337d0.png"))

    demo = User(display_name="Demo",
                email="demo@aa.io",
                password="password")
    marnie = User(display_name="marnie",
                  email="marnie@aa.io",
                  password="password")
    bobbie = User(display_name="bobbie",
                  email="bobbie@aa.io",
                  password="password",
                  profile_picture_url=upload_image_to_bucket_from_url("https://cdn.discordapp.com/avatars/182662416633561089/c0d48f71e483b33f109e694782949510.png"))

    db.session.add_all([anna, brian, caitlynn, derrik,
                       elizabeth, demo, marnie, bobbie])
    db.session.commit()

    ################
    ## Categories ##
    ################

    wedding = Category(name="wedding")
    boyfriend = Category(name="boyfriend")
    girlfriend = Category(name="girlfriend")
    gift = Category(name="gift")
    bag = Category(name="bag")
    case = Category(name="case")
    personalized_gift = Category(name="personalized_gift")
    leather = Category(name="leather")
    home_decor = Category(name="home_decor")
    newborn = Category(name="newborn")
    child = Category(name="child")
    toy = Category(name="toy")

    ##############
    ## Products ##
    ##############

    product = Product(
        seller=anna,
        categories=[wedding, gift, girlfriend, bag],
        name="60%Off customized straw bags Personalized WEDDING GUEST GIFT monogrammed bag bridal shower bags,custom beach bag,straw tote,embroidered bag",
        price="28.00",
        description="This straw is Personalized order and send me your name Personalized you want Write it down in this bags"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23020574/r/il/831fda/3099213156/il_794xN.3099213156_rar7.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23020574/r/il/fad766/3146934257/il_1588xN.3146934257_lnos.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23020574/r/il/d928ce/3099213096/il_1588xN.3099213096_n86d.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23020574/r/il/499c97/3146934189/il_1588xN.3146934189_sb01.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23020574/r/il/3d113a/3146934181/il_1588xN.3146934181_7nex.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23020574/r/il/3fffd4/3146934133/il_1588xN.3146934133_hbmo.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23020574/r/il/67c451/3146934239/il_1588xN.3146934239_ik6z.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="I love, love how the bag turned out!!! So cute!! Amazing buyer service and quick delivery… My only complaint was the packaging for shipping. I felt like the basket got a little banged up in transit because it was just in like a bag. Otherwise couldn’t recommend any more!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="This is the perfect little bag for summer! It fits a lot and still looks stylish! I’m so glad I found this!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=3,
            review="I'll start by saying that I was pleased with my bags when they arrived. Shipping was pretty quick, but the packaging was essentially a tarp wrapped around the bags and duct taped. My biggest issue was communication. I ordered 5 bags for myself and my bridesmaids for my upcoming wedding and wanted personalized writing on the bags. Nowhere in the listing did it indicate that there was a character limit, or that I would be upcharged for a larger bag if I exceeded that character limit. I actually used a phrase that is advertised in one of the listing pictures, but was informed there would be an additional surcharge because the writing wouldn't fit. Ultimately, I had to pay an extra $24 for 3 larger bags, but the seller did use the same larger bag for my 2 remaining items for free. Just be aware of this when placing your order."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4,
            review="Only complaint is that the text is not centered on the bag - is pretty 'left justified'. Otherwise, super adorable product and fast shipping."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding, boyfriend, gift],
        name="Men's Leather Dopp Kit, Personalized Groomsman Gift, Men's Leather Accessory, Custom Mens Shave Bag, Anniversary Gift for Man, Birthday Gift",
        price="14.92",
        description="Personalized Leather Dopp Kit, Third Anniversary Gifts For Men, Leather Toiletry Bag, Birthday Gift For Dad, Valentines Day Gift For Him, Dopp Kit, Travel Bag, Personalized Groomsmen Gift, Custom Leather Toiletry Bag, Leather Personalized Gift, Mens Toiletry Bag, Father’s Day Gift, Birthday Gift, Gift for Him"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/cb7d09/3714311335/il_794xN.3714311335_4kwq.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/490c85/3478726118/il_1588xN.3478726118_cq9g.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/73824a/3890948405/il_1588xN.3890948405_dpmf.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/0fc8b8/3890948387/il_1588xN.3890948387_o5r0.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/5f5055/3889937763/il_1588xN.3889937763_s56t.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/ed4ec5/3889941053/il_1588xN.3889941053_3xj1.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/34db34/3526372801/il_1588xN.3526372801_s24t.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/69854a/3481338888/il_1588xN.3481338888_osh1.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32929192/r/il/98071f/3842438288/il_1588xN.3842438288_4uzt.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="Of all the things I’ve ever ordered from Etsy, this one is my ultimate favorite! WOW! Words cannot express how beautiful this toiletry bag is! I almost want to give the gift to my FIL now! (Haha) I’ve shown all of my friends and family and am encouraging them to seller from this seller. It shipped so quickly and the added keychain was just the cherry on top! Absolutely wonderful product!! I will be shipping with this seller again and again!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I've never experienced buyer service like I did with Enes! They made sure I was satisfied and kept me up to date with my order without me asking. I ordered a bag with my boyfriends initials and it looks stunning 🤩 I'm so excited to gift it to him. Super satisfied with my item!!! Thank you 🙏"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="The packaging on this items was a real surprise! The kit itself is well made and the stitching and name looks good. The color was also what I expected. I did measure when trying to decide on the size and think the next size up would have been better, but that is on me. I would definitely order this again."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Seller was very responsive and super quick with getting my order ready--even with a customization. The bag looks exactly like the picture and the packaging is really good!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[girlfriend, bag, case],
        name="Leather iPhone 12 13 case bag, wallet with card pocket, Gift for Her, Leather Phone Bag, Leather Accessories for her",
        price="87.00",
        description="Crossbody phone bag Milley is very suitable for daily casual wearing, office occasion, travel. Especially for travel - it's perfect for holding your phone, cards and passport. This style features and adjustable strap, magnetic closure and a pocket on a back panel."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/7a4962/3416025636/il_794xN.3416025636_neol.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/1c7ca9/3375663430/il_1588xN.3375663430_8iom.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/67771d/3415990988/il_1588xN.3415990988_iisk.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/a60150/3415986242/il_1588xN.3415986242_t37f.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/1f74de/4291529578/il_1588xN.4291529578_3jqc.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/7ab155/4191194083/il_1588xN.4191194083_m91m.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/4ac5ca/3375665586/il_1588xN.3375665586_fesp.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/cfedfe/3375661820/il_1588xN.3375661820_3gap.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/b739ae/4143913686/il_1588xN.4143913686_8quk.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="I LOVE this bag!!!! It is perfect size to put some personal stuff and a place for cards and an outside pocket for your phone. I will be ordering another color! The only thing I regret was not getting my initials on the bag because I needed it fast for a trip. This seller shipped with a week and half when expected to be closer to 2-3 weeks!! buyer service was great! Responding to all my messages in a timely manner. Thank you so much!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I just received my bag and I love it! Well made, quality and show the love of the creator in every detail. Thank you very much, happy buyer here."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Perfect cell phone bag for when you don't need to carry a purse or bag. Holds the cards you need, cell phone, and chapstick, keys etc. Strap is adjustable.Bought in the wine burgundy color. Fast shipping quality product. My 3rd item from this store."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="It’s beautifully made!!!! I just love it!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding, girlfriend, bag, gift],
        name="Personalized Tote Bag, Bridesmaid Totes,Name Tote,Canvas Bag, Bridesmaid Gift, Bachelorette Gift, (Font 6 - 10 inch wide/ 6 inch height MAX)",
        price="9.10",
        description="Bag Dimensions are approximately 15x15 inches No Zipper Or Clip."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/28509384/r/il/0927a2/3343967865/il_794xN.3343967865_sjls.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/28509384/r/il/74386f/3296265660/il_1588xN.3296265660_4osh.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/28509384/r/il/84a682/3294635830/il_1588xN.3294635830_hlx8.jpg"),
            preview=False
        ),


        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/28509384/r/il/69ea0d/3358133601/il_1588xN.3358133601_odoq.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/28509384/r/il/38041d/3358133381/il_1588xN.3358133381_lqpf.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/28509384/r/il/e9e519/3663698967/il_1588xN.3663698967_5vxb.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/28509384/r/il/41842b/3663698885/il_1588xN.3663698885_apk3.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="These are beautiful! Great size too !! Shipped super quick! Love them!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Great product! Fast turn around & shipping! It came out so cute!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="The tote bags look awesome! They worked with me to finalize the logo I wanted on the bags. 10/10 will recommend."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Absolutely love my order! Items were shipped extremely fast. I highly recommend!! Great quality!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[bag, personalized_gift],
        name="Custom Text Bags in Bulk , Custom Tote Bag, Promotional Tote Bag, Trade Show Gift Bag, Custom sellerper, sellerping Bags, Custom Text Tote",
        price="4.45",
        description="Custom Text Bag, Custom Tote Bag, Promotional Tote Bag, Trade Show Gift Bag, Custom sellerper, sellerping Bags, Custom Text Tote"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17766621/r/il/16e3f0/4236608158/il_794xN.4236608158_aztc.jpg"),
            preview=True
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="This came out perfect. With my wording on my canvas I think it's best I don't post a picture. (Kinda explicit.) You did an amazing job. Thank you so much."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="These bags turned out wonderfully! The graphics came out great and the colors are beautiful. I will definitely order from here again. Amazingly pleased with this order!!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I was so excited to receive my package, it was extra special because it had my business logo. it met all my needs I am obsessed."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Item was perfect, seller was very attentive and quick to respond to my questions! Item came very quickly!!! personalized totes for hotel guests for my son's wedding in Phila!!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[bag, gift],
        name="Campbell Tote | Choose Your Strap",
        price="37.19",
        description="Now you can build your perfect tote! Pick your favorite color Campbell Tote and then pick your favorite style strap to build the perfect bag. All straps are interchangeable!Our beautiful Campbell tote from the Threaded Pear is the perfect take anywhere bag. This stunning and durable bag features a zipper closure to access the spacious interior for all your must-have essentials. Multiple interior pockets allow for organization for all your items on the go."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/aee3c0/4146026909/il_794xN.4146026909_dfu3.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/52186d/3759312349/il_1588xN.3759312349_5e1s.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/be0888/3711743784/il_1588xN.3711743784_73im.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/03ea82/4146016113/il_1588xN.4146016113_oz2z.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/a8a692/4098359482/il_1588xN.4098359482_q6sx.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/3640f4/3759312653/il_1588xN.3759312653_k3c0.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/d6f597/4138828614/il_1588xN.4138828614_7i59.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/c0e07b/4186489933/il_1588xN.4186489933_lq60.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/e89ace/4138829272/il_1588xN.4138829272_ix21.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27481253/r/il/6d94ba/4138829522/il_1588xN.4138829522_40bj.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="I actually had my strap and needed a purse due to my purse breaking. I wax sent a picture of this purse! It worked perfect"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Love this bag. It’s massive! Perfect for professionals or moms who are transitioning out of the diaper bag phase but still have to carry random kid items. Super happy with the strap and the way the bag looks overall. I will be ordering more!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="This bag is the perfect size to carry my laptop and work stuff plus my normal purse items. No more carrying multiple bags as this one holds it all! The wide strap doesn't dig into your shoulder like small ones do and being able to choose the strap let me add a little bit of my style to this classy tote. Thank you!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Love this bag so much! So spacious and arrived so fast! I’ve already gotten several compliments from friends and even strangers. I’ll definitely be purchasing other colors in the future."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[bag, personalized_gift],
        name="Beach Tote Bags for Women Personalize, Embroidery Initial Monogram Large Bag, 100% Cotton Canvas, Bridesmaid Bachelorette Gift A-Z",
        price="18.97",
        description="- Elegant beach bag: The canvas beach tote is a classic, minimalist design bag with plenty of room for your daily summer tasks. Whether by the poolside, at the beach, or a quick grocery trip. It is big enough to fit all of the day's essentials and perfect for a weekend getaway."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/70440b/2916023872/il_794xN.2916023872_agns.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/1c7a2a/3854800271/il_1588xN.3854800271_obi0.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/27274f/3872663237/il_1588xN.3872663237_b73y.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/73de40/2109966780/il_1588xN.2109966780_f0o2.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/1494ff/3895691133/il_1588xN.3895691133_b9zu.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/64eb90/3157818513/il_1588xN.3157818513_sjcb.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/9c9483/2117559993/il_1588xN.2117559993_9qnp.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21515874/r/il/576709/2069990788/il_1588xN.2069990788_4356.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="These bags are simply beautiful. I ordered them for my bridesmaids for our wedding morning and I was concerned about the quality because some other sellers had poor reviews for similar items. However these bags are divine. They are so sturdy the entire inside is coded with a waterproof material they are beautiful the stitching is Flawless and I’m so glad that I had the idea of ordering one for myself because I would definitely be jealous of my girls if I hadn’t!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I bought several of these tote bags as bridesmaids gifts, and they’re perfect. They are a good size, sturdy, and they come with a hard interior bottom insert that keeps them from tipping over. The embroidered letters look perfect. Love them!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I ordered 5 of these and they arrived in time for my trip, they were neatly packaged so I can easily pack, size is perfect for a beach/pool bag, super cute, and they feel sturdy."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I ordered 5 of these and they arrived in time for my trip, they were neatly packaged so I can easily pack, size is perfect for a beach/pool bag, super cute, and they feel sturdy."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding, gift, bag],
        name="MakeUp Bag Make Up Bag Bridesmaid Make Up Bag with Name Birthday Gift Ideas for Her (EB3222AD)",
        price="7.22",
        description="Make Up Bags personalized with a name in pretty script make a great gift for bridesmaids or a birthday gift for any woman. Customize each bag with her name. Cosmetic Bags are lined on the inside and have a metallic zipper."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/0c6972/2264040092/il_794xN.2264040092_5oim.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/c0510a/2271000930/il_1588xN.2271000930_4nu0.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/4876ec/2143657481/il_1588xN.2143657481_tiqt.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/be1d24/2318598873/il_1588xN.2318598873_33fn.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/61d7d3/2271001676/il_1588xN.2271001676_4cdi.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/200fa7/2135455738/il_1588xN.2135455738_2wwe.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/c417ee/3106133842/il_1588xN.3106133842_3kkd.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8617622/r/il/ca6d5d/3880525610/il_1588xN.3880525610_k3lt.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="This seller is amazing! Unfortunately, my original shipment was lost/stolen and this seller worked with me on the replacement shipment and even expedited the shipping! Make up bags and mirrors are gorgeous, pictures really do not do the make up bags any justice. The pink with rose gold lettering is my fave combo and the pink is so pretty and flattering. Great buyer service. Incredibly happy with my items and my experience with this seller."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="The makeup bags were exactly as pictured. I ordered them as Christmas gifts for my nieces in their tween and teen years. It was easy to pick bag color and choice of font and print color. Shipped quickly and came nicely packaged."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Bags came out better than I thought! My 2 girls are going to love it!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Super cute! My favorite part is the satin like inside."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=brian,
        categories=[boyfriend, leather, bag, case],
        name="Leather briefcase man, leather bag man, mens briefcase, shoulder bag, laptop messenger bag, satchel bag, new job gift, graduation gift",
        price="147.00",
        description="This comfortable genuine leather briefcase can be a great addition to any outfit and an excellent helper for every day. It is convenient to carry a laptop, wallet, documents, books, keys everything you need to have at hand. This is a great gift, especially if you add personalization, for a friend, boyfriend, husband, brother, dad for any occasion."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/956aa9/4036801838/il_794xN.4036801838_jl78.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/a9d3a1/3215372425/il_1588xN.3215372425_t00v.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/ef1b05/3254013457/il_1588xN.3254013457_98tn.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/773447/3225389747/il_1588xN.3225389747_7tx1.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/80a445/4334997689/il_1588xN.4334997689_gj8u.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/ac5cf0/3254017891/il_1588xN.3254017891_d4l9.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/221a6d/3181554992/il_1588xN.3181554992_tsyd.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/29566173/r/il/2b8f93/4039378744/il_1588xN.4039378744_m5gw.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="I love my new briefcase bag!! It’s such a great feeling supporting a small business and having a handmade, leather bag that is very functional, unique, personalized, and durable! I already purchased another matching bag from Jordan (the duffel bag) because I’m so pleased."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Thanks a lot !!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I’m very happy with this bag. The leather quality is outstanding, the style is great, and the stitching is top-notch. I bought the large size, and there is plenty of room for my laptop, charger, and a few (small) 1” binders and folders, etc. I’m very confident that this bag will last for years if not decades (with proper leather care of course). All in all, I couldn’t be happier!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="thanks!You've just made my day!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor, personalized_gift, child],
        name="Personalized Night Light with Moon & Stars - Nursery Decor - Custom Name Light Night Gift - Kids Room Decor - Personalized Gifts for Kids",
        price="36.99",
        description="Custom Rainbow Night Light"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/c4c01c/2873811274/il_794xN.2873811274_mrtd.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/0e004a/3571770510/il_1588xN.3571770510_j6y1.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/6a3644/3619396337/il_1588xN.3619396337_ohih.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/7c6f27/3571769514/il_1588xN.3571769514_dnpg.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/9776c2/3619395923/il_1588xN.3619395923_qvg3.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/e36494/3619394791/il_1588xN.3619394791_8is3.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/bf3a8a/3571771138/il_1588xN.3571771138_8u0r.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/5e8f5c/3619394805/il_1588xN.3619394805_257z.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/cf9c3c/3619397621/il_1588xN.3619397621_sxrc.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=3,
            review="The product is nice but the picture is deceiving, it is a lot smaller than the posted picture. The quality is okay! The shipping was very quick but I did pay for fast shipping. I gave it 3 stars because I had wrote down under personalization the wrong name; after I noticed that I msged them hrs later and they were able to change it for me."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="The night light is absolutely perfect. The quality, the craftsmanship, the time it took to arrive!! I’m so glad I found this seller bc I couldn’t have picked a better place for my gift. The response times were almost instantaneous and the package arrived and you could tell it was handled with care. Thank you for making these amazing items. 20 out of 10 I recommend!!! (Pictured with the plastic still on bc it is a gift)"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=1,
            review="The item written name was must smaller than anticipated and connects with a USB plug. Just did not look as amazing as the photo."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="This night light was perfect! Love how it looks and the quality of it"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[newborn, gift, personalized_gift],
        name="Birth Flower Jewelry Travel Case, Birth Month Flower Gift, Personalized Birthday Gift, Leather Jewelry Travel Case, Custom Jewelry Case",
        price="14.49",
        description="Personalized Jewelry Boxes, Birth Flower Jewelry Case, Travel Case For Bridesmaids, Minimal Jewelry Box, Jewelry Organizer, Jewelry Box"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/e1510f/4033777789/il_794xN.4033777789_dqlw.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/3f876c/4248811668/il_1588xN.4248811668_qimg.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/f97159/4033778219/il_1588xN.4033778219_m8za.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/166da7/4033778223/il_1588xN.4033778223_sp6a.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/5aca21/4033778233/il_1588xN.4033778233_pkrc.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/3defa8/4033778221/il_1588xN.4033778221_fffh.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/eabb31/3986126544/il_1588xN.3986126544_dbum.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/5fa922/4033778467/il_1588xN.4033778467_bbiz.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/3c568d/3986127254/il_1588xN.3986127254_ltgj.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/35966576/r/il/c849c5/4296447437/il_1588xN.4296447437_fzz0.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="Beautiful! The photos don’t do them justice. Very satisfied!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Oh my gosh, if I didn't have this custom with my cousins name (the flowers are totally fine) I would be keeping this for myself haha it's so cute and small. Perfect nightstand/travel size. The inside is nice n study and the outside is soft. The teal color is beautiful! Definitely recommend for gifts. I'm gifting it for Christmas this year and will likely share the link after so she can get me one as well lol!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="This came out amazing! Love it, will purchase agian!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I am so happy with this item! Matched the description and arrived fast! It’s a Christmas present so I hope my daughter loves it as much as I do! Would definitely order another one!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[newborn, personalized_gift, gift, case],
        name="Birth Flower Jewelry Travel Case, Birth Month Flower Gift, Personalized Birthday Gift, Leather Jewelry Travel Case, Custom Jewelry Case",
        price="14.90",
        description="Personalized Jewelry Boxes, Birth Flower Jewelry Case, Travel Case For Bridesmaids, Minimal Jewelry Box, Jewelry Organizer, Jewelry Box"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/14c918/4184624086/il_794xN.4184624086_s698.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/14c918/4184624086/il_794xN.4184624086_s698.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/2fa402/4232282423/il_1588xN.4232282423_sffe.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/6ae3d6/4232282411/il_1588xN.4232282411_s250.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/fb63a6/4232282215/il_1588xN.4232282215_57p8.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/b93c56/4184622950/il_1588xN.4184622950_mbjb.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/b2ed6f/4184625188/il_1588xN.4184625188_fs8m.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/62d356/4184625114/il_1588xN.4184625114_o8ik.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/935548/4232285551/il_1588xN.4232285551_8083.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23702777/r/il/f6c098/4232281079/il_1588xN.4232281079_bw8q.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=3,
            review="Received purple. Asked for pink. Name looks like Liuz instead of Liz"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=4,
            review="Rarely got updates on the shipping end, which sucked. Took a little longer to get here than expected. But the boxes were great! Very cute on the outside and the inside is nice and soft material."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="These are beautiful! I purchased as a gift for my best friend and couldn’t resist buying one for myself too. The quality is nice and shipping was fast. I chose the color Rawhide. Would def buy again!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4,
            review="its so cute!! a bit smaller than i thought!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[child, gift, toy, personalized_gift],
        name="Baby Girl and Baby Boy Name Puzzle by BusyPuzzle, Christmas Gift For Kids, 1 Year Old Birthday Gift, Montessori Toys",
        price="1.99",
        description="· Name Puzzle from BusyPuzzle is the Best Personalized Wooden Gift for Kids ·"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/95b009/3398360096/il_794xN.3398360096_rpcp.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/5de389/3398348088/il_1588xN.3398348088_4jzk.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/4877ec/3398348092/il_1588xN.3398348092_1wcg.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/3791e1/3446014715/il_1588xN.3446014715_b4fg.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/f04819/3446014719/il_1588xN.3446014719_2xu9.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/d9f6ea/3454598673/il_1588xN.3454598673_9oh8.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/877d98/3398358046/il_1588xN.3398358046_eu55.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/9c85e8/3446025849/il_1588xN.3446025849_6sjx.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17305851/r/il/fc16a4/3398359014/il_1588xN.3398359014_bk4g.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="I was at a loss at what to get my nephew for his 1st birthday. And then I found this awesome seller with these beautiful puzzles. I paid the extra to get the pegs put on to make it easier for my nephew to use and it was perfect. Someone different and special to celebrate turning 1. Thank you for the lovely puzzle."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="They came out beautifully. I even received a few duplicate letters in glitter which I wasn't expecting but very happy about. They were packaged very securely. I love them. I'd certainly recommend to others."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4,
            review="OMG! I love this product. And my baby love it too. She started pulling out the letter.it looks great and quality is great. It just fit right in her room. We love it."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift, leather, boyfriend, gift],
        name="Personalized Flask for Men, Leather Flask, Flask Personalized, Flask Leather, Flasks",
        price="9.99",
        description="Personalized Leather Flask!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/824d8a/3906405268/il_794xN.3906405268_aubi.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/518070/3953900723/il_794xN.3953900723_fws4.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/a6f0ac/3953898647/il_794xN.3953898647_rypx.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/1606e5/3953897201/il_794xN.3953897201_e1gg.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/a471d4/2022380975/il_794xN.2022380975_m69x.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/55c6e1/1974823668/il_794xN.1974823668_js8r.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/af0949/2022381025/il_794xN.2022381025_bate.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/20811748/r/il/437abe/1974823536/il_75x75.1974823536_7wlu.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="So cute! Such good quality and the seller was so nice and responded quick! Great price also! I think all the groomsmen for our wedding will be very excited with these! :)"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Item looks great! Lettering was very well done. Picture of the Gray with Black flask is a little misleading, the picture looks more cream colored but the flask itself is more gray. That being said they still came out great"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Very nice, good size. I got the gray and plan to use it while out fox hunting. Nice quality for price and like the monogram!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="The day of my wedding, I gifted these flasks to my dad, groom and my brother. They were so surprised in the quality and really liked the flask. Well made and shipped before the expected date! Made great gifts!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[newborn, child, gift, personalized_gift, home_decor],
        name="Kids Night Light, Personalized Baby Gift, Woodland Nursery Decor, Custom Night Light Lamp, Gifts for Toddler Birthday Baby Shower, Christmas",
        price="34.50",
        description="The wooden night light provides a gentle, soft, and calming glow for kids of all ages to fight away monsters under the bed and make their sleep magical and sweet. With a nursery night light, it is easier to check on your kid at night to ensure s/he is peacefully asleep or to soothe a baby crying at night. The item is easy to use, colorful, and portable."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/7300a3/4437193987/il_794xN.4437193987_ff7j.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/14f758/4389803568/il_1588xN.4389803568_4xf0.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/3480b5/4411512246/il_1588xN.4411512246_m70u.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/e972a3/4411512230/il_1588xN.4411512230_5tui.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/07d214/4393774586/il_1588xN.4393774586_ph9k.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/c0847e/3654676157/il_1588xN.3654676157_2m6r.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/f7fc26/4441166869/il_1588xN.4441166869_2ott.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22537583/r/il/4f2e94/4437192209/il_1588xN.4437192209_bdig.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="The nightlight is exactly as described! I am so impressed at the quality and how beautiful they are! I bought them as Christmas presents so we haven't lighten them up yet but the craftsmanship is stunning! I love it! ❤️"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I ordered this while I was pregnant. I lost the baby at 20 weeks pregnant but the night light is going on our memory shelf. It’s so cute."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Gifted for my best friend's baby- they said it is absolutely perfect for diaper changes! Soft glow just enough for them to be able to get through the diaper change without having the baby totally wake up!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I LOVE this nightlight. The quality is amazing and I think it is so much better in real life than the pictures. I love the option of using a cord or batteries. The amount of light is gives is perfect. It’s a great addition to our woodlands nursery. My only wish was we bought two as the shipping is a lot to Aus."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[newborn, gift, personalized_gift, home_decor],
        name="Personalized Plexi Night Light with Little Prince - Nursery Decor - Le Petit Prince - Kids Room Decor - Personalized Gifts for Kids",
        price="36.99",
        description="Custom Baby Night Lights with Little Prince!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/b029b4/2847834009/il_794xN.2847834009_nd9k.jpg"),
            preview=True
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/059dba/3000942409/il_1588xN.3000942409_p8p2.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/f1c61d/3513343688/il_1588xN.3513343688_jnus.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/fb4d2f/2800157076/il_1588xN.2800157076_hsm7.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/2c53d5/2847838107/il_1588xN.2847838107_rxyx.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/ce50de/2847839301/il_1588xN.2847839301_oc9z.jpg"),
            preview=False
        ),

        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27235619/r/il/8cc9e3/2953230296/il_1588xN.2953230296_eq5s.jpg"),
            preview=False
        ),

        Review(
            buyer=bobbie,
            product=product,
            rating=5,
            review="I'm in love! This is, BY FAR, the most beautiful gift I've ever given myself. I am constantly showering myself with gifts (because who else knows what I like better than myself?!) and let me just say that this is next level gorgeous. I am an avid reader, and I love The Little Prince sooo much that my original copy has 70% of the pages falling out. So when I saw this light, I KNEW I must have it. I cannot stress enough how perfect it is. Even as good as the photos make this look, they do not do it justice, so imagine it about 10,000 times more amazing. I just got it, and honestly, I cannot tear my eyes away; I just keep staring at the whole thing. I am over the moon thrilled with this purchase and 100% satisfied with my care. Infinity % recommend. Synopsis: GET IT. I guarantee you will not be disappointed. It's truly lovely."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Super cute! It turned out better than I even expected. The personalization is such a great touch and I can’t wait to see it light up my nephews nursery for years to come!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Incredible buyer service, Ibrahim was so great to correspond with and made it really easy and efficient! And the product is sooooo beautiful. It makes the perfect nightlight for my daughter and also serves as really pretty decoration on her night stand. I HIGHLY recommend it, if you're on the fence just get it!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Absolutely gorgeous. The perfect addition to my themed nursery. And Ibrahim is also very responsive. Thanks again."
        ),
    ])

    db.session.commit()

    # order = Order(buyer_id=bobbie.id)
    # db.session.add_all([
    #     OrderDetail(
    #         seller_id=anna.id,
    #         price=product.price,
    #         product=product,
    #         order=order,
    #         buyer_id=bobbie.id,
    #         quantity=1
    #     )
    # ])

    # db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Personalized Leather Engraved Key Chain Key Ring with Wood Box Handsome Groomsmen, Corporate or Promotional Gift (024917)",
        price="8.59",
        description="These functional stylish key chains are a sure winner. With polished stainless steel accessories, this nifty key chain makes the perfect groomsmen gift, or corporate promotional gift. We can add about 4 lines of text and include an image (as long as the image isn't too complicated)."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8057725/r/il/41a291/757727885/il_794xN.757727885_9nnk.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="tech accessories"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="keychain for men"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4,
            review="personalized keychain for men"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Custom 10” Family Name Hand Embroidered Wall Hanging, Wreath, Wall Decor, Greenery, Brass Bells, Minimal, Christmas, Winter, Personalized",
        price="60.00",
        description="This beautiful minimal wall hanging is the perfect touch to your winter decor. It can be hung in your entryway, on the inside of a door, in the kitchen, by the fireplace... the options are endless."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23853452/r/il/e89522/2620894123/il_794xN.2620894123_oxii.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="seasonal decor"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="personalized holiday decor"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="last name embroidery hoop"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Christmas Gift for Him, Custom Leather Wallet, Personalized Wallet, Engraved Wallet, Gift For Boyfriend, Mens Wallet, Dad Birthday Gift",
        price="14.99",
        description="Anniversary Gift for Him, Custom Leather Wallet, Personalized Wallet, Engraved Wallet, Gift For Boyfriend, Mens Wallet, Dad Birthday Gift"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32404941/r/il/984a6e/3788291077/il_794xN.3788291077_enuv.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="It was perfect. I apologize for the profanity. It has been mine and my brothers little saying to each other for the longest time. He loved it and it turned out beautifully."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="This is my second purchase from this shop and once again I’m absolutely pleased! Everything came out beautifully and on time for Christmas!!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Got here sooo fast and was so pretty when i got it. I got it for my boyfriend for christmas and i know hes gonna love it."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Such great leatherwork. So artistic and great looking. I’m in love"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Personalized Gift for Dad from Daughter, Toiletry Bag Leather Men, Gift for Husband, Engraved Leather Dopp Kit, Christmas Gift for Husband",
        price="15.00",
        description="Our personalized Dopp kits are just what you are looking for. This is a perfect gift for your dad, husband, or any man in your life. The leather Toiletry bag has plenty of room for all his grooming supplies. And you can make it even more special by engraving his name on the kit!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/38065945/r/il/cb3273/4287587457/il_794xN.4287587457_jcw2.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Logo not as appears in listing. Much smaller. Would not purchase again. Posted picture of listing photo and mine under. Update: seller reached out and is working to correct it!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=2,
            review="Wonderful customer service! Absolutely amazing bags! I had bags made with a custom picture put on them. Every detail in the picture was on the bag. Great work!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="The seller was so kind as to send me a preview of the design. After seeing it I decided to change the design and the seller had no issues doing that for me. The bag is so nice, beautiful quality, and shipped very quickly! Thank you!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Leather Toiletry Bag"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Custom Royal Portrait from Photo | Renaissance Portrait | Custom Portrait | Human Portraits | Custom Man Woman Portrait |Historical Portrait",
        price="26.79",
        description="If you are a human portrait lover like us, you will find the best custom human portraits for you and you're loved ones! We are aware that when it comes to our special ones, everyone wants to get attention! Our main goal is to make each customer satisfied and happy with your portrait design! You will love the way our design team works along the process. We will provide numerous options to add your artwork! More Customization is available with different types of styles. Our designer team will work hard until you get the most astonishing artwork of you and your loved ones! We will send you the preview every time the changes are made and if you are not satisfied with it, you have an option to cancel your order!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/26335741/r/il/19e4ce/3162498762/il_794xN.3162498762_8ghk.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Absolutely love it. So did my friend. He was so amazed what you can do with a head shot. Arrived very quickly. Neatly packaged . I certainly made a good choice selecting this shop . Already planning my next purchase !!! Thank you Canvas Archive"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Met and exceeded my expectations for graphic editing abilities, quality, and turnaround times. I bought this as a gift for my brother. He and his wife loved it so much, they want portraits for the whole family!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I ordered one for my dad's birthday and he absolutely loved it! Quality is awesome and delivery was fast. This product definitely met my expectations. I am very happy. Thank you so much CanvasArchive for wonderful work and quick response to all my requests ! I will definitely order again."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Hands down the best gift I’ve ever given. My dad loved it and the whole family can’t stop talking about it. The perfect gift for that person in your life who is hard to buy for. 10/10 recommend."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Whiskey Sets Bourbon Decanter Set Gifts for Men Fathers Day Birthday Scotch Glasses Drinkware College Graduation Gift Engraved Monogram",
        price="9.98",
        description="This listing is for Customized Whiskey Rock Glasses Laser Engraved Personalized with Name and Initial."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/5703048/r/il/6c410e/2255509652/il_794xN.2255509652_dng4.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Second set we have purchased. O e for us and this one for a friend!! Great quality and shipping packaging!!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Absolutely gorgeous glasses, nice and heavy weight to them and beautiful engraving! My husband will love these!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I ordered glasses for my dad and they are beautiful! I needed a lot of help with the order because of my own error and they were patient, kind and super helpful! Will definitely order other items in the future! Customer service is amazing!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="It’s beautiful! Came well packaged and got here quicker than expected. The set of glasses and decanter are very nice. The etching is very well done"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Personalized Waxed Canvas Dopp Kit , Men's Shaving Dopp Kit , Large Makeup Bag , Travel Case Groomsmen , Unique Gift For Him Her",
        price="72.00",
        description="** ITEM PROCESSING TIME IS 4-6 WEEKS"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/9696294/r/il/ac0ff4/3114605483/il_794xN.3114605483_giix.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="personalized gifts"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="accessories"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="personalized gifts for him"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="custom phrase mug . funny mug . christmas gift . surprise gift . personalized mug . bottom of the mug . inside the mug phrase",
        price="20.00",
        description="An all white, 13 oz. ceramic mug with a hand painted phrase placed on the inside bottom, inside rim or outside of the mug. A fun gift and surprising way to start the morning. Surprise someone with a proposal, announcement, inside joke, or personal sentiment. Leave your specific phrases in the personalization box and where you'd like it placed on the mug (OR just leave it blank for the “poisoned” message.) GENTLY HAND WASH- NO SCRUBBING."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8026669/r/il/cabbf2/4378368846/il_794xN.4378368846_74to.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="mugs custom phrase mug . white m..."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="mugs mugs"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="custom mug"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Personalized Cheese Board, Personalized Cutting Board, Christmas Gifts, Gifts For Men, Gifts For Women, Closing Gift, Gift For Her, Husband",
        price="39.32",
        description="Our personalized cheese boards, like our cutting boards, are made from multiple strips of premium wood that are edge glued and sanded for lasting strength and beauty. Not only are our home goods functional kitchen tools but they are the perfect heartfelt gift to commemorate any occasion. SHOWN IN HARD MAPLE"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8503074/r/il/22598d/1048352440/il_794xN.1048352440_ebp2.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="gift for the home"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=4,
            review="gift for the home christmas"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="gift for the home wood signs"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[personalized_gift],
        name="Mother's Day Gift - Handwriting Bracelet, Children's Actual Handwriting, Engraved Cuff Bracelet, Custom Bangle, Handwriting Gift, Medium HND",
        price="42.50",
        description="Our custom Handwriting Cuff Bracelet is made from actual children's handwriting, handwriting from grandparents, parents, and loved ones from cards and documents. All we need is a photo of the writing - phone photos work great! Cuff measures 3/8' wide made with the highest quality stainless steel materials with a glossy mirror finish, or brushed satin finish. Packaged in our Tom Design logo-stamped gift boxes with optional gift wrap."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/5395361/r/il/592588/1458870688/il_794xN.1458870688_b6l5.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="personalized jewelry"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="personalized jewelry for mom"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="personalized jewelry for her"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Let Love Grow- Custom Seed Wedding Favors Personalized SEALED with SEEDS INCLUDED, Wedding Favors, Elegant Wedding Favors, Florals, Favors",
        price="10.00",
        description="*If you would like to order your packets without seeds they are $1 per packet. Message us for a custom listing*"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/10627719/r/il/baafa1/2270730350/il_794xN.2270730350_4zud.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Got to me on time and were so cute!!! Gave them out at our engagement party with our wedding date on them. What a gorgeous lil favor!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I love these! I couldn’t find the proper sized pot, but hot glueing the packages to popsicle sticks worked really well. These are going to make perfect favors."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Yes everyone loved them such a beautiful thing to add to our thank you bags."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="These were the most perfect favour - our guests loved them and they came packaged so well, very elegant. Would order again!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Set of 2 - Champagne Flutes Personalized, Wedding Gifts, Mr and Mrs Champagne Glasses, Toasting Flutes for Couples - Bride and Groom",
        price="29.95",
        description="Set of 2 - Wedding Champagne Flutes, Mr. and Mrs. Champagne Glasses, Wedding Gifts for Couples, Toasting Flutes"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/14466987/r/il/40ede1/2584790379/il_794xN.2584790379_pwyg.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="These were great for my champagne toast during the cake cutting at my wedding! The product came in very quickly!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="We love our wedding champagne glasses! Packaged perfectly in a box! We could not be happier with how they turned out!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="These are extremely high quality. The weight of the glasses are perfect and the seller worked with me to get a custom message put on them. Highly reccomend."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="They are beautiful I can't wait for our wedding day to drink out of them!!!!!! It looked just like the photo and is made great comes in a very good padded box!!!!!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Mother of the Bride Gift & Father of the Bride Gift from the Bride, Mother of Bride Gift, wedding handkerchief from daughter - POB-POG",
        price="18.80",
        description="Mommy, it's happening! Your little girl has found a man and he's going to marry her! They're planning a wedding soon, and we want you to make that day extra special. From the bride...with love!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/11936504/r/il/00119a/4437647866/il_794xN.4437647866_scem.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I bought one for my mom and dad to gift to them on wedding day and their reaction was priceless! I’m so glad I got one for the both of them. The one for my mom was in Spanish. The quality is good and arrived fast. My dad kept showing it off to guests as he thought it was such a beautiful gift. Both of my parents cried when they read the message and I’m happy they have something to remember my wedding and how much I love them."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="These turned out so pretty! I did a custom note and was so pleased with the outcome. Shipped quickly. So excited to gift these to my parents on my wedding day."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I gifted this to my parents & to my In laws and everyone cried! It was such a sweet gift that they will cherish forever. Beautiful package and work done!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="My parents loved these and it created such a sweet moment at my wedding. Thank you!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Vintage style Pearl cluster earrings Crystal bridal earrings Simple marquise star earrings Rhinestone earrings Wedding jewelry for Brides",
        price="65.00",
        description="A brilliant combination of the finest European crystal and crystal pearl create this modern take on a classic look! The rhinestone marquise stones fan out from the cabochon pearl to give this bridal earring elegant style and simple sophistication."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/10677293/r/il/f5c02c/1391204021/il_794xN.1391204021_cbux.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Loved the design! The pearl and crystal combination was perfect with my wedding gown!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Absolutely beautiful! Shipped so quickly and came in the most amazing handcrafted box! I can't wait to wear these on my wedding day!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="These are so pretty! They are not heavy and don’t make your ears droopy. I love them and can’t wait to wear on my big day!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Absolutely beautiful!!! Came in a darling little box too. Thank you so much! Will ad a photo after my daughters wedding."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Personalized leather photo album, free shipping, leather scrapbook, junk journal, anniversary, wedding, baby album scrapbook",
        price="29.59",
        description="Handmade item, with high quality genuine top-grain leather"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/12712405/r/il/d7040c/1847147403/il_794xN.1847147403_fr4e.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I am absolutely in love with this little photo album. I wanted to do something really special with wedding photos for my family for Christmas and this was the perfect gift! It turned out so amazing. I can’t wait to order one for myself."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I CANT RECOMMEND THIS ENOUGH!! It may be a little more work putting in the photo sleeves or stickers yourself but it's worth it. Good things take effort and it will be worth it. As I add pictures it doesn't stretch the spine or look over filled because that was planned into it. It's so unique when it comes to photo books, I looked for days and only found this for the kind of look we want on our book shelf and to take out and show family/our kids. Its great quality and I have no doubt it will last:)"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Better than expected! Great purchase! This is quality leather and the name is professionally printed. The photo album worked well with old photos of my great grandmother. The item was shipped and arrived as promised in time for my mother’s 70th birthday. This seller is great to work with!!!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=3,
            review="The quality of this journal was nice, but to call it a photo album seems to me a misnomer. There is no way to attach or insert photos, but rather blank pages. I'd definitely not have purchased this had I known that. I'd suggest calling it something else or being very transparent about the fact that there is no actual way to insert photos. Thanks - Tracy"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Monto - Australian Native flower Men's Buttonhole / Boutonniere. Wattle, blue Geraldton wax flower and gumnuts.",
        price="17.17",
        description="Monto is a big splash of Australian colour in a buttonhole. Bright yellow wattle flower, sparkling blue Geraldton wax and bright green gumnuts surrounded by soft grey native foliages."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/6383615/r/il/97adca/900068619/il_794xN.900068619_pmzs.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="This was purchased for my husband to be, to wear on our wedding day, and I adore it! I can’t wait to see it in action, but my initial impressions are that it’s light and beautifully made! Thank you!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Love this very Australian very pretty thanks guys"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Beautiful. Karen was helpful and accomodating with my requests. Definitely recommended!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Very beautiful, delivered very fast also. Thank you"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Beauty and the Beast Bracelet Rose Charm Bracelet Bridesmaid Gifts Birthday Gift Belle Costume Wedding Jewelry Personalized Initial -3MRBR",
        price="11.50",
        description="Beauty and the Beast Bracelet Rose Charm Bracelet Bridesmaid Gifts Birthday Gift Belle Costume Wedding Jewelry Personalized Initial"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/10158348/r/il/b95792/4400761752/il_794xN.4400761752_447e.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Such a beautiful piece!! It was my second time ordering. I got a rose gold first and ended up loving it and wanting the gold version! I’m obsessed!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="So so cute! Looks exactly like the picture. Fast shipping!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Such a beautiful product. I love it!! The shipping was lightning fast! I ordered this on Thursday and it was shipped the next day and delivered to me by Saturday!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="It was shipped out really fast and the quality and looks were really well done. im so happy with it!!!!!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Personalized wedding place table cards Laser cut names Guest names Weddings place cards Laser cut name signs Place settings Bride and Groom",
        price="1.05",
        description="Personalized wedding place cards."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/10797415/r/il/958742/1164600927/il_794xN.1164600927_idts.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Amazing quality, I almost cried when I saw these nameplates!!!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="The names are so lovely and they arrived so quickly! I am thrilled with this purchase and really appreciate the quickness of the shop on getting them to me."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="They came out amazing! They are so delicate and cute. Going to make for a nice simple detail!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Loved these little name tags. Perfect little touch for my wedding"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Rustic Wedding Cake Server Set & Knife Cake Cutting Set Wedding Cake Knife Set Wedding Cake Servers Wedding Cake Cutter Cake Decoration",
        price="49.99",
        description="Rustic Wedding Cake Server Set & Knife Cake Cutting Set Wedding Cake Knife Set Wedding Cake Servers Wedding Cake Cutter Cake Decoration"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8931561/r/il/41b247/1708909197/il_794xN.1708909197_t7zj.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=4,
            review="These turned out to be SO cute! I went with the sage green and it was perfect for my color scheme. One thing is that I noticed the quality of the stainless still was a bit iffy. The scratches aren’t a big deal but I did see a good size flaw on the back side of one of them. I’ll put a photo. Other than that, they’re great! The scratches you can’t see from far away so I really don’t mind. Just thought I’d note it for anyone else!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="SUPER SUPER CUTE CAKE CUTTING SET and it perfectly fits our rustic white barn theme :) I am SOOO in love and can't wait to use them to cut our cake in a month from today!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="My set came out so perfect!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Absolutely love them!!!! Beautiful! They're even more beautiful than in the picture! So happy with my purchase! Great quality!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[wedding],
        name="Rainbow Paper Flower Bouquet, Colorful Paper Flowers",
        price="27.00",
        description="This beautiful rainbow paper flower bouquet encompasses a variety of bright and colorful roses made from high quality card stock paper. They make a great pop of color in your ceremony and a keepsake in the house as a conversation piece or table arrangement. They’re also the perfect gift for any occasion; birthdays, Anniversaries, Showers, or simply just because. Handmade in the USA!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/11935929/r/il/2d9e82/1265469165/il_794xN.1265469165_abzk.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Very pleased! Just as described. Perfect 1st Anniversary gift. Speedy turn around and shipped safely. Thanks so much."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="These turned out so adorable and shipped so quickly!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="These turned out so adorable and shipped so quickly!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Rainbow Flowers"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Japan Art Matsumoto Hoji frog Sad Frog art print Japanese woodblock reproduction Ugly cute toad Print Wabi sabi wall art frog painting",
        price="17.45",
        description="Get 60% discount when you buy 6 (or more) prints at our store. Discount shown at checkout."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/10533774/r/il/717449/3262011801/il_794xN.3262011801_d3re.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Unfortunately, my package seemed to got lost on the way - but the shop owner Sintija was very accomodating! The package showed up eventually and the quality of the print is just as good as the customer service. I ordered the print in a very large size. Ordering prints in that size is always risky because most of them don‘t have a good quality because of the scaling, but this one marked every box. I love it and it earned it‘s place right above my bed, in my favorite frame. That‘s the highest honor a print can earn in my house."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Fantastic print- exactly as pictured- brilliantly vibrant with good quality ink and durable, high quality paper. What’s more- when my dog ate the first print when posted through our post box- the seller send ANOTHER completely free of charge- including free international shipping. He really went above and beyond with his generosity and customer service. I can’t recommend highly enough!!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=3,
            review="First of all: a super nice customer service (fast response and very accommodating), unfortunately the first package got lost on the way from France, but I was immediately sent a new one at no extra charge, unfortunately it was damaged during shipping and the pictures arrived slightly kinked at the edge - otherwise really nice pictures and good quality😊"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="very great quality and print. arrived on time, estimated delivery was the 24th and i got it today, the 26th."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Whale Painting, Watercolor Painting, Whale Print, Whale and Boat, Whale Art, Whale Nursery, Humpback Whale, Print titled, \"Fathoms Below\"",
        price="10.20",
        description="This is a fine art giclée print made from my original watercolor painting titled 'Fathoms Below'."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8585009/r/il/18ea08/1207942531/il_794xN.1207942531_78qo.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I love these! We combined the whale and the manta for our hall, and the atmosphere is so much better. We got arctic matte as paper, the quality is superb, but our frame is a bit shiny, so that's why it seems that way on the photo. To get it fit in our frames, we got passepartouts additionally, I am very happy with the result. Big recommendation!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="This is one of my favorite pictures in my room now. It’s literally beautiful and I’m so happy with this purchase!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Another beautiful print in the collection I purchased! I found a complimentary mat and frame that will enhance this artwork even more. I am very pleased with this print and how quickly and safely it arrived to me!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="smaller than I thought but that mistake was mine. The picture is gorgeous and I love it. It's going in my young grandson's room. I know he will love looking at it."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Botanical Print Set of 4 - Botanical Illustration - Botanical Art Print - Art Prints - Vintage Botanical Print Set of 4 - Botanical Poster",
        price="38.00",
        description="This is for a set of 4 prints of a Botanical Floral illustration that has been hand painted and were found in an Antique natural history text book. The original has been digitally enhanced and are printed on heavy matte photo paper."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/12324116/r/il/8c7815/4325208654/il_794xN.4325208654_ppzn.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Prints were well packaged and good quality. The enhanced colors are a little uncanny up close but look great and vibrant when displayed on the wall."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="The prints arrived quickly, the colors are as pictured on Etsy. The prints are a great addition to my dining space."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="These prints are beautiful! A perfect addition to our walls."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Fabulous! Framed in black over my bed. Plan to have the current glass changed to anti-glare glass to enhance these lovely prints."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Cardinal Candle Holder - Hand Made In Ukraine - Blown Glass - Hand Painted - Cardinal On Frosted Glass",
        price="14.95",
        description="Old world craftsmanship comes to life in these elegant, hand painted, Cardinal candle holders. These charming mouth blown glass candle holders are a great addition to any home. Both beautiful and symbolic, the Cardinal candle holder is a unique gift for your loved ones that they will cherish forever."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/19998115/r/il/f39930/2158794765/il_794xN.2158794765_a9n5.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="The cardinal candle holder is so beautiful! The colors are vibrant and I love the design. It is a lovely reminder of lost loved ones. The package arrived so quickly and it is extra special that it is made in Ukraine. Thank you!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="This candleholder is so beautiful, I love it! Smaller than expected but that’s on me because I didn’t read the specs. It’s perfect!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Absolutely beautiful candle!!Artwork is superb ! Customer service awesome! Highly recommend!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I had this beautiful candle holder sent to a dear friend who loves cardinals. She loves it!!! She said that the seller hand wrote my note to her. She said the gift and the note made her smile. Thank you for putting a smile on her face and taking great care in sending it to her! Shipping was very fast too!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Monarch butterfly stained glass window hangings Christmas gifts Fairy garden decor Custom stained glass butterfly suncatcher",
        price="54.90",
        description="You've never seen such a beautiful monarch butterfly in your life 🙈 Just imagine how you are wandering through the valley full of wildflowers and butterflies 🌼 I am sure it has already caught your attention 😉 Capture the endless summer in your house with this monarch stained glass window hanging. Besides, it may be a fairy garden decor too 🏡"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/16555624/r/il/7bb5e7/4407431844/il_794xN.4407431844_27eu.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="The monarch handmade glass butterfly is even more beautiful than I imagined before seeing it in person. The colors, workmanship, and artistry is excellent. Ivan of GlassArtStories is wonderful to work with as he contacted me before starting the work to make sure he was making exactly what I wanted, and to thank me for choosing to do business with his shop, which I in turn appreciated as well. Based on the product I bought, and received I’d recommend the variety of beautiful artwork presented, and handmade by Ivan on his website to anyone for purchase. I know you will love his products as much as I do. Thank you Ivan, and staff. #Support Ukraine, and all Ukrainians."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I have a small collection of stained glass sun catchers and this one is by far the most beautiful!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Ivan did an awesome job on making my monarch butterfly. I love it. The colors and detail are beautiful. He packaged it well and boxed it. I like the size if it The leaf on the stem adds a nice touch. I'm glad I found his shop. He offers so many beautiful stained glass items. Plus he is a pleasure to communicate with. I would recommend his shop. You won't be disappointed."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I wrote a review of another sun catcher which is a beautiful blue bird. The monarch butterfly is stunning and the quality is beautiful. I’m looking forward to buying more pieces in the future. Shipping wasn’t bad considering it comes from the Ukraine. Packaging was great too! Thank you!"
        ),
    ])

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Wedding Gift, Wedding Gifts, Personalized Pillow, Newlywed Gift, Engagement Gift, Rustic Wedding Gift, Linen Pillow, Gift for bride",
        price="24.00",
        description="CYBER MONDAY SALE GOING ON NOW!!! 25% OFF OR SIGN UP FOR OUR INSIDER'S CLUB FOR 30% OFF"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/7384426/r/il/10a116/4294165579/il_794xN.4294165579_acag.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I received my pillow in less than a week. The pillow is beautiful, and shipping was fast. I would definitely recommend placing an order. 🤍"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Best customer service, ordered one day and received it 4 days later! Beautiful work! This was the 4th item I have ordered from Willow Creek and always happy with the results!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Item turned out great and was an awesome git for my newlywed pals. :) They loved it and so happy with how the pillow turned out!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="It's beautiful and exactly what I wanted! The seller responded to me very quickly and it shipped very quickly. Loooove it!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Nursery Name Sign, Nursery Decor, Nursery Wall Art, Wooden Name Sign, Name Sign for Nursery, Woodland Nursery Decor, Woodland Wooden Letters",
        price="20.95",
        description="The price of the listing is for INDIVIDUAL LETTERS. (ie. If ordering for the name EMILY you would add a quantity of 5 letters to the cart). Please include the desired name & font choice in the personalization box. If no font is specified Arial will be used."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/8815198/r/il/38546c/2437884391/il_794xN.2437884391_6d5h.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Communication with seller was great. My package went missing off my pouch and the seller tried their best to help. I was lucky enough that a few days later my package reappeared (I just they realized they would have no use for a personalized letters, lol). Beautiful work! Love how the nursery looks with his name about the crib!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I absolutely love them! It's a great addition to my nephew's room. The wait is definitely worth it. You can tell how much hard work and attention to detail is put into each lettering. So very pleased!!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="We absolutely are in love with the way that these turned out for our little man’s nursery! They are the finishing touch. Thank you so much, and I would totally recommend this store."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="So cute! She did such a good job, it exceeded my expectations! Was perfect for the woodland theme of our sons room. I had requested specific animals and it was just as I asked for !"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Palestine Sheep Wool Table Top Nativity Scene & Trees Set",
        price="135.00",
        description="* Set of wool nativity scene and christmas trees"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/18758094/r/il/f99ce1/4253097582/il_794xN.4253097582_kfqz.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I try hard to buy through the Fair Trade from around the world. This Nativity was even cooler than it looked. I have it in my curio cabinet!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Dear Holidays"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Israel"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Nativity Figurines"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="SUPER HUGE Jumbo Rustic 12\" Decorative Clothespin in Walnut Finish, Photo Note Holder for Home Office, Kids Drawing Display, Bathroom Hooks",
        price="28.00",
        description="What a unique and fun way to hang your towels in your bathroom or laundry room. Can also be a fun way to display photos, kids drawings, or notes in your home, nursery or office with a large rustic decorative walnut stained clothespin."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/10462935/r/il/34db35/4298852076/il_794xN.4298852076_pqqz.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="LOVE this! So cute but small! I don't know why I was thinking it would be bigger. I put a picture of my kids, when they were very little, clipped in it. It just looks perfect in my bathroom in the one little space I had."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Thought they were smaller than expected but was happy with their size once they were all set up. Good grip, nice finish, great quality! Shown in photo: Super Huge Jumbo size, with weathered oak stain."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Absolutely love them!! Excited to add them to my bathroom project!!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4,
            review="So cute!!! The only draw back is it took a month to get to my house, so I don’t think I would order again. But very very cute!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[home_decor],
        name="Knife Abstract art,Acrylic paintings on canvas,Landscape Colorful Forest Painting,Bedroom Wall Decor,Textured Impasto Painting,painting gift",
        price="99.20",
        description="Abstract Painting on Canvas, Original Art, Modern Art, Landscape Art, Abstract Art, Textured Wall Art, Wall Decor Living Room, Impasto Art abstract art canvas original Knife Abstract Art"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/6624893/r/il/62da02/4419545477/il_794xN.4419545477_5mso.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="LOVE LOVE LOVE this painting! It arrived very timely and it's beautiful; very high quality, and exceeded my high expectations! It's already displayed on the mantle and bringing a much needed pop of color to the family room! I'll definitely look to purchase additional art from Xiangwuchen for other rooms in the house."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="What an amazing art piece created by Chen! Loved every bit of it, and this is currently hanging pretty on our living room wall. It shipped on time, Chen was super responsive, and we were able to track our shipment. Chen, hope you keep creating these amazing paintings! Cheers"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="It looks much better in real life then on photo! A very eye-catching piece, I receive a lot of compliments on it. We have it in our breakfast nook/kitchen and it’s a true pleasure to see it every day. Highly recommend!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="LOVE this artwork! The colors are so vibrant and the piece is amazing. It’s a statement piece in my office. Size was true to specs. It’s an actual painting, not a print. It’s beautiful!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Toy Bow and Arrow Set - For All Ages: Kids to Adults - Bow and Arrow for Kids, Kids Bow and Arrow, Archery, Bow and Arrow Toy",
        price="25.50",
        description="Handmade, custom Toy Bow and Arrow kit for all ages."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/25823893/r/il/9550c1/3673765573/il_794xN.3673765573_s8qy.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="This bow was exactly what I was looking for, and made my grandson very happy, the colourful arrow tips look like golf balls, but are super soft, perfect for a kid to learn how to handle a bow ! Great product !"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I had this shipped to my sisters house for my nephews birthday & he loves it! His parents even had some fun with it while he was at school. The shop owners are also awesome! First I put my gift message in the ‘note to seller’ section by mistake & they still printed the message out for me & put it inside of the package. Then I ran into a problem with shipping (my fault) & they were super helpful with getting it resolved quickly. I would definitely buy from them again!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Christmas gift for my son, came very quickly, nicely made. My husband and I played around with it upon arrival. Very excited for our son to open this item. A nice hand written note on our order was a nice touch!!!!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Shipped super fast and great quality! Love it for little kids!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Personalized Wooden Handmade Music Box,Christmas Music Box,Wooden Horse Musical Carousel,Horse Music Box, Musical Carousel,Heirloom Carousel",
        price="34.31",
        description="Personalized Wooden Handmade Music Box,Christmas Music Box,Wooden Horse Musical Carousel,Horse Music Box, Musical Carousel,Heirloom Carousel"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/38145326/r/il/43d06c/4380917599/il_794xN.4380917599_oqhq.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Absolutely beautiful! The craftsmanship is remarkable. So happy with purchase! Bought for my new granddaughter so hoping it will be a treasure for her as she gets older."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="LOVE! We got the carousel for our son's first Christmas, and it is absolutely adorable. Beautifully made, incredible talent. Highly recommend!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=2,
            review="Item came not working and the top part of the carousel was loose and crooked. There is also glue residue all over the joints of the product where it looks hastily assembled. I was able to fix the loose top part and now it looks fine, except for all of the glue residue. Not a bad product for the price, but I was expecting more than a glued together pre-fab music box. Not too great, not too bad."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Better than the pictures! It’s absolutely stunning. Can’t stop looking at it."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Drylands Board Game - Two Player Abstract Game Set in Africa - Beautiful Hand Drawn Art - Ages 5 and Up - Nature Themed Science Game",
        price="34.00",
        description="Our new game “Drylands” is now available!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22868680/r/il/eca102/4423387730/il_794xN.4423387730_rfp9.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I got this as a gift for someone. I can’t wait to play it. The illustrations are so beautiful!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Our all time FAVORITE game! We have purchased every edition for our own collection and really enjoy our Ecologies nights! This is also a go-to gift! We love spreading the Ecologies love by gifting for weddings, holidays, birthdays, and even White Elephant parties! 10/10!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="These cards are gorgeous. Far and away better than I even expected."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Disclaimer: As with all children's products, adult supervision is required. Products that contain small parts may pose a choking hazard and should not be used by children under 3. Sellers are responsible for following applicable laws and regulations, including posting items with accurate labeling and warnings. Etsy assumes no responsibility for the accuracy, labeling, or content of sellers' listings and products. Always read labels, warnings, directions and other information provided with the product before using it. If you have any questions, message the seller. See Etsy's Terms of Use for more information."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Safecracker 40 Math Puzzle",
        price="24.00",
        description="Fantastic and unique puzzle based on a 1911 design. The object is to get each of the 16 columns of numbers to add to 40 at the same time. Can you find the combination?"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/6191225/r/il/7ce851/2292691349/il_794xN.2292691349_9lju.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="This item looks exactly as pictured. I was very pleased when I received it. I have it 3 stars for shipping only because I was surprised I had to pay for shipping on each one individually. I ordered three and had to pay separate shipping on each, even though it was all shipped in the same box."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I cannot for the life of me measure the challenge presented by this here puzzle - suffice to say I cannot afford to have my brain melt in this day and age. But I can vouch for the high quality of workmanship, the swift and unimpeachable time in which it arrived, and the care that was provided in delivering this puzzle. Surely, this is a craftsman who is worthy of your business."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Love this! It is beautiful and so well done. I haven't tried it since it is a gift. Definitely will purchase other items from this shop."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I can’t believe that the shipment is here already…..ordered Wednesday and delivered Friday. The puzzle is very well made and I know my son will love it. Very impressed with with this seller"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Montessori toys, human body puzzle, toddler toys wooden human puzzle kids anatomy puzzle human anatomy preschool anatomy gifts for kids toys",
        price="39.32",
        description="The main goal of our shop EcoBabyPuzzle is to create wonderful educational toys for kids and make the process of learning more interesting and fun. We’re very proud of our quality wooden puzzles that motivate children to explore the world around them and learn more about themselves."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32753543/r/il/8c72f6/3842617767/il_794xN.3842617767_gft1.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Love love love! I am so impressed with the quality of the two puzzles I received from this shop. The shipping was really fast too! My son absolutely loved them and started playing with them as soon as we opened the package. I will buy from this seller again!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Love the puzzle and my interactions with the seller have so far been great! They are super helpful at getting me extra pieces!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="The item is a wonderful learning puzzle. It is what I expected. I do think it is very overpriced. I knew it was when I ordered, but my daughter wanted it for her little girl so I bought it. I even got it for half price, but by the time I paid shipping, it was almost $50. That’s just way too much for a small puzzle."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="It is for a Christmas gift! My kiddo is obsessed with learning body parts! She should love this"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Ready to Ship - Natural Wood Toddler Sized Bowling Set Christmas Toy",
        price="30.00",
        description="Our Wooden 10 Pin Bowling Set is a MUST for any little kid."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/6005933/r/il/1afc76/692697609/il_794xN.692697609_khof.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="This set is SO PRECIOUS!!! I got it for a toddler for Christmas and admittedly did not read the description clearly enough to know the size to expect… but I was so pleasantly delighted by this set when it arrived. The pins are beautifully made and the little bowling ball is adorable and the whole thing comes in a wonderful bag. I could not be happier and I can’t recommend these enough. I know a small kiddo who is going to think this is the greatest thing ever. And the shipping was super fast! I would absolutely buy from this shop again!!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I bought these for my nephew's birthday and my brother just called to tell me they are his favorite gift! He is picky! What make these such a hot item is that the kids like to play with them, and in years to come they will make great handmade antiques. Thanks for the card you threw in and making Zach (and his sister) so happy!!!!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Love it! No splinters!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Perfect! Was a hit at the birthday party"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Handmade in USA, Montessori Balance board for kids, Wobble Board, Award-winning Open-ended design - Bunny Hopkins",
        price="56.00",
        description="The Bunny Hopkins™ Wobble Board is an International Award-winning Open-ended Wooden toy."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/22270458/r/il/2cf3d4/4467928587/il_794xN.4467928587_2njg.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Love it! My 2 year old loves it, too! Been using it to roll our cars down exclaiming, “Hoovay!” (aka “hooray” in toddler speak). Our stuffed friends and the 2 year old also use it as a slide. Excellent craftsmanship! Beautifully sanded— I got it unfinished. I may apply a coat of finish for durability purposes, but it’s sanded so well that it is smooth enough as is without being too slippery for the kiddo. I have one questionable situation that I will need to evaluate over time: I thought I heard a slight crack whilst my 138 lbs. was balancing on it— like the ply board split. It looks fine, so I hopefully it was just some crumbs underneath or something. Not sure my 200+ lbs. hubby should use it, though. Glad I purchased from here instead of Amazon. It really is a beautiful piece of wood with so many possibilities!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="We were so stoked about this purchase for our little one since she just turned a year old. We decided on the smaller version as she’s never used one before and we expected for it to take some time for her to get the hang of. To our surprise she actually rocks it and uses it ALL the time, and now we’re planning on ordering the larger one! The finish on this product is insanely beautiful and the quality is absolutely phenomenal. I have no concerns for safety issues and it seems to be quite durable. Overall we’re very pleased with this purchase and intend to make future purchases with this seller. Thank you so much for your efforts and amazing customer service!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Got the item in 2 days! Mind you, I'm only 6hrs away but that is insane! Amazon Prime doesn't even get me goods that quickly. The board arrived safely and is perfect. No unevenness in coloring, no rough edges. It's a great, reliable weight though still light enough for my 1.5yr old to flip and move. Will definitely buy the larger board if she ends up using this one enough!!!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Beautifully made, sturdy beyond belief, and has been a huge hit with our tiny gymnast. The rainbow stripes are bright and fun without being garish. We’ll keep this for ages."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Talking Cactus with Hat Toy Rechargeable Upgraded Version Toy Singing, Recording, and Repeating What You Say with 120 Songs and LED Lighting",
        price="12.45",
        description="Perfect Gift for Kids over 3 Years Old"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/23795241/r/il/684f5e/4245323807/il_794xN.4245323807_7ubv.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="This item is exactly as I expected. Our lab and cats love it! Really funny to watch them interact with it!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=1,
            review="The boxes they came in were crushed.😢 They were supposed to be gifts for my Grandkids."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Brilliant, made me laugh straight away Thank you for speedy delivery too"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4,
            review="Missing adapter contacted seller Disapointed"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Rivajam Nature Scavenger Hunt Games for Kids, Toddlers & Family Fun | Outdoor Toys and Treasure Hunt Family Games | Backyard Camping Games",
        price="25.99",
        description="Rivajam’s Roll & Seek Nature Scavenger Hunt dice game helps children engage in conversation and increase their awareness of the wondrous natural world around them. They learn to observe small details, identify shapes and colors, ask thought-provoking questions, and most importantly, share the excitement of discovery with their friends."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/24029016/r/il/158033/3447328824/il_794xN.3447328824_6ex0.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Perfect! Bought these for my niece and nephew to use while camping. Exactly as pictured. The foam looks durable and easy to wipe off any dirt or mud. Quick shipping."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=4,
            review="This is such a fun and educational idea for outdoor play. The only reason I left off one star is because the print was faded on a couple blocks. Otherwise, it’s great!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Fun and very useful teaching tool. Only reason quality is a four is that I don’t know how well the dice will hold up. As far as customer service, I put the wrong shipping address in, then emailed the seller hoping to correct it, and the response was immediate and they fixed it. Shipping time was incredibly fast, too. Thank you!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="This was the 2nd time I bought this for a gift. This time for a cousin's 3 year old. She recently texted me and said that of all the gifts her son received for his birthday, THIS gift was the most played with. He has an older brother and sister and they all love playing it together!!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[toy],
        name="Large Musical Marble Tree| Visual Tracking Skills Toy| High Quality Wooden Toy",
        price="54.00",
        description="**SHIPPING UPDATE 12/11/22** This specific item need 1 week of processing and we will ship it out according to the processing timeframe shown at checkout. Thank you all for your support and attention!**"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/14382159/r/il/8a6969/4380591413/il_794xN.4380591413_pxyh.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="This is a beautiful piece!! Larger than I thought. Almost 3 ft. The sounds are lovely! I’m curious how my kids like it but I anticipate it being a favorite! Also I’m so glad there are so many marbles… less chances of fighting for a turn. Beautiful. Thanks you!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Absolutely gorgeous!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="My daughter in law was pretty impressed when I picked this one out! A handcrafted toy for our 3 years old and 9 month old grandchildren. We cannot wait til they open it on Christmas day!!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Beautiful toys! I am so excited to give these to my 2 year old for his birthday. They're excellent quality. Shipping was incredibly fast as well."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[bag],
        name="Briefcase for women, brown briefcase for laptop, 13 inches tote bag, strap tote bag for women, leather briefcase with compartment for laptop",
        price="134.00",
        description="Elegantly designed, Adele laptop bag is a true implementation of fashion and convenience. We made every effort to create the most functional design for maximum comfort. An outer pocket for small things has a simple design and reliable closure. Short handles that are also made of genuine leather are dense and could handle heavy things for sure. An optional shoulder strap is available to make the bag more versatile."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/31475762/r/il/fd23fc/3446078359/il_794xN.3446078359_ezvx.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="This bag is beautiful! The leather, the color of the brown, the personalization was an added bonus! The communication with DiOleBags was immediate and the shipping time was fast! I would highly recommend these products. You can't beat the price for the quality! Thanks so much DiOleBags!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Great quality! Genuine feel/leather and great structure!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="So pleased to hear it. Hope to see you in our shop again :)"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=2,
            review="Excellent product! Will enjoy using my new case!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[bag],
        name="Large Capacity Canvas Cotton Bags, Canvas Cotton Tote Bags, Canvas Crossbody Bags ,Canvas Shoulder Bags, Canvas Handbag, Class Book",
        price="21.39",
        description="★★Fast Shipping: Shipping within 24 hours"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/32518999/r/il/65b6bf/3660014160/il_794xN.3660014160_bx3r.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Very nice bag! Good quality and I've been taking it to class with me, it fits multiple notebooks, my pencil case, my laptop and my water bottle (its relatively small) and a few other miscellaneous items - the extra straps are super useful and I'm very glad i got it!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="So awesome! It looks exactly like all of the pictures. It's spacious, convenient, and I love it so much!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4,
            review="Really excited about this bag. My purse has not been large enough for the amount of notebooks I now carry. This is large and sturdy without looking like a backpack. My only wish is for a few more pockets on the inside to organize small things away from the larger books. Otherwise, super cute and I've received several compliments. Went outside my normal zone and got the yellow and it's very understated and adorable!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I LOVE this bag! 1st day & I already got compliments on it. Great quality, bright color, & the magnet snaps on it work great!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[boyfriend],
        name="Personalized PS5 and Xbox Controller and Headphone Stand, Graduation Gift for Him, Gamer Room Decor, Headset Stand, Boyfriend Gift Teen Gift",
        price="92.45",
        description="The Personalized Wooden Controller Stand is a versatile desk organizer. A stand where you can put your controllers."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27005739/r/il/77842b/3751624698/il_794xN.3751624698_cwve.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="It's perfect ! I am obsessed!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="It arrived in such a timely manner, almost within the week! And it smelled of fresh wood, very lovely. The quality is pretty great from what I can tell, and the assembly was easy to do. The parts don't just slide in which I like, they feel secure once they are placed. I also made a custom designed to be engraved and Sadettin was great about it. Very excited to gift it!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="OMG AMAZING. I ordered for my bf for Christmas and I know hell love it! 6/5 stars. The quality of wood, the designs, the DELIVERY TIME. I order this on 11/30 and received this on 12/06. Thank you so so much!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Very pretty and exactly like what I imagined . I don’t know why but I thought it would come all put together but the fact that you can break it down is a bonus for moving and storage . Thank you very much my boyfriend will love this for Christmas !"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[boyfriend],
        name="Heart Keychain Set - Made with Authentic LEGO® Bricks, Matching keychains, Gift Set for Couples, Best Friends - Very High Quality & DURABLE",
        price="8.48",
        description="Matching Heart Friendship Keychain Set, Handmade with Real LEGO® Bricks!"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/27890741/r/il/31a0dd/4028709894/il_794xN.4028709894_i6tr.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="Love my keychains!! Amazing quality and super fast shipping!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="I got this for my boyfriend, it's very cute and the size is great! I'm so excited for him to get it."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="So cute!"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Came as expected. Love it!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[boyfriend],
        name="Leather Wallet, Personalized Wallet, Engraved Wallet, Gift For Him, Mens Wallet, Gift For Boyfriend, Gift For Dad, wallet for Son, RFID",
        price="15.99",
        description="How to add your personalization:"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/15037991/r/il/d35a34/3121890041/il_794xN.3121890041_pjaw.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I bought this early so I am ready for Father's day for my boyfriend and I can not express how happy I am with the wallet I got. I also received it way faster than expected."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Product was perfect and exactly what I was hoping for. The packaging is what blew my mind! It was in a very nice box and bubble wrapped twice!! Shipping was also faster than expected. Amazing shop to work with!!!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="Absolutely AMAZING! I’m so excited to give it to my boyfriend! And the customer service was fantastic they were so sweet! I’m so in love with this wallet 🥺"
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="Absolutely perfect! Fast shipping, great pricing. My personalized engraving came out exactly as I’d imagined. I know my fiancé will love it when I give it to him as a wedding gift! Highly recommend this shop!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[boyfriend],
        name="The Night We Met - 100% Accurate Star Map and the Perfect Anniversary Gift! (Gold Foil Look)",
        price="18.50",
        description="❤️ The Perfect Anniversary Gift: Gold Foil Look Star Map by Date and Location ❤️"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/21320634/r/il/ec9c96/3248220667/il_794xN.3248220667_3f92.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I’m obsessed with this. It’s so stunning and sentimental. I’m so glad I purchased from this shop."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Printed at Office Depot and it turned out perfectly!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I can’t wait to give this to my boyfriend for our anniversary. The creator was kind and helpful and the product looks great."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I got mine back the same day I ordered it! Super fast and fast responses as well from the seller. Got mine for me and my bfs 1 year anniversary"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[boyfriend],
        name="Anniversary Gift for Him, Wood Watch, Personalized Watch, Engraved Watch,Wooden Watch,Groomsmen Watch,Mens Watch,Boyfriend Gift,Gift for Dad",
        price="44.99",
        description="⌚Complimentary adjustment tool for wood link."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/17860793/r/il/582f59/1766951619/il_794xN.1766951619_sww3.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="I gave this watch to my husband for our 10 year wedding anniversary. He absolutely loved it and the engraving on the back came out great! The turnaround time and shipping was much quicker than I expected and I highly recommend!!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=5,
            review="Second item purchased from them! Very sleek with great quality!! They fit my long engraving on the back with ease!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=5,
            review="I love love love this watch! And I know that my fiancé will love it too. Thank you so much for a beautiful piece! I will definitely be shopping here again."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=4,
            review="Shop responded fast when I miss wrote my engraved statement. Shipped quickly. Watch is beautiful. Wish had a tad more color contrast."
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[boyfriend],
        name="POCKET HUG •a love token• Im always with you• long distance relationship• gifts for him •organza gift bag for giving",
        price="16.00",
        description="Send a POCKET HUG ."
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/6443042/r/il/ab7ed0/2844836111/il_794xN.2844836111_djny.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=5,
            review="The cutest little gift ever! I got it for my boyfriend for his birthday at the end of this month and I am so excited to be able to give it to him! Shipping was fast and the product is well made! Would definitely buy from Heather - Debbie again:) Thank y’all so much for this!"
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=1,
            review="I expected to have something to be on the back side. It's just a blank slug!"
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=4,
            review="Very cute packaging and fast delivery. The lettering came out a bit crooked but cute overall. My boyfriend loved it."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=5,
            review="I love it and I know my boyfriend will too!! Not only does it look perfect but after it was delivered I got a message from the seller making sure it got to me and it was in good condition!!"
        ),
    ])

    db.session.commit()

    product = Product(
        seller=anna,
        categories=[boyfriend],
        name="Men Docking Station,Anniversary Gift Him,Gift for Him Boyfriend,Wood Desk Organizer,Gift for Men Birthday,Gift for Husband,Father's Day Gift",
        price="26.73",
        description="Docking Station,Desk Organizer Wood,Gift for Him Boyfriend,Gift for Men Birthday,Gift for Husband,Anniversary Gifts Him,Father's Day Gift,Office Desk Gift"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url(
                "https://i.etsystatic.com/38091196/r/il/9753c9/4404296664/il_794xN.4404296664_aj3g.jpg"),
            preview=True
        ),

        Review(
            buyer=brian,
            product=product,
            rating=1,
            review="Item arrived broken and you can barely see the etching. Woods seem is very fragile and the recipe pages are completely unsatisfactory. They have a random red stamp that I think says “new” on the page corner but it is cut off and the 3 wholes are cut on the lines you are supposed to write on. Etching does not look like the picture. It is very thin, small, and light so you can barely see it. Shipping took a very long time."
        ),

        Review(
            buyer=caitlynn,
            product=product,
            rating=2,
            review="Update: because of my initial disappoint with the product, the seller did give me a partial refund. The binder itself is nice, but I still might replace the pages. Disappointed with this. The recipe pages look like they had taken a picture of someone else’s work and printed them out."
        ),

        Review(
            buyer=derrik,
            product=product,
            rating=2,
            review="Quality of the item was not the greatest my biggest disappointment was that the book design cover and writing is very small looks nothing like what the picture showed. This item did not meet my expectations."
        ),

        Review(
            buyer=elizabeth,
            product=product,
            rating=3,
            review="It arrived with the back broken off. I was disappointed as this was to be a Christmas gift. The customization is small and hard to read, but the seller did give me a full refund due to my disappointment with the product and is sending me a brand new one. Customer service gets 5 stars, but the product more like 2-3."
        ),
    ])

    db.session.commit()

    # Insert seeder code above this line

    for review in Review.query:
        review.seller_id = anna.id
        order = Order(buyer_id=review.buyer_id)
        purchase = OrderDetail(
            order=order,
            product_id=review.product_id,
            seller_id=review.seller_id,
            buyer_id=review.buyer_id,
            price=review.product.price,
            quantity=randint(1, 10)
        )
        db.session.add(purchase)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.


def undo_seed():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.order_details RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM reviews")
        db.session.execute("DELETE FROM order_details")
        db.session.execute("DELETE FROM orders")
        db.session.execute("DELETE FROM products_categories")
        db.session.execute("DELETE FROM categories")
        db.session.execute("DELETE FROM product_images")
        db.session.execute("DELETE FROM products")
        db.session.execute("DELETE FROM users")

    db.session.commit()
