import { NavLink } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from "react";
import CartSummary from "./CartSummary/CartSummary";
import './ShoppingCart.css'


export default function ShoppingCart() {
    return (
        <div className="cartWrapper">
            <CartSummary />
        </div>
    )
}
