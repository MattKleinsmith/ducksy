import "./FiveStars.css";

export default function FiveStars({ rating }) {
    const fullStarNum = Math.floor(rating);
    const partialStar = rating % 1;
    const lastClass = partialStar > 0.5 ? "" : "-half";
    return (<>
        {[...Array(fullStarNum)].map(_ => <i className="fa-solid fa-star FiveStars" />)}
        {partialStar !== 0 && <i className={`fa-solid fa-star${lastClass} FiveStars`} />}
    </>);
}
