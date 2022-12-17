import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from "react-router-dom";
import { useEffect } from "react";
import { getCurrentUserOrders } from '../../store/orderDetails';
import { setReviewModal, setEditReviewModal, setDeleteReviewModal } from '../../store/ui';
import { setProductId } from '../../store/productDetails';
import { getReviewsByBuyerId } from '../../store/buyerReviews';
import { clearReviewDetails, setReviewDetails } from '../../store/reviewDetails';
import styles from './Purchases.module.css';
import BuyItAgain from './BuyItAgain';

export default function Purchases() {
    const dispatch = useDispatch();
    const orderDetails = useSelector(state => state.order_details);
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
                    {orderDetails.length > 0 && orderDetails.map((orderDetail, i) =>
                        <div key={i} className={styles.orderInfo}>
                            <div className={styles.purchaseFromWrapper}>
                                <div>Purchased from {orderDetail.seller.display_name} <span>on {orderDetail.purchase_date}</span></div>
                                <div>{`$${parseFloat(orderDetail.price).toFixed(2)}`}</div>
                            </div>
                            <div className={styles.productWrapper}>
                                <NavLink
                                    className={styles.productName}
                                    to={`/listing/${orderDetail.product.id}`}>
                                    <div className={styles.imageWrapper}>
                                        <img className={styles.image} src={orderDetail.product ? orderDetail.product.preview_image : "/images/placeholder.png"} alt="previewImage" />
                                    </div>
                                </NavLink>
                                <div className={styles.infoWrapper}>
                                    <NavLink
                                        className={styles.productName}
                                        to={`/listing/${orderDetail.product.id}`}>
                                        <div>
                                            {orderDetail.product ? orderDetail.product.name : "Product is unavailable"}
                                        </div>
                                    </NavLink>
                                    <div className={styles.yourReview}>
                                        {orderDetail.product_id in reviews ?
                                            <div>
                                                <div className={styles.cancelWrapper}>
                                                    <div className={styles.rating}>
                                                        <span>Your review </span>
                                                        <div>{[...Array(reviews[orderDetail.product_id].rating)].map((_, i) => <i key={i} className="fa-solid fa-star" />)}</div>
                                                    </div>
                                                    <button className={styles.removeReviewBtn} onClick={() => {
                                                        dispatch(setReviewDetails(reviews[orderDetail.product_id].id, reviews[orderDetail.product_id].review));
                                                        dispatch(setDeleteReviewModal(true));
                                                    }}>x</button>
                                                </div>
                                                <div className={styles.review}>{reviews[orderDetail.product_id].review} </div>
                                                <div>
                                                    <button className={`${styles.editReviewBtn}`} onClick={() => {
                                                        dispatch(setProductId(orderDetail.product_id));
                                                        dispatch(setReviewDetails(reviews[orderDetail.product_id].id, reviews[orderDetail.product_id].review, reviews[orderDetail.product_id].rating));
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
                                    <BuyItAgain product={orderDetail.product} />
                                </div>
                            </div>
                            <div className={styles.shopNote}>
                                <p style={{ color: '#333' }}>Shop Note</p>
                                <p>Thank you so much for your purchase!!! We will have it shipped out asap and send you an email to notify you when it ships. Again, your patronage is very much appreciated and keeps our small business running strong. Thanks for your support!</p>
                            </div>
                        </div>
                    )}
                    {orderDetails.length === 0 && <div>No purchases yet.</div>}
                </div>
            </div>
        </>
    );
};
