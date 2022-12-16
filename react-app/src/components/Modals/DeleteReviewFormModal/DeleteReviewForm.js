import styles from './DeleteReviewForm.module.css';
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setDeleteReviewModal } from "../../../store/ui";
import { deleteReview } from '../../../store/buyerReviews';


export default function DeleteReviewForm() {
    const [errors, setErrors] = useState([]);
    const dispatch = useDispatch();
    const reviewId = useSelector(state => state.reviewDetails);

    const handleSubmit = e => {
        e.preventDefault();
        return dispatch(deleteReview(reviewId.id))
            .then(() => {
                dispatch(setDeleteReviewModal(false));
            })
            .catch(response => {
                if (response.errors) setErrors(Object.values(response.errors));
            });
    };

    return (
        <form className={styles.deleteForm} onSubmit={handleSubmit}>
            <ul style={{ color: 'rgb(246, 18, 18)' }}>
                {errors.map((error, i) => <li key={i}>{error}</li>)}
            </ul>
            <div><button className={styles.cancel} onClick={() => dispatch(setDeleteReviewModal(false))}>x</button></div>
            <h4>Are you sure you want to delete this review?</h4>
            <button className={styles.deleteFormButton} type="submit">Delete review</button>
        </form >
    );
}
