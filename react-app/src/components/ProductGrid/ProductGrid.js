import { NavLink, useParams } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

import styles from "./ProductGrid.module.css";
import ProductGridItem from "./ProductGridItem/ProductGridItem";
import { getProductsByCategory } from "../../store/productsBySearch";
import { useEffect } from "react";

export default function ProductGrid({ isHomepage = false }) {
    const dispatch = useDispatch();
    const { categoryName } = useParams();
    const productsAll = useSelector(state => Object.values(state.products));
    const productsBySearch = useSelector(state => Object.values(state.productsBySearch));
    let products = productsBySearch.length ? productsBySearch : productsAll;
    if (categoryName) products.reverse()
    if (isHomepage) products = products.slice(10)

    useEffect(() => {
        if (categoryName) dispatch(getProductsByCategory(categoryName));
    }, [dispatch, categoryName])

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
