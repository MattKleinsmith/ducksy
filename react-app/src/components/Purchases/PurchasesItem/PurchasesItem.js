import styles from './PurchasesItem.module.css';
import ShopNote from './ShopNote/ShopNote';
import PurchasedFrom from './PurchasedFrom/PurchasedFrom';
import PurchasedProduct from './PurchasedProduct/PurchasedProduct';

export default function PurchasesItem({ orderDetail }) {
    return (
        <div className={styles.wrapper}>
            <PurchasedFrom orderDetail={orderDetail} />
            <PurchasedProduct orderDetail={orderDetail} />
            <ShopNote />
        </div>
    );
};
