import { useState } from "react";
import { useDispatch } from "react-redux";
import { setProductId } from "../../../store/productDetails";
import { setDeleteProductModal } from "../../../store/ui";
import FiveStars from "../../FiveStars/FiveStars";
import "./ProductDetailsRight.css"

export default function ProductDetailsRight({ product }) {
    const [quantity, setQuantity] = useState("");

    const dispatch = useDispatch();

    const updateCart = (product) => {
        const cart_data = window.localStorage.getItem("ducksyCart")
        let cart_obj;
        if (cart_data) {
            cart_obj = JSON.parse(cart_data)
            if (String(product.id) in cart_obj) cart_obj[product.id] += 1
            else cart_obj[product.id] = 1
        } else {
            cart_obj = {};
            cart_obj[product.id] = 1
        }
        window.localStorage.setItem('ducksyCart', JSON.stringify(cart_obj))
    }

    const onDeleteClick = () => {
        dispatch(setProductId(product.id))
        dispatch(setDeleteProductModal(true));
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
                <button className="button" onClick={onDeleteClick}>Delete product</button>
            </div>
        </div>
    );
}
