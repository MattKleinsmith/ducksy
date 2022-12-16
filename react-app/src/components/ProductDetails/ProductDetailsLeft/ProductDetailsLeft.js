import styles from "./ProductDetailsLeft.module.css";
import ProductDetailsImages from "./ProductDetailsImages/ProductDetailsImages";
import ProductDetailsReviewList from "./ProductDetailsReviewList/ProductDetailsReviewList";

export default function ProductDetailsLeft({ product }) {
    return (
        <div className={styles.ProductDetailsLeftWrapper}>
            <div className={styles.ProductDetailsLeft}>
                <ProductDetailsImages product={product} />
                <ProductDetailsReviewList product={product} />
            </div>
        </div>
    );
}
