import styles from './PurchasedProductReview.module.css';
import { setReviewModal, setDeleteReviewModal } from '../../../../../store/ui';
import { setProductId } from '../../../../../store/productDetails';
import { clearReviewDetails, setReviewDetails } from '../../../../../store/reviewDetails';
import { useSelector, useDispatch } from 'react-redux';

export default function PurchasedProductReview({ orderDetail }) {
    const dispatch = useDispatch();
    const reviews = useSelector(state => state.buyerReviews);
    return (
        <div className={styles.wrapper}>
            {orderDetail.product_id in reviews ?
                <div>
                    <div className={styles.cancelWrapper}>
                        <div className={styles.rating}>
                            <span>Your review </span>
                            <div>{[...Array(reviews[orderDetail.product_id].rating)].map((_, i) => <i key={i} className="fa-solid fa-star" />)}</div>
                        </div>
                        <button className={styles.removeReviewBtn} onClick={() => {
                            dispatch(setReviewDetails(
                                reviews[orderDetail.product_id].id,
                                reviews[orderDetail.product_id].review,
                                reviews[orderDetail.product_id].rating,
                                orderDetail.product_id));
                            dispatch(setDeleteReviewModal(true));
                        }}>x</button>
                    </div>
                    <div className={styles.review}>{reviews[orderDetail.product_id].review} </div>
                    <div>
                        <button className={`${styles.editReviewBtn}`} onClick={() => {
                            dispatch(setProductId(orderDetail.product_id));
                            dispatch(setReviewDetails(
                                reviews[orderDetail.product_id].id,
                                reviews[orderDetail.product_id].review,
                                reviews[orderDetail.product_id].rating,
                                orderDetail.product_id));
                            dispatch(setReviewModal(true));
                        }}>Edit review</button>
                    </div>
                </div>
                :
                <div className={styles.reviewBtnWrapper}>
                    <button className={`${styles.reviewBtn}`} onClick={() => {
                        dispatch(setProductId(orderDetail.product_id));
                        dispatch(clearReviewDetails());
                        dispatch(setReviewModal(true));
                    }}>Review this item</button>
                </div>
            }
        </div>
    );
};
