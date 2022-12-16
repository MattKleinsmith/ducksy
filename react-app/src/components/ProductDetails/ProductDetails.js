import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import styles from "./ProductDetails.module.css";
import ProductDetailsLeft from "./ProductDetailsLeft/ProductDetailsLeft";
import ProductDetailsRight from "./ProductDetailsRight/ProductDetailsRight";

export default function ProductDetails() {
    const { productId } = useParams();

    const productsAll = useSelector(state => state.products);
    const productsBySearch = useSelector(state => state.productsBySearch);
    const products = productId in productsBySearch ? productsBySearch : productsAll;
    const product = products[productId];

    if (!product) return;
    return (
        <div className={styles.ProductDetailsWrapper}>
            <div className={styles.ProductDetails}>
                <ProductDetailsLeft product={product} />
                <ProductDetailsRight product={product} />
            </div>
        </div>
    );
}
