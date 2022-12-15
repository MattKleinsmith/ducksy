import styles from "./ProductGridItem.module.css";
import ProductGridItemDescription from "./ProductGridItemDescription/ProductGridItemDescription";

export default function ProductGridItem({ product }) {
    return (
        <div className={styles.ProductGridItem}>
            <img src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/placeholder.png"; }} />
            <ProductGridItemDescription product={product} />
        </div>
    );
}
