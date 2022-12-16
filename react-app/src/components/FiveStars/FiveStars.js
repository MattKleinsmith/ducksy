import "./FiveStars.css"

export default function FiveStars({ avgRating }) {
    const fullStarNum = Math.round(avgRating)
    const halfStar = (avgRating - fullStarNum) * 10
    return (<>
        {[...Array(fullStarNum).keys()].map(_ => (<i className="fa-solid fa-star FiveStars" />))}
        {fullStarNum < 5 && ((halfStar > 5 || halfStar == 0) ?
            (<i className="fa-solid fa-star FiveStars" />) :
            (<i className="fa-solid fa-star-half FiveStars"></i>))}
    </>);
}
