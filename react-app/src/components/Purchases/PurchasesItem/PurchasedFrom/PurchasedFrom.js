import styles from './PurchasedFrom.module.css';

export default function PurchasedFrom({ orderDetail }) {
    return (
        <div className={styles.wrapper}>
            <div>Purchased from {orderDetail.seller.display_name} <span>on {orderDetail.purchase_date}</span></div>
            <div>{`$${parseFloat(orderDetail.price).toFixed(2)}`}</div>
        </div>
    );
};
