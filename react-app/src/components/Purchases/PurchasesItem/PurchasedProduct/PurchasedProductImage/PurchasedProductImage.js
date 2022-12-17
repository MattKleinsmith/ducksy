import styles from './PurchasedProductImage.module.css';
import { NavLink } from "react-router-dom";

export default function PurchasedProductImage({ orderDetail }) {
    return (
        <div className={styles.wrapper}>
            <NavLink to={`/listing/${orderDetail.product.id}`}>
                <img
                    className={styles.image}
                    src={orderDetail.product ? orderDetail.product.preview_image : "/images/placeholder.png"}
                    alt="previewImage"
                />
            </NavLink>
        </div >
    );
};
