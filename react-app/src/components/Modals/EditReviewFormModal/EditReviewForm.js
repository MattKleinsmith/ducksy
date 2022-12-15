import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setEditReviewModal } from '../../../store/ui';
import { getReviewsByBuyerId, updateReview } from '../../../store/buyerReviews';
import styles from './EditReviewForm.module.css';

export default function EditReviewForm() {
    const originalReview = useSelector(state => state.reviewDetails);
    const [review, setReview] = useState(originalReview.review);
    const [rating, setRating] = useState(originalReview.rating);
    const [hover, setHover] = useState(rating);
    const [errors, setErrors] = useState([]);
    const dispatch = useDispatch();

    const handleSubmit = async e => {
        e.preventDefault();
        const newReview = { rating, review };
        if (newReview) {
            return await dispatch(updateReview(originalReview.id, newReview))
                .then(() => {
                    dispatch(setEditReviewModal(false));
                    dispatch(getReviewsByBuyerId());
                })
                .catch(response => {
                    if (response.errors) setErrors(Object.values(response.errors));
                });
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
                                    className={i <= ((rating && hover) || hover) ? styles.on : styles.off}
                                    onClick={() => setRating(i)}
                                    onMouseEnter={() => setHover(i)}
                                    onMouseLeave={() => setHover(rating)}
                                >
                                    <span className={styles.star}><i className="fa-solid fa-star" style={{ fontSize: '25px' }}></i></span>
                                </button>);
                        })}
                    </div >
                    <div>
                        <p className={styles.tagline}>Help others by sharing your feedback</p>
                        <p className={styles.suggestion}>What do you like about this? Did it ship on time? Describe your experience with this shop.</p>
                    </div>
                    <textarea
                        className={styles.reviewDetail}
                        placeholder='Update here'
                        type='text'
                        onChange={e => setReview(e.target.value)}
                        value={review}
                    />
                    <div className={styles.btnWrapper}>
                        <button className={styles.cancelBtn} onClick={() => dispatch(setEditReviewModal(false))}>Cancel</button>
                        <button className={styles.reviewBtn} type='submit'>Update Your review</button>
                    </div>
                </form>
            </div>
        </>
    );
};
