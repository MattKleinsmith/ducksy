import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import { getCurrentUserOrders } from '../../store/orderDetails';
import { setReviewModal, setEditReviewModal, setDeleteReviewModal } from '../../store/ui';
import { setProductId } from '../../store/productDetails';
import { getReviewsByBuyerId } from '../../store/buyerReviews';
import { setReviewId } from '../../store/reviewDetails';
import styles from './Purchases.module.css';

export default function Purchases() {
    const dispatch = useDispatch();
    const orderDetails = useSelector(state => Object.values(state.order_details));
    const reviews = useSelector(state => state.buyerReviews);

    useEffect(() => {
        dispatch(getCurrentUserOrders());
        dispatch(getReviewsByBuyerId());
    }, [dispatch]);

    return (
        <>
            <div>
                <div className={styles.heading}>
                    <p className={styles.purchases}>Purchases</p>
                </div>
                <div className={styles.orderInfoWrapper}>
                    {orderDetails.length && orderDetails.map(orderDetail =>
                        <div className={styles.orderInfo}>
                            <div className={styles.purchaseFromWrapper}>
                                <div>Purchased from {orderDetail.seller.display_name} <span>on {orderDetail.purchase_date}</span></div>
                                <div>{`$${parseFloat(orderDetail.price).toFixed(2)}`}</div>
                            </div>
                            <div className={styles.productWrapper}>
                                <div className={styles.imageWrapper}>
                                    <img className={styles.image} src={orderDetail.product ? orderDetail.product.preview_image : "/placeholder.png"} alt="previewImage" />
                                </div>
                                <div className={styles.infoWrapper}>
                                    <div className={styles.productName}>
                                        {orderDetail.product ? orderDetail.product.name : "Product is unavailable"}
                                    </div>
                                    <div className={styles.yourReview}>
                                        {orderDetail.product_id in reviews ?
                                            <div>
                                                <div className={styles.cancelWrapper}>
                                                    <div className={styles.rating}>
                                                        {(reviews[orderDetail.product_id].rating === 1) ?
                                                            <div><span>Your review </span><i class="fa-solid fa-star"></i></div> :
                                                            (reviews[orderDetail.product_id].rating === 2) ?
                                                                <div>
                                                                    <span>Your review </span>
                                                                    <i class="fa-solid fa-star"></i>
                                                                    <i class="fa-solid fa-star"></i>
                                                                </div> :
                                                                (reviews[orderDetail.product_id].rating === 3) ? <div>
                                                                    <span>Your review </span>
                                                                    <i class="fa-solid fa-star"></i>
                                                                    <i class="fa-solid fa-star"></i>
                                                                    <i class="fa-solid fa-star"></i>
                                                                </div> :
                                                                    (reviews[orderDetail.product_id].rating === 4) ? <div>
                                                                        <span>Your review </span>
                                                                        <i class="fa-solid fa-star"></i>
                                                                        <i class="fa-solid fa-star"></i>
                                                                        <i class="fa-solid fa-star"></i>
                                                                        <i class="fa-solid fa-star"></i>
                                                                    </div> :
                                                                        <div>
                                                                            <span>Your review </span>
                                                                            <i class="fa-solid fa-star"></i>
                                                                            <i class="fa-solid fa-star"></i>
                                                                            <i class="fa-solid fa-star"></i>
                                                                            <i class="fa-solid fa-star"></i>
                                                                            <i class="fa-solid fa-star"></i>
                                                                        </div>
                                                        } </div>
                                                    <button className={styles.removeReviewBtn} onClick={() => {
                                                        dispatch(setReviewId(reviews[orderDetail.product_id].id, reviews[orderDetail.product_id].review));
                                                        dispatch(setDeleteReviewModal(true));
                                                    }}>x</button>
                                                </div>
                                                <div className={styles.review}>{reviews[orderDetail.product_id].review} </div>
                                                <div>
                                                    <button className={styles.editReviewBtn} onClick={() => {
                                                        dispatch(setProductId(orderDetail.product_id));
                                                        dispatch(setReviewId(reviews[orderDetail.product_id].id, reviews[orderDetail.product_id].review, reviews[orderDetail.product_id].rating));
                                                        dispatch(setEditReviewModal(true));
                                                    }}>Edit review</button>
                                                </div>
                                            </div>
                                            :
                                            <div className={styles.reviewBtn}>
                                                <button className={styles.reviewBtn} onClick={() => {
                                                    dispatch(setProductId(orderDetail.product_id));
                                                    dispatch(setEditReviewModal(false));
                                                    dispatch(setReviewModal(true));
                                                }}>Review this item</button>
                                            </div>
                                        }
                                    </div>
                                    <div className={styles.buyAgain}>
                                        <div><button className={styles.buyAgainBtn}>Buy this again</button></div>
                                        <div className={styles.price}>{`$${parseFloat(orderDetail.price).toFixed(2)}`}</div>
                                    </div>
                                </div>
                            </div>
                            <div className={styles.shopNote}>
                                <p style={{ color: '#333' }}>Shop Note</p>
                                <p>Thank you so much for your purchase!!! We will have it shipped out asap and send you an email to notify you when it ships. Again, your patronage is very much appreciated and keeps our small business running strong. Thanks for your support!</p>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </>
    );
};
