import './DeleteReviewForm.css';
import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { setDeleteReviewModal } from "../../../store/ui";
import { deleteReview } from '../../../store/reviews';

export default function DeleteReviewForm() {
    const dispatch = useDispatch();
    const reviewId = useSelector(state => state.reviewId);
    console.log(reviewId);

    const handleSubmit = (e) => {
        e.preventDefault();
        return dispatch(deleteReview(reviewId.id))
            .then(() => {
                dispatch(setDeleteReviewModal(false));
            });
    };

    return (
        <form className="deleteForm" onSubmit={handleSubmit}>
            <h1 style={{ width: "300px" }}>Are you sure you want to delete this review?</h1>
            <button className="deleteFormButton" type="submit">Delete review</button>
        </form >
    );
}
