import { NavLink } from "react-router-dom";
import { useSelector } from 'react-redux';

import styles from "./ProductGrid.module.css";
import ProductGridItem from "./ProductGridItem/ProductGridItem";
// import { clearProductDetails } from "../../store/productDetails";

export default function ProductGrid() {
    const productsAll = useSelector(state => Object.values(state.products));
    const productsBySearch = useSelector(state => Object.values(state.productsBySearch));
    const products = productsBySearch.length ? productsBySearch : productsAll;
    return (
        <div className={styles.ProductGridWrapper}>
            <div className={styles.ProductGrid}>
                {products.map((product, i) =>
                    <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                        <ProductGridItem product={product} />
                    </NavLink>)
                }
            </div >
        </div>
    );
}
