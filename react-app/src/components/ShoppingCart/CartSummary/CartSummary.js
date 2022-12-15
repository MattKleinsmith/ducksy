import { useNavigate } from "react-router";
import './CartSummary.css'


export default function CartSummary({ cart_items }) {
    const navigate = useNavigate();
    const total = cart_items.length;

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
