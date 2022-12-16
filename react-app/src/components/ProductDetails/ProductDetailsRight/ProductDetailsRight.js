import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router";
import { addItemToCart, checkoutNow } from "../../../store/shoppingCart";
import { setRegisterModal } from "../../../store/ui";
import FiveStars from "../../FiveStars/FiveStars";
import styles from "./ProductDetailsRight.module.css";


export default function ProductDetailsRight({ product }) {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const [quantity, setQuantity] = useState(1);
    const [hasAddedToCart, setHasAddedToCart] = useState(false);
    const checkoutHandler = user => {
        if (user) dispatch(checkoutNow(product.id, quantity))
            .then((orderId) => navigate(`/cart/checkout/${orderId}`))
        else dispatch(setRegisterModal(true))
    }

    return (
        <div className={styles.ProductDetailsRightWrapper}>
            <div className={styles.ProductDetailsRight}>
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
                        <button
                            onClick={() => checkoutHandler(user)}
                        >Buy it now</button>
                        <button onClick={() => {
                            setHasAddedToCart(true);
                            dispatch(addItemToCart(product, user, quantity));
                        }}>Add to cart</button>
                        {hasAddedToCart && <div style={{ textAlign: "center" }}>Added to cart!</div>}
                    </>
                    :
                    <button onClick={() => navigate(`/your/shop/listing/${product.id}`)}>Edit listing</button>
                }
                <div>{product.description}</div>
            </div>
        </div>
    );
}
