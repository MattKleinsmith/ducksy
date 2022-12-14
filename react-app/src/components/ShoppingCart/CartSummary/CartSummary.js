import { useSelector } from "react-redux";
import { useNavigate } from "react-router";
import './CartSummary.css'


export default function CartSummary({ cart_items }) {
    const navigate = useNavigate();
    const total = cart_items.reduce((total, [product_id, num]) => total += num, 0);

    return (
        <>
            {total &&
                <div className="cartSummary">
                    <div>
                        <h1>{total} items in your cart</h1>
                    </div>
                    <div>
                        <button onClick={() => navigate('/')}>
                            Keep shopping</button>
                    </div>
                </div>
            }
        </>
    )
};
