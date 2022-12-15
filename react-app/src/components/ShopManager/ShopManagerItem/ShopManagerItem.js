import styles from "./ShopManagerItem.module.css"
import ShopManagerItemDescription from "./ShopManagerItemDescription/ShopManagerItemDescription";
import { useDispatch } from "react-redux";
import { setDeleteProductModal } from "../../../store/ui";
import { NavLink } from "react-router-dom";
import { setProductId } from "../../../store/productDetails";

export default function ShopManagerItem({ product }) {
    const dispatch = useDispatch();

    const onDeleteClick = async () => {
        dispatch(setProductId(product.id))
        dispatch(setDeleteProductModal(true));
    };

    const url = product.name ? `/your/shop/listing/${product.id}` : "/your/shop/listing/new"

    return (
        <div className={styles.ShopManagerItem}>
            <NavLink to={url} style={{ textDecoration: 'none' }}>
                <img src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/placeholder.png" }} />
                <ShopManagerItemDescription product={product} />
            </NavLink>
            {product.name && <div className={styles.delete} onClick={onDeleteClick}>Delete</div>}
        </div>
    );
}
