import './DeleteReviewForm.css';
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setDeleteReviewModal } from "../../../store/ui";
import { deleteReview, getReviewsByBuyerId } from '../../../store/reviews';

export default function DeleteReviewForm() {
    const [errors, setErrors] = useState([]);
    const dispatch = useDispatch();
    const reviewId = useSelector(state => state.reviewId);

    const handleSubmit = (e) => {
        e.preventDefault();
        return dispatch(deleteReview(reviewId.id))
            .then(() => {
                dispatch(setDeleteReviewModal(false));
                dispatch(getReviewsByBuyerId());
            })
            .catch(response => {
                if (response.errors) setErrors(Object.values(response.errors));
            });
    };

    return (
        <form className="deleteForm" onSubmit={handleSubmit}>
            <ul style={{ color: 'rgb(246, 18, 18)' }}>
                {errors.map((error, i) => <li key={i}>{error}</li>)}
            </ul>
            <div><button className='cancel-x' onClick={() => dispatch(setDeleteReviewModal(false))}>x</button></div>
            <h1 style={{ width: "300px" }}>Are you sure you want to delete this review?</h1>
            <button className="deleteFormButton" type="submit">Delete review</button>
        </form >
    );
}
