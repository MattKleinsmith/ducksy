import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setEditReviewModal } from '../../../store/ui';
import { getReviewsByBuyerId, updateReview } from '../../../store/buyerReviews';
import './editReviewForm.css';

export default function EditReviewForm() {
    const productId = useSelector(state => state.productDetails.id);
    const reviews = useSelector(state => state.reviews);
    const originalReview = reviews[productId];
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
            <div>My review</div>
            <form onSubmit={handleSubmit}>
                <ul style={{ color: 'rgb(246, 18, 18)' }}>
                    {errors.map((error, i) => <li key={i}>{error}</li>)}
                </ul>
                <div className='star-rating'><span>Select your rating   </span>
                    {[...Array(5)].map((star, i) => {
                        i += 1;
                        return (
                            <button
                                type='button'
                                key={i}
                                className={i <= ((rating && hover) || hover) ? 'on' : 'off'}
                                onClick={() => setRating(i)}
                                onMouseEnter={() => setHover(i)}
                                onMouseLeave={() => setHover(rating)}
                            >
                                <span className='star'><i className="fa-solid fa-star" style={{ fontSize: '25px' }}></i></span>
                            </button>);
                    })}
                </div >

                <textarea
                    className='review-detail'
                    placeholder='Update here'
                    type='text'
                    onChange={e => setReview(e.target.value)}
                    value={review}
                />
                <button className='review-btn' type='submit'>Update review</button>
            </form>
            <div><button className='cancel-btn' onClick={() => dispatch(setEditReviewModal(false))}>Cancel</button></div>
        </>
    );
};