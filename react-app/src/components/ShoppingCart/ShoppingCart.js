import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import CartSummary from "./CartSummary/CartSummary";
import './ShoppingCart.css'
import { CartList } from "./CartList/CartList";
import CartCheckout from "./CartCheckout/CartCheckout";

export default function ShoppingCart() {
    const data = window.localStorage.getItem('ducksyCarts');
    const carts = JSON.parse(data);

    return (
        <div className="cartWrapper">
            <CartSummary carts={carts} />
            <div className="cart_grid_container">
                <CartList carts={carts} />
                <CartCheckout carts={carts} />
            </div>

        </div>
    )
}
