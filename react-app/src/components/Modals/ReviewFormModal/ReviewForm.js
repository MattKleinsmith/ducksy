import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setReviewModal } from '../../../store/ui';
import { getReviewsByBuyerId, postReview } from '../../../store/buyerReviews';
import styles from './ReviewForm.module.css';


export default function ReviewForm() {
    const [review, setReview] = useState('');
    const [rating, setRating] = useState(0);
    const [hover, setHover] = useState(0);
    const [errors, setErrors] = useState([]);
    const dispatch = useDispatch();

    const id = useSelector(state => state.productDetails.id);
    const handleSubmit = async e => {
        e.preventDefault();
        const newReview = { rating, review };
        if (newReview) {
            return await dispatch(postReview(id, newReview))
                .then(() => {
                    dispatch(setReviewModal(false));
                    dispatch(getReviewsByBuyerId());
                    setRating(0);
                    setReview("");
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
                                    <i className="fa-solid fa-star" style={{ fontSize: '25px' }}></i>
                                </button>);
                        })}
                    </div >
                    <div>
                        <p className={styles.tagline}>Help others by sharing your feedback</p>
                        <p className={styles.suggestion}>What do you like about this? Did it ship on time? Describe your experience with this shop.</p>
                    </div>
                    <textarea className={styles.reviewDetail}
                        placeholder='Review here'
                        type='text'
                        onChange={e => setReview(e.target.value)}
                        value={review}
                    />
                    <div className={styles.btnWrapper}>
                        <button className={styles.cancelBtn} onClick={() => dispatch(setReviewModal(false))}>Cancel</button>
                        <button className={styles.reviewBtn} type='submit'>Post Your review</button>
                    </div>
                </form>
            </div >
        </>
    );
};
