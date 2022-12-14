import { useSelector } from "react-redux"
import './CartItem.css'

export default function CartItem({ product, amount }) {
    const removeHandler = () => {

    }
    return (
        <div>
            <div className="cart_seller_info">
                <div className="seller_profile_picture">
                    D
                </div>
                <div>{product.seller.display_name}</div>
            </div>

            <div className="cart_product_grid">
                <div className="cart_product_image">
                    <img src={product.preview_image}></img>
                </div>
                <div className="cart_grid_middle_ele">
                    <div>
                        {product.name}
                    </div>
                    <div>
                        <button
                            onClick={() => removeHandler()}
                        >Remove</button>
                    </div>
                </div>

            </div>
            <div>{amount}</div>
        </div>
    )
}
