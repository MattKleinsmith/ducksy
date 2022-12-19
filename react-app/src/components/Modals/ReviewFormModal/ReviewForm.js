import styles from './ReviewForm.module.css';
import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setReviewModal } from '../../../store/ui';
import { getReviewsByBuyerId, postReview, updateReview } from '../../../store/buyerReviews';
// import { getProductsByCategory } from '../../../store/productsBySearch';
// import { getProducts } from '../../../store/products';


export default function ReviewForm() {
    const originalReview = useSelector(state => state.reviewDetails);
    const [review, setReview] = useState(originalReview?.review || '');
    const [rating, setRating] = useState(originalReview?.rating || 0);
    const [hover, setHover] = useState(rating);
    const [errors, setErrors] = useState([]);
    const dispatch = useDispatch();

    const productId = useSelector(state => state.productDetails.id);
    const handleSubmit = async e => {
        e.preventDefault();
        const body = { rating, review };
        const thunk = originalReview ?
            updateReview(originalReview, body) : postReview(productId, body);
        try {
            await dispatch(thunk);
            dispatch(setReviewModal(false));
            dispatch(getReviewsByBuyerId());
        }
        catch (e) {
            const errors = Object.entries(e.errors)
                .map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`);
            setErrors(errors);
        }
    };

    return (
        <>
            <div className={styles.formWrapper}>
                <form onSubmit={handleSubmit}>
                    <ul className={styles.errors}>
                        {errors.map((error, i) => <li key={i}>{error}</li>)}
                    </ul>
                    <div className={styles.myReview}>My review</div>
                    <div className={styles.stars}>
                        {[...Array(5)].map((star, i) => {
                            i += 1;
                            return (
                                <button
                                    type='button'
                                    key={i}
                                    className={`${styles.button} ${i <= ((rating && hover) || hover) ? styles.on : styles.off}`}
                                    onClick={() => setRating(i)}
                                    onMouseEnter={() => setHover(i)}
                                    onMouseLeave={() => setHover(rating)}
                                >
                                    <span className={styles.star}><i className="fa-solid fa-star" style={{ fontSize: '25px' }} /></span>
                                </button>);
                        })}
                    </div >
                    <div>
                        <p className={styles.tagline}>Help others by sharing your feedback</p>
                        <p className={styles.suggestion}>What do you like about this? Did it ship on time? Describe your experience with this shop.</p>
                    </div>
                    <textarea className={styles.reviewDetail}
                        placeholder='Write your review here'
                        type='text'
                        onChange={e => setReview(e.target.value)}
                        value={review}
                    />
                    <div className={styles.btnWrapper}>
                        <button className={styles.cancelBtn} onClick={() => dispatch(setReviewModal(false))}>Cancel</button>
                        <button className={styles.reviewBtn} type='submit'>{originalReview ? "Update" : "Post"} your review</button>
                    </div>
                </form>
            </div >
        </>
    );
};
