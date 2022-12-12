import { useState } from "react";
import FiveStars from "../../FiveStars/FiveStars";
import "./ProductDetailsRight.css"

export default function ProductDetailsRight({ product }) {
    const [quantity, setQuantity] = useState("");

    return (
        <div className="ProductDetailsRightWrapper">
            <div className="ProductDetailsRight">
                <div>{product.seller.display_name}</div>
                <div style={{ "display": "flex" }}><span>1000 sales | <FiveStars /></span></div>
                <div>{product.name}</div>
                <div>{product.price}</div>
                <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)}></input>
                <button>Buy it now</button>
                <button>Add to cart</button>
                <div>{product.description}</div>
            </div >
        </div >
    );
}
