import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";
import { addItemToCart } from "../../../store/shoppingCart";
import FiveStars from "../../FiveStars/FiveStars";
import "./ProductDetailsRight.css";

export default function ProductDetailsRight({ product }) {
    const [quantity, setQuantity] = useState(1);
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const navigate = useNavigate();

    return (
        <div className="ProductDetailsRightWrapper">
            <div className="ProductDetailsRight">
                <div>{product.seller.display_name}</div>
                <div style={{ "display": "flex" }}><span>1000 sales | <FiveStars /></span></div>
                <div>{product.name}</div>
                <div>{product.price}</div>
                {!user || user.id !== product.seller_id ?
                    <>
                        <label>Quantity
                            <select
                                value={quantity}
                                onChange={(e) => {
                                    setQuantity(e.target.value);
                                }}>
                                {[...Array(11).keys()].slice(1).map((num) => (
                                    <option
                                        key={num}
                                        value={num}
                                    >
                                        {num}</option>))}
                            </select>
                        </label>
                        <button>Buy it now</button>
                        <button onClick={() => {
                            console.log("onClick AddToCart");
                            dispatch(addItemToCart(product, user, quantity));
                        }}>Add to cart</button>
                    </>
                    :
                    <button onClick={() => navigate(`/your/shop/listing/${product.id}`)}>Edit listing</button>
                }
                <div>{product.description}</div>
            </div>
        </div>
    );
}
