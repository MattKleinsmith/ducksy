import styles from './Purchases.module.css';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import { getCurrentUserOrders } from '../../store/orderDetails';
import { getReviewsByBuyerId } from '../../store/buyerReviews';
import PurchasesHeading from './PurchasesHeading/PurchasesHeading';
import PurchasesItem from './PurchasesItem/PurchasesItem';

export default function Purchases() {
    const dispatch = useDispatch();
    const orderDetails = useSelector(state => state.order_details);

    useEffect(() => {
        dispatch(getCurrentUserOrders());
        dispatch(getReviewsByBuyerId());
    }, [dispatch]);

    return (
        <>
            <div>
                <PurchasesHeading />
                <div className={styles.orderInfoWrapper}>
                    {orderDetails.map((orderDetail, i) =>
                        <PurchasesItem key={i} orderDetail={orderDetail} />
                    )}
                    {orderDetails.length === 0 && "No purchases yet."}
                </div>
            </div>
        </>
    );
};
