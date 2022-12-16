import "./FiveStars.css"

export default function FiveStars({ rating }) {
    const fullStarNum = Math.round(rating)
    const halfStar = (rating - fullStarNum) * 10
    return (<>
        {[...Array(fullStarNum).keys()].map(_ => (<i className="fa-solid fa-star FiveStars" />))}
        {fullStarNum < 5 && ((halfStar > 5 || halfStar == 0) ?
            (<i className="fa-solid fa-star FiveStars" />) :
            (<i className="fa-solid fa-star-half FiveStars"></i>))}
    </>);
}
