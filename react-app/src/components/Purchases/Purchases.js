import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import { getCurrentUserOrders } from '../../store/orderDetails';
import { setReviewModal, setEditReviewModal, setDeleteReviewModal } from '../../store/ui';
import { setProductId } from '../../store/productDetails';
import { getReviewsByBuyerId } from '../../store/buyerReviews';
import { setReviewId } from '../../store/reviewId';
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
            <div styles={styles.heading}>Purchases</div>
            <div>
                {orderDetails.length && orderDetails.map(orderDetail =>
                    <div>
                        <div>Purchase from {orderDetail.seller.display_name}</div>
                        <div>{orderDetail.purchase_date} </div>
                        <div><img src={orderDetail.product ? orderDetail.product.preview_image : "/placeholder.png"} alt="previewImage" /></div>
                        <div>{orderDetail.product ? orderDetail.product.name : "Product is unavailable"}</div>
                        <div>{orderDetail.price}</div>
                        <div>{orderDetail.product_id in reviews ?
                            <div>
                                <div>Your review {reviews[orderDetail.product_id].rating} </div>
                                <div>{reviews[orderDetail.product_id].review} </div>
                                <button onClick={() => {
                                    dispatch(setProductId(orderDetail.product_id));
                                    dispatch(setEditReviewModal(true));
                                }}>Edit review</button>
                                <button onClick={() => {
                                    dispatch(setReviewId(reviews[orderDetail.product_id].id));
                                    dispatch(setDeleteReviewModal(true));
                                }}>Remove review</button>
                            </div>
                            :
                            <button onClick={() => {
                                dispatch(setProductId(orderDetail.product_id));
                                dispatch(setEditReviewModal(false));
                                dispatch(setReviewModal(true));
                            }}>Review this item</button>
                        }
                        </div>
                    </div>
                )}
            </div>
        </>
    );
}
