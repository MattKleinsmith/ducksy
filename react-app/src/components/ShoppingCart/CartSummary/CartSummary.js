import { useSelector } from "react-redux";
import { useNavigate } from "react-router";
import './CartSummary.css'


export default function CartSummary({ carts }) {
    const navigate = useNavigate();
    const user = useSelector(state => state.session.user)
    const totalItems = (carts) => {
        const current_cart = user ? carts[user.id] : carts["guest"]
        const total = Object.values(current_cart).reduce((total, num) => total += num, 0);
        return total;
    };
    const itemNum = totalItems(carts)
    console.log(itemNum);

    return (
        <>
            {itemNum &&
                <div className="cartSummary">
                    <div>
                        <h1>{totalItems(carts)} items in your cart</h1>
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
