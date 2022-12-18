import FiveStars from "../../../../FiveStars/FiveStars";
import styles from "./ProductDetailsReview.module.css"

export default function ProductDetailsReview({ review }) {
    let reviewDate = new Date(review.created_at);
    reviewDate = reviewDate.toLocaleDateString('en-us', { weekday: "short", year: "numeric", month: "short", day: "numeric" });
    return (
        <div className={styles.ProductDetailsReviewWrapper}>
            <div className={styles.reviewList}>
                <div>
                    <FiveStars rating={review.rating} />
                </div>
                <div className={styles.reviewText}>
                    {review.review}
                </div>
                <div className={styles.buyerInfo}>
                    <div className={styles.buyerPicture}><img src={review.buyer.profile_picture_url} alt={review.buyer.display_name[0].toUpperCase()} /></div>
                    <div className={styles.buyerName}>{review.buyer.display_name}</div>
                    <div className={styles.reviewDate}>{reviewDate}</div>
                </div>
            </div>
        </div>
    );
}
