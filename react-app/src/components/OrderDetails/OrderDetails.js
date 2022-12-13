import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import { getCurrentUserOrders } from '../../store/orderDetails';
import { setReviewModal } from '../../store/ui';
import { setProductId } from '../../store/productDetails';
// import { getReviewsByBuyerId } from '../../store/reviews';


export default function OrderDetails() {
    const dispatch = useDispatch();
    const allOrders = useSelector(state => Object.values(state.order_details));
    // const reviews = useSelector(state => Object.values(state.reviews));

    useEffect(() => {
        dispatch(getCurrentUserOrders());
        // dispatch(getReviewsByBuyerId());
    }, [dispatch]);

    return (
        <>
            <div>Purchases</div>
            <div>
                {allOrders.length && allOrders.map(product =>
                    <div>
                        <div>{product.product.seller_name}</div>
                        <div>{product.product.name}</div>
                        <div><img src={product.product.preview_image} alt="previewImage" /></div>
                        <div>{product.price}</div>
                        <div></div>
                        <div><button onClick={() => {
                            dispatch(setProductId(product.product_id));
                            dispatch(setReviewModal(true));
                        }}>Review this item</button>
                        </div>
                    </div>
                )}
            </div>
        </>
    );
}
