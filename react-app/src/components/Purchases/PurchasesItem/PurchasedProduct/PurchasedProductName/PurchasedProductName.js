import styles from './PurchasedProductName.module.css';
import { NavLink } from "react-router-dom";

export default function PurchasedProductName({ orderDetail }) {
    return (
        <NavLink className={styles.wrapper} to={`/listing/${orderDetail.product.id}`} >
            <div>{orderDetail.product ? orderDetail.product.name : "Product is unavailable"}</div>
        </NavLink>
    );
};
