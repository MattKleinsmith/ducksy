import styles from './PurchasedProduct.module.css';
import BuyItAgain from './BuyItAgain/BuyItAgain';
import PurchasedProductReview from './PurchasedProductReview/PurchasedProductReview';
import PurchasedProductName from './PurchasedProductName/PurchasedProductName';
import PurchasedProductImage from './PurchasedProductImage/PurchasedProductImage';

export default function PurchasedProduct({ orderDetail }) {
    return (
        <div className={styles.wrapper}>

            <PurchasedProductImage orderDetail={orderDetail} />

            <div className={styles.right}>
                <PurchasedProductName orderDetail={orderDetail} />
                <PurchasedProductReview orderDetail={orderDetail} />
                <BuyItAgain product={orderDetail.product} />
            </div>

        </div>
    );
};
