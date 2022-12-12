import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";

import "./ProductGrid.css";
import ProductGridItem from "./ProductGridItem/ProductGridItem";
import { getProducts } from "../../store/products";
// import { clearProductDetails } from "../../store/productDetails";

export default function ProductGrid() {
    const dispatch = useDispatch();
    const products = useSelector(state => Object.values(state.products));
    useEffect(() => {
        dispatch(getProducts());
        // dispatch(clearProductDetails());
    }, [dispatch]);

    return (
        <div className="ProductGridWrapper">
            <div className="ProductGrid">
                {products.map((product, i) =>
                    <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                        <ProductGridItem product={product} />
                    </NavLink>)
                }
            </div >
        </div>
    );
}
