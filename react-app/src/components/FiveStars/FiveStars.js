import "./FiveStars.css";

export default function FiveStars({ rating }) {
    const fullStarNum = Math.floor(rating);
    const partialStar = rating % 1;
    const lastClass = partialStar > 0.5 ? "" : "-half";
    return (<div className="FiveStarsDiv">
        {[...Array(fullStarNum)].map((_, i) => <i key={i} className="fa-solid fa-star FiveStar" />)}
        {partialStar !== 0 && <i className={`fa-solid fa-star${lastClass} FiveStar`} />}
    </div>);
}
