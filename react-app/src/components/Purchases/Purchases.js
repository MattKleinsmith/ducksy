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
            <div className={styles.body}>
                <div className={styles.heading}>Purchases</div>
                <div className={styles.orderInfo}>
                    {orderDetails.length && orderDetails.map((orderDetail, i) =>
                        <div key={i}>
                            <div className={styles.purchaseFromWrapper}>
                                <div>Purchase from {orderDetail.seller.display_name} <span>on {orderDetail.purchase_date}</span></div>
                                <div>{orderDetail.price}</div>
                            </div>
                            <div className={styles.productWrapper}>
                                <div><img className={styles.image} src={orderDetail.product ? orderDetail.product.preview_image : "/placeholder.png"} alt="previewImage" />
                                </div>
                                <div className={styles.infoWrapper}>
                                    <div className={styles.productName}>
                                        {orderDetail.product ? orderDetail.product.name : "Product is unavailable"}
                                    </div>
                                    <div>
                                        {orderDetail.product_id in reviews ?
                                            <div>
                                                <div>Your review {reviews[orderDetail.product_id].rating} </div>
                                                <div>{reviews[orderDetail.product_id].review} </div>
                                                <div>
                                                    <button onClick={() => {
                                                        dispatch(setProductId(orderDetail.product_id));
                                                        dispatch(setReviewId(reviews[orderDetail.product_id].id, reviews[orderDetail.product_id].review, reviews[orderDetail.product_id].rating));
                                                        dispatch(setEditReviewModal(true));
                                                    }}>Edit review</button>
                                                    <button onClick={() => {
                                                        dispatch(setReviewId(reviews[orderDetail.product_id].id, reviews[orderDetail.product_id].review));
                                                        dispatch(setDeleteReviewModal(true));
                                                    }}>Remove review</button>
                                                </div>
                                            </div>
                                            :
                                            <div className='styles.reviewBtn'>
                                                <button onClick={() => {
                                                    dispatch(setProductId(orderDetail.product_id));
                                                    dispatch(setEditReviewModal(false));
                                                    dispatch(setReviewModal(true));
                                                }}>Review this item</button>
                                            </div>
                                        }
                                    </div>
                                    <div className={styles.buyAgain}>
                                        <div><button className={styles.buyAgainBtn}>Buy this again</button></div>
                                        <div>{orderDetail.price}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </>
    );
}
