import "./FiveStars.css"

export default function FiveStars({ rating }) {
    const fullStarNum = Math.floor(rating);
    const partialStar = rating % 1;
    return (<>
        {[...Array(fullStarNum)].map(_ => (<i className="fa-solid fa-star FiveStars" />))}
        {partialStar !== 0 &&
            (partialStar > 0.5 ?
                <i className="fa-solid fa-star FiveStars" />
                :
                <i className="fa-solid fa-star-half FiveStars" />)
        }
    </>);
}
