from app.models import db, environment, SCHEMA, User, Product, ProductImage, Review, Category, Order, OrderDetail
from app.seeds.upload import upload_image_to_bucket_from_url

# Adds a demo user, you can add other users here if you want


def seed_all():
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

    demo = User(display_name="Demo",
                email="demo@aa.io",
                password="password")
    marnie = User(display_name="marnie",
                  email="marnie@aa.io",
                  password="password")
    bobbie = User(display_name="bobbie",
                  email="bobbie@aa.io",
                  password="password")

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
    personalized_gift = Category(name="personalized gift")
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
        seller=anna,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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
            buyer=brian,
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

    order = Order(buyer_id=brian.id)
    db.session.add_all([
        OrderDetail(
            seller_id=anna.id,
            price=product.id,
            product=product,
            order=order
        )
    ])

    db.session.commit()

    # Insert seeder code above this line

    reviews = Review.query.all()
    for review in reviews:
        review.seller = anna
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
            f"TRUNCATE table {SCHEMA}.orders_products RESTART IDENTITY CASCADE;")
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
