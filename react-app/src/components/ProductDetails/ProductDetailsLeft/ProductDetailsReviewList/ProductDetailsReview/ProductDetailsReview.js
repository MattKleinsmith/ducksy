import FiveStars from "../../../../FiveStars/FiveStars";
import "./ProductDetailsReview.css"

export default function ProductDetailsReview({ review }) {
    return (
        <div className="ProductDetailsReviewWrapper">
            <div className="ProductDetailsReview">
                <div>
                    <FiveStars rating={review.rating} />
                </div>
                {review.review}
            </div>
        </div>
    );
}
