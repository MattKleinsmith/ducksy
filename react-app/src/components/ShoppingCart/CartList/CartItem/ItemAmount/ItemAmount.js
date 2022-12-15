import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { updateItemAmount } from "../../../../../store/shoppingCart";
import './ItemAmount.css'


export default function ItemAmount({ amount, user, product }) {
    const dispatch = useDispatch();
    const [itemAmount, setItemAmount] = useState(amount);
    useEffect(() => {
        dispatch(updateItemAmount(product, user, itemAmount));
    }, [dispatch, itemAmount, product, user]);

    return (
        <div className="cart_grid_item_amount">
            <select
                value={itemAmount}
                onChange={(e) => {
                    setItemAmount(e.target.value);
                }}>
                {[...Array(11).keys()].slice(1).map((num) => (
                    <option
                        key={num}
                        value={num}
                    >
                        {num}</option>))}
            </select>
            <div>
                {`$${(Math.round(itemAmount * product.price * 100) / 100).toFixed(2)}`}
            </div>
        </div>
    )
}
