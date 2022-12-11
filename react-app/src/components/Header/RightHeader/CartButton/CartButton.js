// import { useState, useEffect } from "react";
// import { useSelector } from 'react-redux';

import "./CartButton.css";

export default function CartButton() {
    // const [showMenu, setShowMenu] = useState(false);
    // const ui = useSelector(state => state.ui);

    return (
        <>
            <button className="cartButton">
                <i className="fa-solid fa-cart-sellerping"></i>
            </button>
        </>
    );
}
