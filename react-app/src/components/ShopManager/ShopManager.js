import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";

import "./ShopManager.css";
// import { clearProductDetails } from "../../store/productDetails";

export default function ShopManager() {
    const dispatch = useDispatch();
    const products = useSelector(state => Object.values(state.products));

    return (
        <div className="ShopManagerWrapper">
            <div className="ShopManager">
                {products.map((product, i) =>
                    <NavLink key={i} to={`/products/${product.id}`} style={{ textDecoration: 'none' }}>
                        <ProductGridItem product={product} />
                    </NavLink>)
                }
            </div >
        </div>
    );
}
