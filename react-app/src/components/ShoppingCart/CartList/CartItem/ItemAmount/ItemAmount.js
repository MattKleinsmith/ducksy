import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { updateItemAmount } from "../../../../../store/shoppingCart";


export default function ItemAmount({ amount, user, product }) {
    const dispatch = useDispatch();
    const [itemAmount, setItemAmount] = useState(amount);
    useEffect(() => {
        dispatch(updateItemAmount(product, user, itemAmount));
    }, [dispatch, itemAmount, product, user]);

    return (
        <div>
            <select
                value={itemAmount}
                onChange={(e) => {
                    setItemAmount(e.target.value);
                }}>
                {[...Array(10).keys()].map((num) => (
                    <option
                        key={num}
                        value={num}
                    >
                        {num}</option>))}
            </select>
        </div>
    )
}
