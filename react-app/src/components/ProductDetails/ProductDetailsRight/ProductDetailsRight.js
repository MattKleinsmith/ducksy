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
                <div className={styles.sellerInfo}>
                    <div>{product.seller.display_name}</div>
                    <div className={styles.salesData}>{product.sales} sales<div>|</div><FiveStars rating={product.product_rating} /></div>
                </div>
                <div className={styles.productName}>{product.name}</div>
                <div className={styles.productPrice}>${(Math.round(product.price * 100) / 100).toFixed(2)}</div>
                {!user || user.id !== product.seller_id ?
                    <div className={styles.purchaseOptions}>
                        <label htmlFor="quantity">Quantity</label>
                        <select
                            name="quantity"
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

                        <div>
                            <button className={styles.buyItNow}
                                onClick={() => checkoutHandler(user)}
                            >Buy it now</button>
                        </div>
                        <div>
                            <button className={styles.addToCart}
                                onClick={() => {
                                    setHasAddedToCart(true);
                                    dispatch(addItemToCart(product, user, quantity));
                                }}>Add to cart</button>
                        </div>
                        {hasAddedToCart && <div className={styles.addToCartText} style={{ textAlign: "center" }}>Added to cart!</div>}
                    </div>
                    :
                    <button onClick={() => navigate(`/your/shop/listing/${product.id}`)}>Edit listing</button>
                }
                <div className={styles.description}>Description</div>
                <div className={styles.productDescription}>{product.description}</div>
            </div>
        </div>
    );
}
