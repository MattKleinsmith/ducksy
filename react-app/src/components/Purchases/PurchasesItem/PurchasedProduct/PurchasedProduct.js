import styles from './PurchasedProduct.module.css';
import { NavLink } from "react-router-dom";
import BuyItAgain from './BuyItAgain/BuyItAgain';
import PurchasedProductReview from './PurchasedProductReview/PurchasedProductReview';

export default function PurchasedProduct({ orderDetail }) {
    return (
        <div className={styles.wrapper}>

            <NavLink
                className={styles.name}
                to={`/listing/${orderDetail.product.id}`}>
                <div className={styles.imageWrapper}>
                    <img className={styles.image} src={orderDetail.product ? orderDetail.product.preview_image : "/images/placeholder.png"} alt="previewImage" />
                </div>
            </NavLink>

            <div className={styles.infoWrapper}>

                <NavLink
                    className={styles.name}
                    to={`/listing/${orderDetail.product.id}`}>
                    <div>
                        {orderDetail.product ? orderDetail.product.name : "Product is unavailable"}
                    </div>
                </NavLink>

                <PurchasedProductReview orderDetail={orderDetail} />
                <BuyItAgain product={orderDetail.product} />
            </div>
        </div>
    );
};
