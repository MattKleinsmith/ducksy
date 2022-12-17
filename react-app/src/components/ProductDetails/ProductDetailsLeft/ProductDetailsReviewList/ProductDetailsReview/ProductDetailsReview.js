import FiveStars from "../../../../FiveStars/FiveStars";
import styles from "./ProductDetailsReview.module.css"

export default function ProductDetailsReview({ review }) {
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
                    <div className={styles.buyerPicture}>{review.buyer.display_name[0].toUpperCase()}</div>
                    <div className={styles.buyerName}>{review.buyer.display_name}</div>
                    <div className={styles.reviewDate}>{review.created_at.slice(5, 17)}</div>
                </div>
            </div>
        </div>
    );
}
