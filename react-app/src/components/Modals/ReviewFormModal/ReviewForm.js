import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setReviewModal } from '../../../store/ui';
import { postReview } from '../../../store/reviews';
import './reviewForm.css';

export default function ReviewForm() {
    const [review, setReview] = useState('');
    const [rating, setRating] = useState(0);
    const [hover, setHover] = useState(0);
    const dispatch = useDispatch();

    const handleSubmit = async e => {
        e.preventDefault();
        const newReview = { rating, review };
        if (newReview) {
            return await dispatch(postReview(newReview, 1)) // use review no1 for testing now
                .then(() => {
                    dispatch(setReviewModal(false));
                    setRating(0);
                    setReview("");
                });
        }
    };

    return (
        <>
            <div>My review</div>
            <form onSubmit={handleSubmit}>
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
        </>
    );
}
