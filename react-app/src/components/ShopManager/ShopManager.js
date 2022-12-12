import { NavLink } from "react-router-dom";
import { useSelector } from 'react-redux';

import "./ShopManager.css";
import ProductGridItem from "../ProductGrid/ProductGridItem/ProductGridItem";

export default function ShopManager() {
    const user = useSelector(state => state.session.user)
    const products = useSelector(state => Object.values(state.products))
        .filter(product => product.seller_id == user.id);

    return (
        <div className="ShopManagerWrapper">
            <div className="ShopManagerTitle">
                <h1>Add draft listings to your shop.</h1>
            </div>
            <div className="ShopManager">
                {products.map((product, i) =>
                    <NavLink key={i} to={`/your/shop/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                        <ProductGridItem product={product} />
                    </NavLink>)
                }
            </div>
        </div>
    );
}
