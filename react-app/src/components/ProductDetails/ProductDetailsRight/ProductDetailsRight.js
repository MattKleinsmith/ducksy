import { useState } from "react";
import { useSelector } from "react-redux";
import FiveStars from "../../FiveStars/FiveStars";
import "./ProductDetailsRight.css";

export default function ProductDetailsRight({ product }) {
    const [quantity, setQuantity] = useState("");
    const user = useSelector(state => state.session.user);

    const updateCart = (product) => {
        const data = window.localStorage.getItem("ducksyCarts");
        const carts = JSON.parse(data);
        const current_cart = user ? carts[user.id] : carts['guest'];
        if (String(product.id) in current_cart) current_cart[product.id] += 1;
        else current_cart[product.id] = 1;
        window.localStorage.setItem('ducksyCarts', JSON.stringify(carts));
    };

    return (
        <div className="ProductDetailsRightWrapper">
            <div className="ProductDetailsRight">
                <div>{product.seller.display_name}</div>
                <div style={{ "display": "flex" }}><span>1000 sales | <FiveStars /></span></div>
                <div>{product.name}</div>
                <div>{product.price}</div>
                <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)}></input>
                <button>Buy it now</button>
                <button
                    onClick={() => updateCart(product)}
                >
                    Add to cart</button>
                <div>{product.description}</div>
            </div>
        </div>
    );
}
