import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";

import "./ShopManager.css";
import ProductGridItem from "../ProductGrid/ProductGridItem/ProductGridItem";

export default function ShopManager() {
    const dispatch = useDispatch();
    const products = useSelector(state => Object.values(state.products));

    return (
        <div className="ShopManagerWrapper">
            <div className="ShopManagerTitle">
                <h1>Add draft listings to your shop.</h1>
            </div>
            <div className="ShopManager">
                {products.map((product, i) =>
                    <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                        <ProductGridItem product={product} />
                    </NavLink>)
                }
            </div>
        </div>
    );
}
