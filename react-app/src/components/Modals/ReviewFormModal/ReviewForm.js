import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setReviewModal } from '../../../store/ui';
import { getReviewsByBuyerId, postReview } from '../../../store/reviews';
import './reviewForm.css';


export default function ReviewForm() {
    const [review, setReview] = useState('');
    // const [isReviewed, setIsReviewed] = useState(false);
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
                    // setIsReviewed(true);
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
                    placeholder='Review here'
                    type='text'
                    onChange={e => setReview(e.target.value)}
                    value={review}
                />
                <button className='review-btn' type='submit'>Post Your review</button>
            </form>
            <div><button className='cancel-btn' onClick={() => dispatch(setReviewModal(false))}>Cancel</button></div>
        </>
    );
};
