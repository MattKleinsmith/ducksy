import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import CartSummary from "./CartSummary/CartSummary";
import './ShoppingCart.css'
import { CartList } from "./CartList/CartList";


export default function ShoppingCart() {
    const data = window.localStorage.getItem('ducksyCart');
    const carts = JSON.parse(data);
    console.log("ShoppingCart", carts)

    return (
        <div className="cartWrapper">
            <CartSummary carts={carts} />
            <CartList carts={carts} />
        </div>
    )
}
