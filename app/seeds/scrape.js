result = `
    product = Product(
        seller=anna,
        categories=[home_decor],
        name="${document.querySelector(".wt-text-body-03.wt-line-height-tight.wt-break-word").innerText}",
        price="${document.querySelectorAll(".wt-text-title-03.wt-mr-xs-1")[0].innerText.replace('+', '').replace("$", '')}",
        description="${document.querySelector(".wt-text-body-01.wt-break-word").innerText.split('\n')[0].replaceAll('"', "'")}"
    )

    db.session.add_all([
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url("${document.querySelector(".wt-max-width-full.wt-horizontal-center.wt-vertical-center.carousel-image.wt-rounded").src}"),
            preview=True
        ),
`

ratings = Array.from(document.querySelectorAll(".wt-grid__item-xs-12 [name='rating']")).map(review => review.value)
reviews = Array.from(document.querySelectorAll(".wt-text-truncate--multi-line")).map(review => review.innerText).slice(0, ratings.length)
users = ["brian", "caitlynn", "derrik", "elizabeth"]

ratings.forEach((rating, i) => {
    result += `
        Review(
            buyer=${users[i]},
            product=product,
            rating=${rating},
            review="${reviews[i].replaceAll('"', "'")}"
        ),
    `
})

result += '])'

result += '\n\n    db.session.commit()'

console.log(result)
