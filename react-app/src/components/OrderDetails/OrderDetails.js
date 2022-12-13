import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import { getCurrentUserOrders } from '../../store/orderDetails';
import { setReviewModal } from '../../store/ui';
import { setProductId } from '../../store/productDetails';


export default function OrderDetails() {
    // const [productId, setProductId] = useState(0);
    const dispatch = useDispatch();
    const allOrders = useSelector(state => Object.values(state.order_details));

    useEffect(() => {
        dispatch(getCurrentUserOrders());
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
