import "./ProductDetailsReview.css"

export default function ProductDetailsReview({ review }) {
    return (
        <div className="ProductDetailsReviewWrapper">
            <div className="ProductDetailsReview">
                {review.review}
            </div>
        </div>
    );
}
