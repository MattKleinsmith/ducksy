import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import { getCurrentUserOrders } from '../../store/orderDetails';
import { setReviewModal, setEditReviewModal } from '../../store/ui';
import { setProductId } from '../../store/productDetails';
import { getReviewsByBuyerId } from '../../store/reviews';


export default function OrderDetails() {
    const dispatch = useDispatch();
    const orderDetails = useSelector(state => Object.values(state.order_details));
    const reviews = useSelector(state => state.reviews);
    console.log(reviews);

    useEffect(() => {
        dispatch(getCurrentUserOrders());
        dispatch(getReviewsByBuyerId());
    }, [dispatch, reviews]);

    return (
        <>
            <div>Purchases</div>
            <div>
                {orderDetails.length && orderDetails.map(orderDetail =>
                    <div>
                        <div>Purchase from {orderDetail.product.seller_name}</div>
                        <div>{orderDetail.purchase_date} </div>
                        <div><img src={orderDetail.product.preview_image} alt="previewImage" /></div>
                        <div>{orderDetail.product.name}</div>
                        <div>{orderDetail.price}</div>
                        <div>{orderDetail.product_id in reviews ?
                            <div>
                                <div>Your review {reviews[orderDetail.product_id].rating} </div>
                                <div>{reviews[orderDetail.product_id].review} </div>
                                <button onClick={() => {
                                    dispatch(setProductId(orderDetail.product_id));
                                    dispatch(setEditReviewModal(true));
                                    dispatch(setReviewModal(false));
                                }}>Edit review</button>
                            </div>
                            :
                            <button onClick={() => {
                                dispatch(setProductId(orderDetail.product_id));
                                dispatch(setEditReviewModal(false));
                                dispatch(setReviewModal(true));
                            }}>Review this item</button>
                        }
                        </div>
                        {/* <div>
                            <button onClick={() => {
                                dispatch(setProductId(product.product_id));
                                dispatch(setReviewModal(true));
                            }}>Review this item</button>
                        </div> */}
                    </div>
                )}
            </div>
        </>
    );
}
