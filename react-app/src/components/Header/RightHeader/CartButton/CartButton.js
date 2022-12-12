import { redirect, useNavigate } from "react-router";
import "./CartButton.css";

export default function CartButton() {
    const navigate = useNavigate()
    return (
        <>
            <button
                className="cartButton"
                onClick={() => navigate('/cart')}
            >
                <i className="fa-solid fa-cart-shopping" />
            </button>
        </>
    );
}
